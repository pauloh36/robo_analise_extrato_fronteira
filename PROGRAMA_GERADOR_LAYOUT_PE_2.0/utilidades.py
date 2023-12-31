import pandas as pd
import grupo_icms


class Utilidades:

    def __init__(self):
        pass

    # metodo para identificar o tributo de cada nota
    def preenche_tributacao(self, df):

        grupo = grupo_icms.Grupo_icms()

        qtde_linhas_df = len(df)

        df['TIPO_IMPOSTO'] = ''

        for i in range(qtde_linhas_df):

            if df.iloc[i, 0] in grupo.lista_grupo_icms:
                print('Encontrei o grupo: ' + df.iloc[i, 0])

                df.loc[i:qtde_linhas_df, 'TIPO_IMPOSTO'] = df.iloc[i, 0]


        return df

    def filtro_df(self, df):

        # realizando os filtros , preencho com 0 minha coluna 5 e depois filtro com base na condição da mascara onde me retornou false

        df.iloc[:, 5] = df.iloc[:, 5].fillna(0)

        mascara_valor = df.iloc[:, 5] == 0

        df_filtrado = df[~mascara_valor]

        mascara_texto = df_filtrado.iloc[:, 5] == 'Nota Fiscal'

        df_filtrado = df_filtrado[~mascara_texto]

        return df_filtrado

    def mesclar_extratos(self, df_extrato_stracta, df_extrato_comum):

        df_mesclado = pd.merge(df_extrato_stracta, df_extrato_comum, on='ITEM FATURA', how='left')

        return df_mesclado

        pass


