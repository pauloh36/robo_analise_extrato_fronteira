import pandas as pd
import variaveis_globais
import ler_arquivo_externo
import re


class Utilidades:

    def __init__(self):
        pass

    def remover_mercadoria_duplicada_nota(self, df):

        df = df.drop_duplicates(subset=['Número nota', 'CNPJ', 'Mercadoria', 'Valor icms atacadao'], keep='first')

        return df

    # metodo para verificar as notas de pallet em pernambuco

    def verifica_cfop_contestacao(self, df):

        qtde_linhas_df = len(df)

        for i in range(qtde_linhas_df):

            if (df.iloc[i, 1] == 2920) & (df.iloc[i, 0] == 'NF SEM PROVISAO'):
                df.iloc[i, 13] = 'ISENTO REMESSA DE PALLET - ICMS COBRADO A MAIOR'

        return df

    # verifica se a nota é para uso e consumo 

    def verifica_cfop_uso_consumo(self, df):

        vg = variaveis_globais.Path_arquivos()

        qtde_linhas_df = len(df)

        for i in range(qtde_linhas_df):

            for c in vg.cfop_uso_consumo:

                if (df.iloc[i, 2] == c) & (df.iloc[i, 0] == 'NF SEM PROVISAO'):
                    df.iloc[i, 7] = 'NF PARA USO E CONSUMO'

        return df

    def localiza_estado_arquivo(self, filial):

        vg = variaveis_globais.Path_arquivos()

        status_erro = 'ERRO'

        estado_encontrado = ''

        if filial > 0:

            for i in vg.filiais_pe:

                if i == filial:
                    estado_encontrado = 'PE'

                    return estado_encontrado

            for i in vg.filiais_ac:

                if i == filial:
                    estado_encontrado = 'AC'

                    return estado_encontrado

            for i in vg.filiais_pb:

                if i == filial:
                    estado_encontrado = 'PB'

                    return estado_encontrado

            for i in vg.filiais_se:

                if i == filial:
                    estado_encontrado = 'SE'

                    return estado_encontrado

            for i in vg.filiais_rr:

                if i == filial:
                    estado_encontrado = 'RR'

                    return estado_encontrado

            for i in vg.filiais_am:

                if i == filial:
                    estado_encontrado = 'AM'

                    return estado_encontrado

            for i in vg.filiais_al:

                if i == filial:
                    estado_encontrado = 'AL'

                    return estado_encontrado

            for i in vg.filiais_ce:

                if i == filial:
                    estado_encontrado = 'CE'

                    return estado_encontrado

            for i in vg.filiais_ro:

                if i == filial:
                    estado_encontrado = 'RO'

                    return estado_encontrado

    def verifica_analise_st(self, df, uf_arquivo):

        vg = variaveis_globais.Path_arquivos()
        ler = ler_arquivo_externo.Ler_arquivo()

        print('Inserindo informações adicionais de contestação...')

        frame_analise_st = df

        qtde_linhas_df = len(frame_analise_st)

        # buscando informação na planilha externa retido fornecedor

        df_retido_fornecedor = ler.ler_arquivo_xls(vg.caminho_retido_fornecedor)

        frame_analise_st = pd.merge(frame_analise_st, df_retido_fornecedor, on=['Origem nota fiscal', 'CNPJ'],
                                    how='left')

        # -------------- fim retido --------------------

        for i in range(qtde_linhas_df):

            # VERIFICA RETIDO FORNECEDOR 

            if (frame_analise_st.iloc[i, 0] == 'NF RETIDO FORNECEDOR') & (frame_analise_st.iloc[i, 7] < -200):

                frame_analise_st.iloc[i, 8] = 'CONTESTAR O FORNECEDOR JÁ RECOLHEU O IMPOSTO'

            elif (frame_analise_st.iloc[i, 0] == 'NF RETIDO FORNECEDOR') & (frame_analise_st.iloc[i, 7] > -200) & (
                    frame_analise_st.iloc[i, 7] < 0):

                frame_analise_st.iloc[i, 8] = 'DESPESA - O FORNECEDOR RECOLHEU O IMPOSTO A MENOR'

            # VERIFICA RETIDO FORNECEDOR COM PROVISÃO

            if (frame_analise_st.iloc[i, 0] == 'NF RETIDO FORNEC. / C PROVISAO') & (frame_analise_st.iloc[i, 7] < -200):

                frame_analise_st.iloc[i, 8] = 'ATENÇÃO - VERIFICAR SE O FORNECEDOR EFETUOU O PAGAMENTO DO IMPOSTO'

            elif (frame_analise_st.iloc[i, 0] == 'NF RETIDO FORNEC. / C PROVISAO') & (
                    frame_analise_st.iloc[i, 7] > -200) & (frame_analise_st.iloc[i, 7] < 0):

                frame_analise_st.iloc[i, 8] = 'DESPESA - O FORNECEDOR RECOLHEU O IMPOSTO A MENOR'

        return frame_analise_st

    def formatar_cnpj(self, cnpj):
        cnpj_formatado = '{}.{}.{}/{}-{}'.format(cnpj[:2], cnpj[2:5], cnpj[5:8], cnpj[8:12], cnpj[12:])
        return cnpj_formatado

    # metodo para localizar a filial do arquivo em excel

    def localiza_filial(self, df):

        filial_arquivo = df['Filial'].loc[0]

        return filial_arquivo

    # funcao para deixar os números em float e remover carateres especiais
    def limpar_e_converter_dados_para_float(self, valor):
        # Remove caracteres especiais usando expressão regular
        valor_sem_especiais = re.sub(r'[^\d.,]+', '', valor)
        # Substitui vírgulas por pontos para garantir que seja um número float válido
        valor_sem_especiais = valor_sem_especiais.replace(',', '.')
        # Tenta converter para float
        try:
            return float(valor_sem_especiais)
        except ValueError:
            return None  # Retorna None se não for possível converter

    def limpar_e_converter_dados_para_int(self, valor):
        # Remove caracteres especiais usando expressão regular
        valor_sem_especiais = re.sub(r'[^\d]+', '', valor)
        # Tenta converter para int
        try:
            return int(valor_sem_especiais)
        except ValueError:
            return None  # Retorna None se não for possível converter

    def limpar_cnpj(self, cnpj):
        # Remove todos os caracteres não numéricos
        cnpj_limpo = ''.join(filter(str.isdigit, cnpj))
        # Preenche com zeros à esquerda para completar 14 dígitos
        cnpj_formatado = cnpj_limpo.zfill(14)
        return cnpj_formatado

    # Função para ler o valor atual do contador no arquivo externo
    def ler_contador(self):
        vg = variaveis_globais.Path_arquivos()

        try:
            with open(vg.contador_processos, 'r') as arquivo:
                valor = int(arquivo.read())
                return valor
        except FileNotFoundError:
            return 0  # Valor padrão se o arquivo não existir

    # Função para incrementar o contador e salvar o novo valor no arquivo
    def incrementar_contador(self):
        vg = variaveis_globais.Path_arquivos()
        u = Utilidades()

        valor_atual = u.ler_contador()
        novo_valor = valor_atual + 1

        with open(vg.contador_processos, 'w') as arquivo:
            arquivo.write(str(novo_valor))

    def uf_fornecedor(self, df):

        print('Localizando UF dos fornecedores...')

        ler = ler_arquivo_externo.Ler_arquivo()
        v = variaveis_globais.Path_arquivos()
        u = Utilidades()

        # importando o arquivo com os UF dos fornecedores

        df_uf = ler.ler_arquivo_xls(v.uf_fornecedores)

        # removendo os carateres especiais da coluna cnpj

        df_uf['CNPJ'] = df_uf['CNPJ'].apply(u.limpar_cnpj).astype(str)

        # junstando as tabelas save e UF fornecedor

        df = pd.merge(df, df_uf, on='CNPJ', how='left')

        return df
