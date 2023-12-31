import cfop
import codigos_tributacao
import utilidades
import pandas as pd
import filtros


class Logica_confronto:

    def __init__(self):
        self.dicionario_frames = {}
        self.c = codigos_tributacao.Codigos_Tributacao()
        self.f = filtros.Filtros()
        self.u = utilidades.Utilidades()
        self.classificao = cfop.Cfop()

    def logica_principal(self, df, filial, estado):
        print('Iniciando analise do confronto')

        df_analise_st_final = self.logica_analise_resumo_st(df, self.logica_valor_sefaz_st(df, estado),
                                                            self.logica_valor_atacadao_st(df),
                                                            self.logica_valor_atacadao_antecipado(df))

        self.dicionario_frames['ORIGINAL'] = df
        self.dicionario_frames['ASTERISCO'] = self.logica_asterisco(df, estado)
        self.dicionario_frames['DIFAL'] = self.logica_difal(df)
        self.dicionario_frames['RETIDO'] = self.logica_retido_fornecedor(df_analise_st_final)
        self.dicionario_frames['ANALISE_RESUMO'] = df_analise_st_final
        self.dicionario_frames['ANALISE_COMPLETO'] = self.logica_analise_completa(df, self.logica_valor_sefaz_st(df,
                                                                                                                 estado),
                                                                                  self.logica_valor_atacadao_desmembrado(
                                                                                      df))
        self.dicionario_frames['FORA_MES'] = self.logica_fora_mes(df, estado)

        return self.dicionario_frames

    def logica_asterisco(self, df, estado):
        print('Processando as notas não efetivadas...')

        df_asterisco = df.loc[(df['Origem nota fiscal'] == '**********')]

        df_asterisco = df_asterisco.loc[(df_asterisco['Código Receita']).isin(
            self.c.dicionario_codigos_tributacao_st[estado]), self.f.colunas_informacoes_principais]

        df_asterisco = self.u.soma_total_coluna(df_asterisco, 'Valor icms sefaz')

        return df_asterisco

    def logica_difal(self, df):
        print('Processando notas de difal...')

        df_difal = df.loc[df['CFOP'].isin(self.classificao.cfop_uso_consumo), self.f.colunas_informacoes_principais]

        return df_difal

    def logica_retido_fornecedor(self, df):

        print('Processando retido fornecedor...')

        df_retido = df.loc[(df['Origem nota fiscal'] == 'NF RETIDO FORNEC. / C PROVISAO') | (
                df['Origem nota fiscal'] == 'NF RETIDO FORNECEDOR')]

        return df_retido

    def logica_valor_sefaz_st(self, df, estado):
        print('Calculando valor de ICMS ST SEFAZ...')

        df_valor_sefaz_st = df.loc[df['Código Receita'].isin(self.c.dicionario_codigos_tributacao_st[estado])]

        # faço isso para complementar o frame principal para trazer todas as notas

        df_notas_antecipado = df.loc[
            ~df['Código Receita'].isin(self.c.dicionario_codigos_tributacao_st[estado]), ['Número nota', 'CNPJ']]

        df_valor_sefaz_st = \
            df_valor_sefaz_st[['Número nota', 'CNPJ', 'Valor icms sefaz']].groupby(['Número nota', 'CNPJ'])[
                'Valor icms sefaz'].sum().reset_index()

        df_valor_sefaz_st = df_valor_sefaz_st.drop_duplicates(subset=['Número nota', 'CNPJ'], keep='first')

        df_valor_sefaz_st = pd.concat([df_valor_sefaz_st, df_notas_antecipado])

        return df_valor_sefaz_st

    def logica_valor_atacadao_st(self, df):
        print('Calculando valor de ICMS ST ATACADAO...')

        df_contador_cods_receita = self.u.contador_cods_receita_df(df)

        df_valor_atacadao_st = df.loc[df['Tributação'].isin(self.c.lista_codigos_atacadao_st)]

        df_valor_atacadao_st = \
            df_valor_atacadao_st[['Número nota', 'CNPJ', 'Valor icms atacadao']].groupby(['Número nota', 'CNPJ'])[
                'Valor icms atacadao'].sum().reset_index()

        try:
            df_valor_atacadao_st['Número nota'] = df_valor_atacadao_st['Número nota'].astype(str).str[:-1].astype(int)
        except ValueError as e:
            print('ERRO!!! NOTA COM APENAS 1 DIGITO VERIFIQUE' + str(e))
            exit()

        df_valor_atacadao_st = pd.merge(df_valor_atacadao_st, df_contador_cods_receita, on=['Número nota', 'CNPJ'],
                                        how='left')

        df_valor_atacadao_st['ATC_ST'] = (
                df_valor_atacadao_st['Valor icms atacadao'] / df_valor_atacadao_st['CONTADOR_CODS']).fillna(0)

        df_valor_atacadao_st = df_valor_atacadao_st[['Número nota', 'CNPJ', 'ATC_ST']]

        return df_valor_atacadao_st

    def logica_valor_atacadao_antecipado(self, df):
        print('Calculando valor de ICMS ANTECIPADO ATACADAO...')

        df_contador_cods_receita = self.u.contador_cods_receita_df(df)

        df_valor_atacadao_antecipado = df.loc[df['Tributação'].isin(self.c.lista_codigos_atacadao_antecipado)]

        df_valor_atacadao_antecipado = \
            df_valor_atacadao_antecipado[['Número nota', 'CNPJ', 'Valor icms atacadao']].groupby(
                ['Número nota', 'CNPJ'])[
                'Valor icms atacadao'].sum().reset_index()

        try:
            df_valor_atacadao_antecipado['Número nota'] = df_valor_atacadao_antecipado['Número nota'].astype(str).str[
                                                          :-1].astype(int)
        except ValueError as e:
            print('ERRO!!! NOTA COM APENAS 1 DIGITO VERIFIQUE' + str(e))
            exit()

        df_valor_atacadao_antecipado = pd.merge(df_valor_atacadao_antecipado, df_contador_cods_receita,
                                                on=['Número nota', 'CNPJ'],
                                                how='left')

        df_valor_atacadao_antecipado['ATC_ANTECIPADO'] = (
                df_valor_atacadao_antecipado['Valor icms atacadao'] / df_valor_atacadao_antecipado[
            'CONTADOR_CODS']).fillna(0)

        df_valor_atacadao_antecipado = df_valor_atacadao_antecipado[['Número nota', 'CNPJ', 'ATC_ANTECIPADO']]

        return df_valor_atacadao_antecipado

    def logica_valor_atacadao_desmembrado(self, df):
        print('Calculando valor de ICMS ST ATACADAO DESMEMBRADO...')

        df_contador_cods_receita = self.u.contador_cods_receita_df(df)

        df_valor_atacadao_702 = df.loc[(df['Tributação'] == 702)]
        df_valor_atacadao_703 = df.loc[(df['Tributação'] == 703)]
        df_valor_atacadao_710 = df.loc[(df['Tributação'] == 710)]
        df_valor_atacadao_715 = df.loc[(df['Tributação'] == 715)]

        df_valor_atacadao_702 = \
            df_valor_atacadao_702[['Número nota', 'CNPJ', 'Valor icms atacadao']].groupby(
                ['Número nota', 'CNPJ'])[
                'Valor icms atacadao'].sum().reset_index()

        df_valor_atacadao_703 = \
            df_valor_atacadao_703[['Número nota', 'CNPJ', 'Valor icms atacadao']].groupby(
                ['Número nota', 'CNPJ'])[
                'Valor icms atacadao'].sum().reset_index()

        df_valor_atacadao_710 = \
            df_valor_atacadao_710[['Número nota', 'CNPJ', 'Valor icms atacadao']].groupby(
                ['Número nota', 'CNPJ'])[
                'Valor icms atacadao'].sum().reset_index()

        df_valor_atacadao_715 = \
            df_valor_atacadao_715[['Número nota', 'CNPJ', 'Valor icms atacadao']].groupby(
                ['Número nota', 'CNPJ'])[
                'Valor icms atacadao'].sum().reset_index()

        try:
            df_valor_atacadao_702['Número nota'] = df_valor_atacadao_702['Número nota'].astype(str).str[
                                                   :-1].astype(int)

            df_valor_atacadao_703['Número nota'] = df_valor_atacadao_703['Número nota'].astype(str).str[
                                                   :-1].astype(int)

            df_valor_atacadao_710['Número nota'] = df_valor_atacadao_710['Número nota'].astype(str).str[
                                                   :-1].astype(int)

            df_valor_atacadao_715['Número nota'] = df_valor_atacadao_715['Número nota'].astype(str).str[
                                                   :-1].astype(int)
        except ValueError as e:
            print('ERRO!!! NOTA COM APENAS 1 DIGITO VERIFIQUE' + str(e))
            exit()

        df_valor_atacadao_702 = pd.merge(df_valor_atacadao_702, df_contador_cods_receita,
                                         on=['Número nota', 'CNPJ'],
                                         how='left')

        df_valor_atacadao_703 = pd.merge(df_valor_atacadao_703, df_contador_cods_receita,
                                         on=['Número nota', 'CNPJ'],
                                         how='left')

        df_valor_atacadao_710 = pd.merge(df_valor_atacadao_710, df_contador_cods_receita,
                                         on=['Número nota', 'CNPJ'],
                                         how='left')

        df_valor_atacadao_715 = pd.merge(df_valor_atacadao_715, df_contador_cods_receita,
                                         on=['Número nota', 'CNPJ'],
                                         how='left')

        df_valor_atacadao_702['ATC_702'] = (
                df_valor_atacadao_702['Valor icms atacadao'] / df_valor_atacadao_702[
            'CONTADOR_CODS']).fillna(0)

        df_valor_atacadao_703['ATC_703'] = (
                df_valor_atacadao_703['Valor icms atacadao'] / df_valor_atacadao_703[
            'CONTADOR_CODS']).fillna(0)

        df_valor_atacadao_710['ATC_710'] = (
                df_valor_atacadao_710['Valor icms atacadao'] / df_valor_atacadao_710[
            'CONTADOR_CODS']).fillna(0)

        df_valor_atacadao_715['ATC_715'] = (
                df_valor_atacadao_715['Valor icms atacadao'] / df_valor_atacadao_715[
            'CONTADOR_CODS']).fillna(0)

        df_valor_atacadao_702 = df_valor_atacadao_702[['Número nota', 'CNPJ', 'ATC_702']]
        df_valor_atacadao_703 = df_valor_atacadao_703[['Número nota', 'CNPJ', 'ATC_703']]
        df_valor_atacadao_710 = df_valor_atacadao_710[['Número nota', 'CNPJ', 'ATC_710']]
        df_valor_atacadao_715 = df_valor_atacadao_715[['Número nota', 'CNPJ', 'ATC_715']]

        df_final_atacadao_desmembrado = pd.merge(df_valor_atacadao_702, df_valor_atacadao_703,
                                                 on=['CNPJ', 'Número nota'], how='left')
        df_final_atacadao_desmembrado = pd.merge(df_final_atacadao_desmembrado, df_valor_atacadao_710,
                                                 on=['CNPJ', 'Número nota'], how='left')
        df_final_atacadao_desmembrado = pd.merge(df_final_atacadao_desmembrado, df_valor_atacadao_715,
                                                 on=['CNPJ', 'Número nota'], how='left')

        return df_final_atacadao_desmembrado

    def logica_analise_resumo_st(self, df_original, df_sefaz, df_atacadao_st, df_atacadao_antecipado):
        print('Processando Analise ST e antecipado...')

        df_analise_st = pd.merge(df_atacadao_st, df_atacadao_antecipado, on=['Número nota', 'CNPJ'], how='left')

        df_analise_st = pd.merge(df_sefaz, df_analise_st, on=['Número nota', 'CNPJ'], how='left')

        df_analise_st = df_analise_st.drop_duplicates(subset=['Número nota', 'CNPJ'], keep='first')

        df_analise_st = self.u.preencher_valores_vazios(df_analise_st)

        df_analise_st['DIVERGENCIA_ST'] = df_analise_st['ATC_ST'] - df_analise_st['Valor icms sefaz']

        df_analise_st = pd.merge(self.u.informacoes_complementares_notas(df_original), df_analise_st,
                                 on=['Número nota', 'CNPJ'],
                                 how='left')

        # organizando a ordem das colunas

        df_analise_st = df_analise_st[self.f.colunas_vizualizao_final_analise_resumo]

        # filtro

        df_analise_st = df_analise_st.loc[(df_analise_st['Origem nota fiscal'] != 'NF RETIDO FORNEC. / C PROVISAO') & (df_analise_st['Origem nota fiscal'] != 'NF RETIDO FORNECEDOR') & (df_analise_st['Origem nota fiscal'] != '**********') & (~df_analise_st['CFOP'].isin(self.classificao.cfop_uso_consumo))]


        return df_analise_st

    def logica_analise_completa(self, df_original, df_sefaz, df_atacadao_desmembrado):

        df_final_completo_analise = pd.merge(df_sefaz, df_atacadao_desmembrado, on=['CNPJ', 'Número nota'], how='left')

        df_final_completo_analise = df_final_completo_analise.drop_duplicates(subset=['CNPJ', 'Número nota'],
                                                                              keep='first')

        df_final_completo_analise = self.u.preencher_valores_vazios(df_final_completo_analise)

        df_final_completo_analise = pd.merge(self.u.informacoes_complementares_notas(df_original),
                                             df_final_completo_analise,
                                             on=['Número nota', 'CNPJ'],
                                             how='left')

        # organizando a ordem das colunas

        df_final_completo_analise = df_final_completo_analise[self.f.colunas_vizualizao_final_analise_completo]

        return df_final_completo_analise

    def logica_fora_mes(self, df, estado):

        print('Processando fora mês...')

        frame_fora_mes = df[df['Código Receita'].isin(self.c.dicionario_codigos_tributacao_st[estado])]

        frame_fora_mes['PERIODO'] = frame_fora_mes['Data efetivação'].str.split(pat="/", n=1).str[1]
        frame_fora_mes['PERIODO'].fillna('NF_NAO_EFETIVADAS', inplace=True)

        total_fora_mes = frame_fora_mes[['PERIODO', 'Valor icms sefaz']].groupby(['PERIODO']).sum().reset_index()

        return total_fora_mes
