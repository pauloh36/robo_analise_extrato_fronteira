import cfop
import codigos_tributacao
import utilidades
import pandas as pd
import filtros


class Logica_confronto:

    def __init__(self) -> None:
        self.dicionario_frames = {}

    def logica_principal(self, df, filial, estado):
        print('Iniciando analise do confronto')

        l = Logica_confronto()

        df_analise_st_final = l.logica_analise_st(df, l.logica_valor_sefaz_st(df, estado),
                                                  l.logica_valor_atacadao_st(df))

        l.dicionario_frames['ORIGINAL'] = df
        l.dicionario_frames['ASTERISCO'] = l.logica_asterisco(df, estado)
        l.dicionario_frames['DIFAL'] = l.logica_difal(df)
        l.dicionario_frames['RETIDO'] = l.logica_retido_fornecedor(df_analise_st_final)
        l.dicionario_frames['ANALISE_ST'] = df_analise_st_final
        l.dicionario_frames['FORA_MES'] = l.logica_fora_mes(df, estado)

        return l.dicionario_frames

    def logica_asterisco(self, df, estado):
        print('Processando as notas não efetivadas...')

        c = codigos_tributacao.Codigos_Tributacao()
        f = filtros.Filtros()
        u = utilidades.Utilidades()

        df_asterisco = df.loc[(df['Origem nota fiscal'] == '**********')]

        df_asterisco = df_asterisco.loc[(df_asterisco['Código Receita']).isin(
            c.dicionario_codigos_tributacao_st[estado]), f.colunas_informacoes_principais]

        df_asterisco = u.soma_total_coluna(df_asterisco, 'Valor icms sefaz')

        return df_asterisco

    def logica_difal(self, df):
        print('Processando notas de difal...')

        classificao = cfop.Cfop()
        f = filtros.Filtros()

        df_difal = df.loc[df['CFOP'].isin(classificao.cfop_uso_consumo), f.colunas_informacoes_principais]

        return df_difal

    def logica_retido_fornecedor(self, df):
        l = Logica_confronto()

        print('Processando retido fornecedor...')

        df_retido = df.loc[(df['Origem nota fiscal'] == 'NF RETIDO FORNEC. / C PROVISAO') | (
                df['Origem nota fiscal'] == 'NF RETIDO FORNECEDOR')]

        return df_retido

    def logica_valor_sefaz_st(self, df, estado):
        print('Calculando valor de ICMS ST SEFAZ...')

        c = codigos_tributacao.Codigos_Tributacao()

        df_valor_sefaz_st = df.loc[df['Código Receita'].isin(c.dicionario_codigos_tributacao_st[estado])]

        # faço isso para complementar o frame principal para trazer todas as notas

        df_notas_antecipado = df.loc[~df['Código Receita'].isin(c.dicionario_codigos_tributacao_st[estado]), ['Número nota', 'CNPJ']]

        df_valor_sefaz_st = \
            df_valor_sefaz_st[['Número nota', 'CNPJ', 'Valor icms sefaz']].groupby(['Número nota', 'CNPJ'])[
                'Valor icms sefaz'].sum().reset_index()

        df_valor_sefaz_st = df_valor_sefaz_st.drop_duplicates(subset=['Número nota', 'CNPJ'], keep='first')

        df_valor_sefaz_st = pd.concat([df_valor_sefaz_st, df_notas_antecipado])

        return df_valor_sefaz_st

    def logica_valor_atacadao_st(self, df):
        print('Calculando valor de ICMS ST ATACADAO...')

        c = codigos_tributacao.Codigos_Tributacao()
        u = utilidades.Utilidades()

        df_contador_cods_receita = u.contador_cods_receita_df(df)

        df_valor_atacadao_st = df.loc[df['Tributação'].isin(c.lista_codigos_atacadao_st)]

        df_valor_atacadao_st = \
            df_valor_atacadao_st[['Número nota', 'CNPJ', 'Valor icms atacadao']].groupby(['Número nota', 'CNPJ'])[
                'Valor icms atacadao'].sum().reset_index()

        try:
            df_valor_atacadao_st['Número nota'] = df_valor_atacadao_st['Número nota'].astype(str).str[:-1].astype(int)
        except:
            print('ERRO!!! NOTA COM APENAS 1 DIGITO VERIFIQUE')
            exit()

        df_valor_atacadao_st = pd.merge(df_valor_atacadao_st, df_contador_cods_receita, on=['Número nota', 'CNPJ'],
                                        how='left')

        df_valor_atacadao_st['ATACADAO_ST'] = (
                df_valor_atacadao_st['Valor icms atacadao'] / df_valor_atacadao_st['CONTADOR_CODS']).fillna(0)

        df_valor_atacadao_st = df_valor_atacadao_st[['Número nota', 'CNPJ', 'ATACADAO_ST']]

        return df_valor_atacadao_st

    def logica_analise_st(self, df_original, df_sefaz, df_atacadao):
        print('Processando Analise ST...')

        u = utilidades.Utilidades()

        df_analise = pd.merge(df_sefaz, df_atacadao, on=['Número nota', 'CNPJ'], how='left')

        df_analise = df_analise.drop_duplicates(subset=['Número nota', 'CNPJ'], keep='first')

        for i in df_analise.columns:
            df_analise[i] = df_analise[i].fillna(0)

        df_analise['DIVERGENCIA'] = df_analise['ATACADAO_ST'] - df_analise['Valor icms sefaz']

        df_analise = pd.merge(u.informacoes_complementares_notas(df_original), df_analise, on=['Número nota', 'CNPJ'],
                              how='left')

        return df_analise

    def logica_fora_mes(self, df , estado):

        print('Processando fora mês...')

        c = codigos_tributacao.Codigos_Tributacao()

        frame_fora_mes = df[df['Código Receita'].isin(c.dicionario_codigos_tributacao_st[estado])]

        frame_fora_mes['PERIODO'] = frame_fora_mes['Data efetivação'].str.split(pat="/", n=1).str[1]
        frame_fora_mes['PERIODO'].fillna('NF_NAO_EFETIVADAS', inplace=True)

        total_fora_mes = frame_fora_mes[['PERIODO', 'Valor icms sefaz']].groupby(['PERIODO']).sum().reset_index()

        return total_fora_mes
