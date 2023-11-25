import pandas as pd
import os
import time
import variaveis_globais
import utilidades
import aba_save
import aba_difal
import aba_nf_nao_efetivadas



class Estado_rr:

    def __init__(self):
        self.estado = 'RR'

    def logica_rr(self, arquivo_atual, caminho_arquivo, caminho_nfs_nao_efetivadas, filial_filtro, df_save):

        e = Estado_rr()
        u = utilidades.Utilidades()
        aba = aba = aba_save.Aba_save()
        vg = variaveis_globais.Path_arquivos()
        ab_difal = aba_difal.Aba_difal()
        ab_asterisco = aba_nf_nao_efetivadas.Aba_nf_nao_efetivadas()

        print('processando o arquivo: ' + arquivo_atual)

        path_arquivo_xlsx = os.path.join(caminho_arquivo, arquivo_atual)

        frameOriginal = pd.read_excel(path_arquivo_xlsx)

        # ------------ asterisco --------------------

        # aba asterisco

        frameAsterisco = ab_asterisco.aba_asterisco(frameOriginal, e.estado)

        # --------------------  logica DIFAL  -----------------------

        frameDifal = ab_difal.frame_difal(frameOriginal)

        frameDifal = u.verifica_cfop_uso_consumo(frameDifal)

        # --------------------  FIM logica DIFAL  -----------------------


        # --------------------  logica ST SEFAZ  -----------------------

        analiseStSefaz = frameOriginal[(frameOriginal['Código Receita'] >= 0)]

        receita_5025 = (
            analiseStSefaz.loc[analiseStSefaz['Código Receita'] == 5025.0, ['Número nota', 'Valor icms sefaz']]
            .groupby(['Número nota', 'Valor icms sefaz'])
            .sum()
            )

        receita_5045 = (
            analiseStSefaz.loc[analiseStSefaz['Código Receita'] == 5045.0, ['Número nota', 'Valor icms sefaz']]
            .groupby(['Número nota', 'Valor icms sefaz'])
            .sum()
            )

        receita_4025 = (
            analiseStSefaz.loc[analiseStSefaz['Código Receita'] == 4025.0, ['Número nota', 'Valor icms sefaz']]
            .groupby(['Número nota', 'Valor icms sefaz'])
            .sum()
            )

        receita_4045 = (
            analiseStSefaz.loc[analiseStSefaz['Código Receita'] == 4045.0, ['Número nota', 'Valor icms sefaz']]
            .groupby(['Número nota', 'Valor icms sefaz'])
            .sum()
            )

        # criaremos um frame para armazenas os desmembramentos

        soma_sefaz_st = [receita_5025]

        soma_sefaz_antecipado = [receita_5045]

        analiseStSefaz = pd.concat(soma_sefaz_st).reset_index()
        analiseAntecipadoSefaz = pd.concat(soma_sefaz_antecipado).reset_index()

        analiseStSefaz = analiseStSefaz.groupby(['Número nota']).sum()
        analiseAntecipadoSefaz = analiseAntecipadoSefaz.groupby(['Número nota']).sum()

        analiseAntecipadoSefaz = analiseAntecipadoSefaz.rename(columns={'Valor icms sefaz': 'SEFAZ ANTECIPADO'})

        if filial_filtro == 248:
            print('Filial 248 encontrada, alterando códigos de receita')

            soma_sefaz_st = [receita_4025]

            soma_sefaz_antecipado = [receita_4045]

            analiseStSefaz = pd.concat(soma_sefaz_st).reset_index()
            analiseAntecipadoSefaz = pd.concat(soma_sefaz_antecipado).reset_index()

            analiseStSefaz = analiseStSefaz.groupby(['Número nota']).sum()
            analiseAntecipadoSefaz = analiseAntecipadoSefaz.groupby(['Número nota']).sum()

            analiseAntecipadoSefaz = analiseAntecipadoSefaz.rename(columns={'Valor icms sefaz': 'SEFAZ ANTECIPADO'})

            # --------------------  FIM logica ST SEFAZ  -----------------------

        # calcular a qtde de códigos de receita na nota

        # pegaremos os numeros das notas filtrando o campo codigo de receita

        analiseStAtacadao = (frameOriginal.loc[frameOriginal['Código Receita'] >= 0, ['Número nota']])

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

        somaStAtacadao = (somaStAtacadao702, somaStAtacadao703)

        soma_atacadao_antecipado = (somaStAtacadao710, somaStAtacadao715)

        somaStAtacadao = pd.concat(somaStAtacadao).reset_index().groupby(['Número nota']).sum()
        soma_atacadao_antecipado = pd.concat(soma_atacadao_antecipado).reset_index().groupby(['Número nota']).sum()

        soma_atacadao_antecipado = soma_atacadao_antecipado.rename(
            columns={'Valor icms atacadao': 'ATACADAO ANTECIPADO'})

        # junção valor st atacadão com a qtde de código de receita

        analiseStAtacadao = pd.merge(analiseStAtacadao, somaStAtacadao, on="Número nota", how='left')

        analiseStAtacadao = pd.merge(analiseStAtacadao, soma_atacadao_antecipado, on="Número nota", how='left')

        # removendo o ultimo digito do numero da nota e convertendo para int

        analiseStAtacadao['Número nota'] = analiseStAtacadao['Número nota'].astype(str).str[:-1]
        analiseStAtacadao["Número nota"] = analiseStAtacadao["Número nota"].astype(int)

        # dividindo o valor de st do atacadão com a qtde de códs que de cada nota

        analiseStAtacadao['VALOR ST ATACADÃO'] = analiseStAtacadao['Valor icms atacadao_y'] / analiseStAtacadao[
            'QTDE CODS']
        analiseStAtacadao['ATACADAO ANTECIPADO'] = analiseStAtacadao['ATACADAO ANTECIPADO'] / analiseStAtacadao[
            'QTDE CODS']

        # removendo as colunas que não serão mais usadas

        # analiseStAtacadao.drop(["Valor icms atacadao"], axis=1, inplace=True)
        analiseStAtacadao.drop(["QTDE CODS"], axis=1, inplace=True)

        # preenchendo os valores vazios com "0"

        analiseStAtacadao['VALOR ST ATACADÃO'] = analiseStAtacadao['VALOR ST ATACADÃO'].fillna(0)

        # colunas que vamos utilizar no frame final

        analiseStAtacadao = analiseStAtacadao[
            ['Origem nota fiscal', 'CFOP', 'Número nota', 'CNPJ', 'Razão social', 'VALOR ST ATACADÃO',
             'ATACADAO ANTECIPADO']]

        # removendo as notas duplicadas validando pelo número da nota e pelo cnpj , se forem números iguais mas de cnpj diferentes irão permanecer no frame

        analiseStAtacadao = analiseStAtacadao.drop_duplicates(subset=['Número nota', 'CNPJ'], keep='first')

        analiseStAtacadao = pd.merge(analiseStAtacadao, analiseStSefaz, on='Número nota', how='left')
        analiseStAtacadao = pd.merge(analiseStAtacadao, analiseAntecipadoSefaz, on='Número nota', how='left')

        analiseStAtacadao['Valor icms sefaz'] = analiseStAtacadao['Valor icms sefaz'].fillna(0)

        # coluna diferenca

        analiseStAtacadao['DIFERENCA ST'] = analiseStAtacadao['VALOR ST ATACADÃO'] - analiseStAtacadao[
            'Valor icms sefaz']
        analiseStAtacadao['DIFERENCA ANTECIPADO'] = analiseStAtacadao['ATACADAO ANTECIPADO'] - analiseStAtacadao[
            'SEFAZ ANTECIPADO']

        # preenchendo com 0 os campos vazios

        analiseStAtacadao['ATACADAO ANTECIPADO'] = analiseStAtacadao['ATACADAO ANTECIPADO'].fillna(0)
        analiseStAtacadao['SEFAZ ANTECIPADO'] = analiseStAtacadao['SEFAZ ANTECIPADO'].fillna(0)
        analiseStAtacadao['DIFERENCA ANTECIPADO'] = analiseStAtacadao['DIFERENCA ANTECIPADO'].fillna(0)

        # colunas que vamos utilizar no frame  analiseStAtacadao

        analiseStAtacadao = analiseStAtacadao[
            ['Origem nota fiscal', 'CFOP', 'Número nota', 'CNPJ', 'Razão social', 'Valor icms sefaz',
             'VALOR ST ATACADÃO', 'DIFERENCA ST', 'SEFAZ ANTECIPADO', 'ATACADAO ANTECIPADO', 'DIFERENCA ANTECIPADO']]

        # criando frame analise antecipado que recebera os valores da analise st já que possue todas as colunas

        frame_analise_antecipado = analiseStAtacadao

        # colunas que vamos utilizar no frame final frame_analise_antecipado

        frame_analise_antecipado = frame_analise_antecipado.loc[:, ['Origem nota fiscal', 'CFOP', 'Número nota', 'CNPJ', 'Razão social', 'SEFAZ ANTECIPADO', 'ATACADAO ANTECIPADO', 'DIFERENCA ANTECIPADO']]

        # colunas que vamos utilizar no frame final analiseStAtacadao

        analiseStAtacadao = analiseStAtacadao.loc[:,['Origem nota fiscal', 'CFOP', 'Número nota', 'CNPJ', 'Razão social', 'Valor icms sefaz',
             'VALOR ST ATACADÃO', 'DIFERENCA ST']]


        analiseStAtacadao = analiseStAtacadao.sort_values(by='DIFERENCA ST', ascending=True)

        # --------- incluindo informações de contestação no frame analise ST ------------

        analiseStAtacadao = u.verifica_analise_st(analiseStAtacadao, e.estado)

        # ------- fim logica atacadão --------

        # ----- logica devolução --------

        frame_devolucao = frameOriginal

        frame_devolucao = frame_devolucao.loc[(frame_devolucao['Valor total ICMS substituto Nf Dev.'] > 0)]

        frame_devolucao = frame_devolucao.loc[:,
                          ['Origem nota fiscal', 'Filial', 'Número nota', 'CNPJ', 'Razão social', 'Código Receita',
                           'Nota Devolução', 'Valor total ICMS substituto Nf Dev.']]

        frame_devolucao = frame_devolucao.drop_duplicates(subset=['Número nota', 'CNPJ'], keep='first')

        soma_devolucao = frame_devolucao.loc[:, 'Valor total ICMS substituto Nf Dev.'].sum()

        contador_linhas_dv = len(frame_devolucao) + 1

        frame_devolucao.loc[contador_linhas_dv, ['Valor total ICMS substituto Nf Dev.']] = soma_devolucao

        # ---------- fim devolução ----------------

        # ----------- fora mês -------------------

        # filtro para cada filial por conta dos cod de receita que são diferentes

        frame_fora_mes = frameOriginal


        if filial_filtro == 248:

            frame_fora_mes = frameOriginal.loc[(frameOriginal['Código Receita'] == 4025)]

        elif filial_filtro == 179:

            frame_fora_mes = frameOriginal.loc[(frameOriginal['Código Receita'] == 5025)]


        frame_fora_mes.loc[:, 'PERIODO'] = frame_fora_mes.loc[:, 'Data efetivação'].str.split(pat="/", n=1).str[
            1].fillna('NF_NAO_EFETIVADAS')

        frame_fora_mes = frame_fora_mes.loc[:, ['PERIODO', 'Valor icms sefaz']]

        total_fora_mes = frame_fora_mes.groupby(['PERIODO']).sum()



        # --------- fim fora mês ---------------

        # ----------- aba save --------------

        df_itens_mercadoria_fam9 = aba.cria_aba_save(frameOriginal)

        if df_save is None:

            print('Arquivo save não encontrado')

        else:

            df_itens_mercadoria_fam9 = pd.merge(df_itens_mercadoria_fam9, df_save, on='Mercadoria', how='left')

            df_itens_mercadoria_fam9 = u.remover_mercadoria_duplicada_nota(df_itens_mercadoria_fam9)

            df_itens_mercadoria_fam9['CNPJ'] = df_itens_mercadoria_fam9['CNPJ'].apply(u.limpar_cnpj).astype(str)

            df_itens_mercadoria_fam9 = u.uf_fornecedor(df_itens_mercadoria_fam9)
        # ---------------- fim aba save 


        writer = pd.ExcelWriter(caminho_arquivo + '/' + e.estado + '_' + arquivo_atual + '_ANALISE.xlsx',
                                engine='xlsxwriter')

        # Armazena cada df em uma aba diferente do mesmo arquivo

        frameOriginal.to_excel(writer, sheet_name='CONFRONTO_ORIGINAL', index=False)
        frameAsterisco.to_excel(writer, sheet_name='NF_NÃO_EFETIVADAS', index=False)
        frameDifal.to_excel(writer, sheet_name='DIFAL', index=False)
        frame_devolucao.to_excel(writer, sheet_name='DEVOLUCAO', index=False)
        df_itens_mercadoria_fam9.to_excel(writer, sheet_name='SAVE', index=False)
        analiseStAtacadao.to_excel(writer, sheet_name='ANALISE_ST', index=False)
        frame_analise_antecipado.to_excel(writer, sheet_name='ANALISE_ANTECIPADO', index=False)
        total_fora_mes.to_excel(writer, sheet_name='FORA_MES')

        writer.close()

        print('Arquivo pronto: ' + arquivo_atual)

        # salvando as notas não efetivadas em um arquivo separado na pasta escolhida

        writer = pd.ExcelWriter(
            caminho_nfs_nao_efetivadas + '/' + e.estado + '_' + arquivo_atual + '_NFS_NAO_EFETIVADAS.xlsx',
            engine='xlsxwriter')
        frameAsterisco.to_excel(writer, sheet_name='NFS_NÃO_EFETIVADAS', index=False)

        writer.close()