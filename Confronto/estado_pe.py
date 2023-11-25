import pandas as pd
import os
import numpy as np
import variaveis_globais
import conexao_bd
import utilidades
import aba_save
import aba_nf_nao_efetivadas
import aba_difal
import aba_nfs_difal_mastersaf_pe

import relatorio_asterisco


class Estado_pe:

    def __init__(self):

        self.r = relatorio_asterisco.Relatorio_asterisco()
        self.estado = 'PE'

    def logica_pe(self, arquivo_atual, n_filial, caminho_arquivo, caminho_nfs_nao_efetivadas,
                  caminho_itens_antecipado_pe,
                  caminho_correcoes_difal, df_save):
        e = Estado_pe()
        u = utilidades.Utilidades()
        aba = aba = aba_save.Aba_save()
        vg = variaveis_globais.Path_arquivos()
        ab_asterisco = aba_nf_nao_efetivadas.Aba_nf_nao_efetivadas()
        ab_difal = aba_difal.Aba_difal()
        ab_nfs_difal_mastersaf = aba_nfs_difal_mastersaf_pe.Aba_nfs_difal_mastersaf()

        r = relatorio_asterisco.Relatorio_asterisco()

        print('processando o arquivo: ' + arquivo_atual)

        path_arquivo_xlsx = os.path.join(caminho_arquivo, arquivo_atual)

        frameOriginal = pd.read_excel(path_arquivo_xlsx)

        frameOriginal['Número do documento'] = frameOriginal['Número do documento'].fillna('-')

        # frame com a data de efetivação

        dataEfetivacao = frameOriginal[
            ['Número do documento', 'Número nota', 'Data efetivação', 'Valor icms sefaz', 'Código Receita']]

        # -------------------- asterisco -------------------

        frameAsterisco = frameOriginal[
            (frameOriginal['Origem nota fiscal'] == '**********') & (frameOriginal['Número do documento'] != '-') & (
                    frameOriginal['Valor icms sefaz'] > 0.0)]

        soma_asterisco = frameAsterisco['Valor icms sefaz'].sum()

        # contando a quantidade de linhas do frame e acrecentando + 1
        # inserindo o valor total da coluna 'Valor icms sefaz'

        # frameAsterisco.loc[qtde_linhas,'Valor icms sefaz'] = soma_asterisco

        qtde_linhas = len(frameAsterisco) + 1

        frameAsterisco.loc[frameAsterisco.index.max() + 1, 'Valor icms sefaz'] = soma_asterisco

        frameAsterisco['Justificativa'] = '                           '

        frameAsterisco = frameAsterisco[
            ['Origem nota fiscal', 'Filial', 'Item Fatura', 'Número nota', 'CNPJ', 'Razão social',
             'Valor base calculo sefaz', 'Valor icms sefaz', 'Justificativa']]

        # renomeando as colunas para ter um melhor aspecto antes de inserir no banco

        # frame asterisco

        frameAsterisco = frameAsterisco.rename(columns={'Origem nota fiscal': 'ORIGEM_NF'})
        frameAsterisco = frameAsterisco.rename(columns={'Filial': 'FILIAL'})
        frameAsterisco = frameAsterisco.rename(columns={'Item Fatura': 'ITEM_FATURA'})
        frameAsterisco = frameAsterisco.rename(columns={'Número nota': 'NF'})
        frameAsterisco = frameAsterisco.rename(columns={'CNPJ': 'CNPJ'})
        frameAsterisco = frameAsterisco.rename(columns={'Razão social': 'FORNECEDOR'})
        frameAsterisco = frameAsterisco.rename(columns={'Valor base calculo sefaz': 'BASE_SEFAZ'})
        frameAsterisco = frameAsterisco.rename(columns={'Valor icms sefaz': 'VALOR_ICMS_SEFAZ'})

        # --------------------  logica ST SEFAZ  -----------------------

        analiseStSefaz = frameOriginal[(frameOriginal['Número do documento'] != '-')]

        receita_0 = (
            analiseStSefaz.loc[analiseStSefaz['Número do documento'] != '-', ['Número nota', 'Valor icms sefaz']]
            .groupby(['Número nota', 'Valor icms sefaz'])
            .sum()
        )

        # criaremos um frame para armazenas os desmembramentos

        soma_cods_sefaz = [receita_0]

        analiseStSefaz = pd.concat(soma_cods_sefaz).reset_index()

        analiseStSefaz = analiseStSefaz.groupby(['Número nota']).sum()

        # --------------------  FIM logica ST SEFAZ  -----------------------

        # calcular a qtde de códigos de receita na nota

        # pegaremos os numeros das notas filtrando o campo codigo de receita

        analiseStAtacadao = (frameOriginal.loc[frameOriginal['Número do documento'] != '-', ['Número nota']])

        # iremos criar uma coluna com valor 1 para cada numero de nome com código de receita preenchido

        analiseStAtacadao["QTDE CODS"] = 1

        analiseStAtacadao = analiseStAtacadao.groupby(['Número nota']).sum()

        analiseStAtacadao = pd.merge(analiseStAtacadao, frameOriginal, on='Número nota', how='left')

        # inserir o fam "9" no final de cada nf

        analiseStAtacadao["Número nota"] = analiseStAtacadao["Número nota"].map(str) + '9'

        # convertendo a coluna "Número nota" para int

        analiseStAtacadao["Número nota"] = analiseStAtacadao["Número nota"].astype(int)

        ## calcular o valor de provisão do atacadão cód 702 e 703 fam 9

        somaStAtacadao702 = (
            frameOriginal.loc[frameOriginal['Tributação'] == 702, ['Número nota', 'Valor icms atacadao']]).groupby(
            ['Número nota']).sum()
        somaStAtacadao703 = (
            frameOriginal.loc[frameOriginal['Tributação'] == 703, ['Número nota', 'Valor icms atacadao']]).groupby(
            ['Número nota']).sum()

        somaStAtacadao710 = (
            frameOriginal.loc[frameOriginal['Tributação'] == 710, ['Número nota', 'Valor icms atacadao']]).groupby(
            ['Número nota']).sum()
        somaStAtacadao715 = (
            frameOriginal.loc[frameOriginal['Tributação'] == 715, ['Número nota', 'Valor icms atacadao']]).groupby(
            ['Número nota']).sum()

        somaStAtacadao702 = somaStAtacadao702.rename(columns={'Valor icms atacadao': 'ATACADAO 702'})
        somaStAtacadao703 = somaStAtacadao703.rename(columns={'Valor icms atacadao': 'ATACADAO 703'})
        somaStAtacadao710 = somaStAtacadao710.rename(columns={'Valor icms atacadao': 'ATACADAO 710'})
        somaStAtacadao715 = somaStAtacadao715.rename(columns={'Valor icms atacadao': 'ATACADAO 715'})

        # junção valor st atacadão com a qtde de código de receita

        analiseStAtacadao = pd.merge(analiseStAtacadao, somaStAtacadao702, on="Número nota", how='left')

        analiseStAtacadao = pd.merge(analiseStAtacadao, somaStAtacadao703, on="Número nota", how='left')

        analiseStAtacadao = pd.merge(analiseStAtacadao, somaStAtacadao710, on="Número nota", how='left')

        analiseStAtacadao = pd.merge(analiseStAtacadao, somaStAtacadao715, on="Número nota", how='left')

        # removendo o ultimo digito do numero da nota e convertendo para int

        analiseStAtacadao['Número nota'] = analiseStAtacadao['Número nota'].astype(str).str[:-1]
        analiseStAtacadao["Número nota"] = analiseStAtacadao["Número nota"].astype(int)

        # remover a coluna qtde de cods

        analiseStAtacadao.drop(["QTDE CODS"], axis=1, inplace=True)

        # preenchendo os valores vazios com "0"

        analiseStAtacadao['ATACADAO 702'] = analiseStAtacadao['ATACADAO 702'].fillna(0)
        analiseStAtacadao['ATACADAO 703'] = analiseStAtacadao['ATACADAO 703'].fillna(0)
        analiseStAtacadao['ATACADAO 710'] = analiseStAtacadao['ATACADAO 710'].fillna(0)
        analiseStAtacadao['ATACADAO 715'] = analiseStAtacadao['ATACADAO 715'].fillna(0)

        # colunas que vamos utilizar no frame final

        analiseStAtacadao = analiseStAtacadao[
            ['Origem nota fiscal', 'CFOP', 'Item Fatura', 'Número nota', 'CNPJ', 'Razão social', 'ATACADAO 702',
             'ATACADAO 703', 'ATACADAO 710', 'ATACADAO 715']].drop_duplicates(subset=['Número nota', 'CNPJ'],
                                                                              keep='first')

        analiseStAtacadao = pd.merge(analiseStAtacadao, analiseStSefaz, on='Número nota', how='left')

        analiseStAtacadao['Valor icms sefaz'] = analiseStAtacadao['Valor icms sefaz'].fillna(0)

        # coluna total atacadão

        analiseStAtacadao['TOTAL ATACADAO'] = analiseStAtacadao['ATACADAO 702'] + analiseStAtacadao['ATACADAO 703'] + \
                                              analiseStAtacadao['ATACADAO 710'] + analiseStAtacadao['ATACADAO 715']

        # coluna divergencia

        analiseStAtacadao['Divergencia'] = analiseStAtacadao['TOTAL ATACADAO'] - analiseStAtacadao['Valor icms sefaz']

        # coluna base para contestação 

        analiseStAtacadao['BASE PARA CONTESTAÇÃO'] = ''

        analiseStAtacadao = analiseStAtacadao[
            ['Origem nota fiscal', 'CFOP', 'Item Fatura', 'Número nota', 'CNPJ', 'Razão social', 'Valor icms sefaz',
             'TOTAL ATACADAO', 'Divergencia', 'ATACADAO 702', 'ATACADAO 703', 'ATACADAO 710', 'ATACADAO 715',
             'BASE PARA CONTESTAÇÃO']]

        # filtro para não aparecer notas não efetivadas no frame final de ANALISE_ST

        analiseStAtacadao = analiseStAtacadao[(analiseStAtacadao['Origem nota fiscal'] != '**********')]

        # verifica algumas correções com base na cfop

        analiseStAtacadao = u.verifica_cfop_contestacao(analiseStAtacadao)

        #  ----------------------------------------------- fim da logica ST atacadão ----------------------------------------------

        # ------------ frame devolução --------------

        meuFrameDv = pd.DataFrame(frameOriginal)

        # remover espaços em branco e validando com try excepyt para caso a coluna não tenha nenhuma divergencia nos números como espaços e "." ou ","

        try:

            meuFrameDv['Valor total ICMS substituto Nf Dev.'] = meuFrameDv[
                'Valor total ICMS substituto Nf Dev.'].str.strip()

            # substituir "." por "" e depois trocar a "," por "."

            meuFrameDv['Valor total ICMS substituto Nf Dev.'] = meuFrameDv[
                'Valor total ICMS substituto Nf Dev.'].str.replace('.', '')
            meuFrameDv['Valor total ICMS substituto Nf Dev.'] = meuFrameDv[
                'Valor total ICMS substituto Nf Dev.'].str.replace(',', '.')

            # preencher com 0 os campos vazios

            meuFrameDv['Valor total ICMS substituto Nf Dev.'] = meuFrameDv[
                'Valor total ICMS substituto Nf Dev.'].fillna(0)

            # converter para float a coluna

            meuFrameDv["Valor total ICMS substituto Nf Dev."] = meuFrameDv[
                "Valor total ICMS substituto Nf Dev."].astype(float)

        except:

            print("valores de devolução ok")

        # filtro devoluções

        devolucao = meuFrameDv[(meuFrameDv['Número do documento'] != '-') & (meuFrameDv['Nota Devolução'] > 0)]

        # comparando se o valor da divergencia está maior ou o da devolução está maior

        devolucao['CONSIDERAR VALOR'] = np.where(
            devolucao['Valor divergência'] > devolucao['Valor total ICMS substituto Nf Dev.'], "DIVERGENCIA",
            "DEVOLUÇÃO")

        devolucao['logicaSoma'] = devolucao['Valor divergência'] + devolucao['Valor total ICMS substituto Nf Dev.']

        devolucao = devolucao[(devolucao['logicaSoma'] > 0)]

        # pegando o valor de provisão do atacadão que ja está pronto em outro frame

        frameDvStAtacadao = analiseStAtacadao[
            ['Número nota', 'ATACADAO 702', 'ATACADAO 703', 'ATACADAO 710', 'ATACADAO 715', 'TOTAL ATACADAO']]

        finalDv = pd.merge(devolucao, frameDvStAtacadao, on='Número nota', how='left')

        finalDv['Divergencia'] = finalDv['TOTAL ATACADAO'] - finalDv['Valor icms sefaz']

        # somando a coluna "valor icms atacadao" e colocando a soma no final da coluna

        total_icms_subs_dv = finalDv['Valor total ICMS substituto Nf Dev.'].sum()

        finalDv.loc[finalDv.index.max() + 1, 'Valor total ICMS substituto Nf Dev.'] = total_icms_subs_dv

        # organizando as colunas

        finalDv = finalDv[
            ['Origem nota fiscal', 'Filial', 'Item Fatura', 'Número nota', 'CNPJ', 'Razão social', 'Valor icms sefaz',
             'TOTAL ATACADAO', 'Divergencia', 'Nota Devolução', 'Valor total ICMS substituto Nf Dev.',
             'CONSIDERAR VALOR', 'ATACADAO 702', 'ATACADAO 703', 'ATACADAO 710', 'ATACADAO 715']]

        # -------------------------  fim do frame devolução   ------------------------------------------

        # ----------- frame de aba 702  ------------

        # meu frame 702 com as colunas que vou usar

        meuFrame702 = frameOriginal

        meuFrame702 = meuFrame702[
            ['Origem nota fiscal', 'Tributação', 'Número nota', 'CFOP', 'CNPJ', 'Razão social', 'Mercadoria',
             'Descrição Mercadoria', 'Valor icms atacadao', 'Código Receita']]

        # remover os valores vazios na coluna DATA EFETIVAÇÃO

        dataEfetivacao702 = dataEfetivacao

        dataEfetivacao702['Data efetivação'] = dataEfetivacao702['Data efetivação'].fillna('-')

        # filtro pelo codigo de receita para não repetir as notas
        dataEfetivacao702 = dataEfetivacao702[(dataEfetivacao702['Número do documento'] != '-')]

        # coloco a fam9 no final das notas e converto para int

        dataEfetivacao702["Número nota"] = dataEfetivacao702["Número nota"].map(str) + '9'
        dataEfetivacao702["Número nota"] = dataEfetivacao702["Número nota"].astype(int)

        # junção entre os frames

        meuFrame702 = pd.merge(meuFrame702, dataEfetivacao702, on="Número nota", how='left')

        # filtro apenas itens com código 702

        meuFrame702 = meuFrame702[(meuFrame702['Tributação'] == 702)]

        #  removo a fam9 e converto para int

        meuFrame702['Número nota'] = meuFrame702['Número nota'].astype(str).str[:-1]
        meuFrame702["Número nota"] = meuFrame702["Número nota"].astype(int)

        # filtro para remover as notas que não retornaram valores

        meuFrame702 = meuFrame702[(meuFrame702['Valor icms atacadao'] > 0)]

        # somando a coluna "valor icms atacadao" e colocando a soma no final da coluna

        total_icms_atacadao_702 = meuFrame702['Valor icms atacadao'].sum()

        meuFrame702.loc[meuFrame702.index.max() + 1, 'Valor icms atacadao'] = total_icms_atacadao_702

        # colocando as ordem das colunas

        meuFrame702 = meuFrame702[
            ['Origem nota fiscal', 'Tributação', 'Número nota', 'Data efetivação', 'CNPJ', 'Razão social', 'Mercadoria',
             'Descrição Mercadoria', 'Valor icms atacadao', 'Valor icms sefaz']]

        # inserindo informações save na aba 702

        # -------------------- fim frame aba 702 --------------------

        # ----------- frame de aba 703  ------------

        # meu frame 703 com as colunas que vou usar

        meuFrame703 = frameOriginal

        meuFrame703 = meuFrame703[
            ['Origem nota fiscal', 'Tributação', 'Número nota', 'CFOP', 'CNPJ', 'Razão social', 'Mercadoria',
             'Descrição Mercadoria', 'Valor icms atacadao', 'Código Receita']]

        # remover os valores vazios na coluna DATA EFETIVAÇÃO

        dataEfetivacao703 = dataEfetivacao

        # filtro pelo codigo de receita para não repetir as notas
        dataEfetivacao703 = dataEfetivacao703[(dataEfetivacao703['Número do documento'] != '-')]

        # coloco a fam9 no final das notas e converto para int

        dataEfetivacao703["Número nota"] = dataEfetivacao703["Número nota"].map(str) + '9'
        dataEfetivacao703["Número nota"] = dataEfetivacao703["Número nota"].astype(int)

        # junção entre os frames

        meuFrame703 = pd.merge(meuFrame703, dataEfetivacao703, on="Número nota", how='left')

        # filtro apenas itens com código 703

        meuFrame703 = meuFrame703[(meuFrame703['Tributação'] == 703)]

        #  removo a fam9 e converto para int

        meuFrame703['Número nota'] = meuFrame703['Número nota'].astype(str).str[:-1]
        meuFrame703["Número nota"] = meuFrame703["Número nota"].astype(int)

        # filtro para remover as notas que não retornaram valores

        meuFrame703 = meuFrame703[(meuFrame703['Valor icms atacadao'] > 0)]

        # somando a coluna "valor icms atacadao" e colocando a soma no final da coluna

        total_icms_atacadao_703 = meuFrame703['Valor icms atacadao'].sum()

        meuFrame703.loc[meuFrame703.index.max() + 1, 'Valor icms atacadao'] = total_icms_atacadao_703

        # colocando as ordem das colunas

        meuFrame703 = meuFrame703[
            ['Origem nota fiscal', 'Tributação', 'Número nota', 'Data efetivação', 'CNPJ', 'Razão social', 'Mercadoria',
             'Descrição Mercadoria', 'Valor icms atacadao', 'Valor icms sefaz']]

        # inserindo informações save na aba 703

        # -------------------- fim frame aba 703 --------------------

        # ----------- frame de aba 710  ------------

        # meu frame 710 com as colunas que vou usar

        meuFrame710 = frameOriginal

        meuFrame710 = meuFrame710[
            ['Origem nota fiscal', 'Tributação', 'Item Fatura', 'Número nota', 'CFOP', 'CNPJ', 'Razão social',
             'Mercadoria', 'Descrição Mercadoria', 'Valor icms atacadao', 'Código Receita']]

        # remover os valores vazios na coluna DATA EFETIVAÇÃO

        dataEfetivacao710 = dataEfetivacao

        # filtro pelo codigo de receita para não repetir as notas
        dataEfetivacao710 = dataEfetivacao710[(dataEfetivacao710['Número do documento'] != '-')]

        # coloco a fam9 no final das notas e converto para int

        dataEfetivacao710["Número nota"] = dataEfetivacao710["Número nota"].map(str) + '9'
        dataEfetivacao710["Número nota"] = dataEfetivacao710["Número nota"].astype(int)

        # junção entre os frames

        meuFrame710 = pd.merge(meuFrame710, dataEfetivacao710, on="Número nota", how='left')

        # filtro apenas itens com código 702

        meuFrame710 = meuFrame710[(meuFrame710['Tributação'] == 710)]

        #  removo a fam9 e converto para int

        meuFrame710['Número nota'] = meuFrame710['Número nota'].astype(str).str[:-1]
        meuFrame710["Número nota"] = meuFrame710["Número nota"].astype(int)

        # filtro para remover as notas que não retornaram valores

        meuFrame710 = meuFrame710[(meuFrame710['Valor icms atacadao'] > 0)]

        # -------------------- fim frame aba 710 --------------------

        # ----------- frame de aba 715  ------------

        # meu frame 715 com as colunas que vou usar

        meuFrame715 = frameOriginal

        meuFrame715 = meuFrame715[
            ['Origem nota fiscal', 'Tributação', 'Item Fatura', 'Número nota', 'CFOP', 'CNPJ', 'Razão social',
             'Mercadoria', 'Descrição Mercadoria', 'Valor icms atacadao', 'Código Receita']]

        # remover os valores vazios na coluna DATA EFETIVAÇÃO

        dataEfetivacao715 = dataEfetivacao

        # filtro pelo codigo de receita para não repetir as notas
        dataEfetivacao715 = dataEfetivacao715[(dataEfetivacao715['Número do documento'] != '-')]

        # coloco a fam9 no final das notas e converto para int

        dataEfetivacao715["Número nota"] = dataEfetivacao715["Número nota"].map(str) + '9'
        dataEfetivacao715["Número nota"] = dataEfetivacao715["Número nota"].astype(int)

        # junção entre os frames

        meuFrame715 = pd.merge(meuFrame715, dataEfetivacao715, on="Número nota", how='left')

        # filtro apenas itens com código 702

        meuFrame715 = meuFrame715[(meuFrame715['Tributação'] == 715)]

        #  removo a fam9 e converto para int

        meuFrame715['Número nota'] = meuFrame715['Número nota'].astype(str).str[:-1]
        meuFrame715["Número nota"] = meuFrame715["Número nota"].astype(int)

        # filtro para remover as notas que não retornaram valores

        meuFrame715 = meuFrame715[(meuFrame715['Valor icms atacadao'] > 0)]

        # -------------------- fim frame aba 715 --------------------

        # ------------   junção dos frames 710 e 715 para ficarem na mesma aba ---------------

        frame_antecipado_710_715 = pd.concat([meuFrame710, meuFrame715])

        # somando a coluna "valor icms atacadao" e colocando a soma no final da coluna

        total_icms_atacadao_710_715 = frame_antecipado_710_715['Valor icms atacadao'].sum()

        frame_antecipado_710_715.loc[
            frame_antecipado_710_715.index.max() + 1, 'Valor icms atacadao'] = total_icms_atacadao_710_715

        # ordem das colunas final do frame antecipado

        frame_antecipado_710_715 = frame_antecipado_710_715[
            ['Origem nota fiscal', 'Item Fatura', 'Tributação', 'Data efetivação', 'Número nota', 'CNPJ',
             'Razão social', 'Mercadoria', 'Descrição Mercadoria', 'Valor icms atacadao', 'Valor icms sefaz']]

        # ------------   FIM -  junção dos frames 710 e 715 para ficarem na mesma aba ---------------

        # --------------------  logica DIFAL  -----------------------

        # caminho correção difal

        df_notas_pagas_difal_pe = ab_difal.frame_nfs_pagas_difal_pe()

        correcao_difal = pd.read_excel(caminho_correcoes_difal)

        # filtro difal

        frameDifal = frameOriginal.loc[frameOriginal['CFOP'].isin(vg.cfop_uso_consumo)]

        # junção com a planilha de aliquota de difal por fornecedor

        # pegando algumas colunas de outro frame pronto

        analiseStAtacadao_difal = analiseStAtacadao[
            ['Número nota', 'Valor icms sefaz', 'TOTAL ATACADAO', 'Divergencia']]

        frameDifal = pd.merge(frameDifal, analiseStAtacadao_difal, on='Número nota', how='left')

        # inserindo as informações do arquivo correcao_difal

        frameDifal = pd.merge(frameDifal, correcao_difal, on='CNPJ', how='left')

        # colunas que iremos utilizar

        frameDifal['VALOR ICMS NOTA'] = frameDifal['Valor base calculo sefaz'] * frameDifal['ALIQ']

        frameDifal['VALOR ICMS NOTA'] = frameDifal['VALOR ICMS NOTA'].fillna('-')
        frameDifal['ALIQ'] = frameDifal['ALIQ'].fillna('-')

        frameDifal['OBS'] = ''
        frameDifal['NF PAGA?'] = ''

        # coluna que vamos utilizar

        frameDifal = frameDifal[
            ['Origem nota fiscal', 'Filial', 'Item Fatura', 'Número nota', 'CFOP', 'Data efetivação', 'CNPJ',
             'Razão social', 'Valor base calculo sefaz', 'ALIQ', 'VALOR ICMS NOTA', 'Valor icms sefaz_x',
             'TOTAL ATACADAO', 'Divergencia', 'OBS', 'NF PAGA?']]

        # juntando os arquivos frameDifal com notas pagas difal pe , com base no CNPJ e numero de nota



        frameDifal['CNPJ'] = frameDifal['CNPJ'].apply(u.limpar_cnpj)

        frameDifal = pd.merge(frameDifal, df_notas_pagas_difal_pe, on=['CNPJ', 'Número nota'], how='left')

        # verificando se alguma nota de uso e consumo foi paga com base no arquivo externo em excel

        qtde_linhas_df_difal = len(frameDifal)

        print('Procurando notas de difal pagas anteriormente...')

        for i in range(qtde_linhas_df_difal):

            if frameDifal.loc[i, 'FILIAL_MS'] > 0:

                frameDifal.loc[i, 'NF PAGA?'] = 'ATENÇÃO NF PAGA'

            else:

                frameDifal.loc[i, 'NF PAGA?'] = 'NÃO PAGO'

            if frameDifal.loc[i, 'Divergencia'] < 0:

                frameDifal.loc[i, 'OBS'] = 'DIFAL - USO E CONSUMO - ICMS COBRADO A MAIOR'

        frameDifal = frameDifal.drop('FILIAL_MS', axis=1)


        frameDifal.loc[qtde_linhas_df_difal, 'Origem nota fiscal'] = 'ATENÇÃO LEMBRE-SE DE ATUALIZAR O ARQUIVO COM AS NOTAS PAGAS ANTES DE UTILIZAR O ROBÔ'

        # --------------------  FIM logica DIFAL  -----------------------

        # ----------------- no caso da filial 187 por conta do beneficio informamos o itens que são pagos com auxilio de um arquivo externo

        if n_filial == 187:
            print("Filial 187 Localizada, incluido lista de itens pagos como antecipado")

            itens_antecipado = pd.read_excel(caminho_itens_antecipado_pe)

            frame_antecipado_710_715 = pd.merge(frame_antecipado_710_715, itens_antecipado, on='Mercadoria', how='left')

            frame_antecipado_710_715['PAGA ANTECIPADO'] = frame_antecipado_710_715['PAGA ANTECIPADO'].fillna('NÃO')

            frame_antecipado_710_715 = frame_antecipado_710_715[
                ['Origem nota fiscal', 'Tributação', 'Item Fatura', 'Número nota', 'Data efetivação', 'CNPJ',
                 'Razão social', 'Mercadoria', 'PAGA ANTECIPADO', 'Descrição Mercadoria', 'Valor icms atacadao',
                 'Valor icms sefaz']]

        # ----------------- FIM no caso da filial 187 por conta do beneficio informamos o itens que são pagos com auxilio de um arquivo externo

        df_itens_mercadoria_fam9 = aba.cria_aba_save(frameOriginal)

        if df_save is None:

            print('Arquivo save não encontrado')

        else:

            df_itens_mercadoria_fam9 = pd.merge(df_itens_mercadoria_fam9, df_save, on='Mercadoria', how='left')

            df_itens_mercadoria_fam9 = u.remover_mercadoria_duplicada_nota(df_itens_mercadoria_fam9)

            df_itens_mercadoria_fam9['CNPJ'] = df_itens_mercadoria_fam9['CNPJ'].apply(u.limpar_cnpj).astype(str)

            df_itens_mercadoria_fam9 = u.uf_fornecedor(df_itens_mercadoria_fam9)

        # ----------------- Inicio Frame Resumo --------------------------------------------------

        # pegando variavel pronta em outros frames

        # pegando o valor que o atacadão provisionou a maior e menor que a sefaz

        provisao_maior_atacadao = (analiseStAtacadao.loc[analiseStAtacadao['Divergencia'] > 0, ['Divergencia']])
        provisao_menor_atacadao = (analiseStAtacadao.loc[analiseStAtacadao['Divergencia'] < 0, ['Divergencia']])

        provisao_maior_atacadao = provisao_maior_atacadao['Divergencia'].sum()
        provisao_menor_atacadao = provisao_menor_atacadao['Divergencia'].sum()

        total_icms_sefaz = frameOriginal['Valor icms sefaz'].sum()

        # criando o frame resumo e dicionario

        resumo = {

            'INFORMAÇÃO': ['VALOR SEFAZ', 'ATACADAO 702', 'ATACADAO 703', 'ATACADAO 710 E 715', '', 'ASTERISCO',
                           'PROVISÃO ATC MAIOR', 'PROVISÃO ATC MENOR'],
            'VALOR': [total_icms_sefaz, total_icms_atacadao_702, total_icms_atacadao_703, total_icms_atacadao_710_715,
                      '', soma_asterisco, provisao_maior_atacadao, provisao_menor_atacadao]
        }

        frame_resumo = pd.DataFrame(resumo)

        # contador de linhas

        contador_frame_resumo = len(frame_resumo) + 7

        alerta = 'Atenção , esses valores são baseados no momento da geração , caso altere algum valor lembre-se de atualizar o mesmo nesta aba'

        frame_resumo.loc[contador_frame_resumo, 'INFORMAÇÃO'] = str(alerta)

        # -------- fim frame resumo

        # ------- frame fora mes -----------
        # pego os frames pronto 702 e 703 e quebro a data de efetivação para agrupar os valores de cada mes , em pernambuco precisa informar o valor do atacadão

        frame_fora_mes_702 = meuFrame702

        # frame_fora_mes_2 = pd.concat(frame_fora_mes_2)

        frame_fora_mes_702.loc[:, 'PERIODO'] = frame_fora_mes_702.loc[:, 'Data efetivação'].str.split(pat="/", n=1).str[
            1]

        frame_fora_mes_702 = frame_fora_mes_702.loc[:, ['PERIODO', 'Valor icms atacadao']]

        frame_fora_mes_702 = frame_fora_mes_702.rename(columns={'Valor icms atacadao': 'ATACADAO 702'})

        frame_fora_mes_702 = frame_fora_mes_702.groupby(['PERIODO']).sum()

        frame_fora_mes_703 = meuFrame703

        # frame_fora_mes_2 = pd.concat(frame_fora_mes_2)

        frame_fora_mes_703.loc[:, 'PERIODO'] = frame_fora_mes_703.loc[:, 'Data efetivação'].str.split(pat="/", n=1).str[
            1]

        frame_fora_mes_703 = frame_fora_mes_703.loc[:, ['PERIODO', 'Valor icms atacadao']]

        frame_fora_mes_703 = frame_fora_mes_703.rename(columns={'Valor icms atacadao': 'ATACADAO 703'})

        frame_fora_mes_703 = frame_fora_mes_703.groupby(['PERIODO']).sum()

        frame_fora_mes_final = pd.merge(frame_fora_mes_702, frame_fora_mes_703, on='PERIODO', how='outer')

        # ------- frame fora fim -----------

        # ------------- frame constando as notas de difal do mastersaf , puxado de um arquivo excel externo

        df_notas_difal_mastersaf = ab_nfs_difal_mastersaf.aba_nfs_difal_mastersaf(n_filial)

        # ------------------ gravação dos frames em excel -------------------

        writer = pd.ExcelWriter(caminho_arquivo + '/' + e.estado + '_' + arquivo_atual + '_ANALISE.xlsx',
                                engine='xlsxwriter')

        # Armazena cada df em uma aba diferente do mesmo arquivo

        frameOriginal.to_excel(writer, sheet_name='CONFRONTO_ORIGINAL', index=False)
        meuFrame702.to_excel(writer, sheet_name='COD_702', index=False)
        meuFrame703.to_excel(writer, sheet_name='COD_703', index=False)
        frame_antecipado_710_715.to_excel(writer, sheet_name='COD_710_715', index=False)
        frameDifal.to_excel(writer, sheet_name='DIFAL', index=False)
        df_notas_difal_mastersaf.to_excel(writer, sheet_name='DIFAL_MASTERSAF', index=False)
        finalDv.to_excel(writer, sheet_name='DEVOLUCAO', index=False)
        frameAsterisco.to_excel(writer, sheet_name='NFS_NÃO_EFETIVADAS', index=False)
        analiseStAtacadao.to_excel(writer, sheet_name='ANALISE_GERAL', index=False)
        df_itens_mercadoria_fam9.to_excel(writer, sheet_name='SAVE', index=False)
        frame_resumo.to_excel(writer, sheet_name='RESUMO', index=False)
        frame_fora_mes_final.to_excel(writer, sheet_name='FORA_MES')

        writer.close()

        # salvando as notas não efetivadas em um arquivo separado na pasta escolhida

        writer = pd.ExcelWriter(
            caminho_nfs_nao_efetivadas + '/' + e.estado + '_' + arquivo_atual + '_NFS_NAO_EFETIVADAS.xlsx',
            engine='xlsxwriter')
        frameAsterisco.to_excel(writer, sheet_name='NFS_NÃO_EFETIVADAS', index=False)

        writer.close()

        # ------------------------------------------------------------------

        # relatorio asterisco

        r.adicionar_lista(frameAsterisco)

        print('Arquivo pronto: ' + arquivo_atual)

# ---------------------------------------- FIM PE --------------------------------------------------------------------------------------------------------
