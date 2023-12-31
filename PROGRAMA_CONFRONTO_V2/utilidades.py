import os
import pandas as pd
import filtros
import path_arquivos


class Utilidades:

    def __init__(self) -> None:
        pass

    def contador_cods_receita_df(self, df):
        df_contador_codigos = df

        df_contador_codigos['Número do documento'] = df_contador_codigos['Número do documento'].fillna('-')

        df_contador_codigos = df_contador_codigos.loc[(df_contador_codigos['Número do documento'] != '-')]

        df_contador_codigos['CONTADOR_CODS'] = 1

        df_contador_codigos = \
        df_contador_codigos[['Número nota', 'CNPJ', 'CONTADOR_CODS']].groupby(['Número nota', 'CNPJ'])[
            'CONTADOR_CODS'].sum().reset_index()

        return df_contador_codigos

    def informacoes_complementares_notas(self, df):
        f = filtros.Filtros()

        df_informacoes_notas = df.loc[
            (df['Código Receita'] > 0), ['Origem nota fiscal', 'Filial', 'CFOP', 'Razão social', 'Data efetivação',
                                         'Número nota', 'CNPJ']]

        df_informacoes_notas = df_informacoes_notas.drop_duplicates(subset=['Número nota', 'CNPJ'], keep='first')

        return df_informacoes_notas

    def soma_total_coluna(self, df , coluna):

        df.loc[len(df)+1, coluna] = df[coluna].sum()

        return df

    def contador_arquivos_pasta(self, caminho_pasta):

        p = path_arquivos.Path_arquivos()

        contador = 0

        for file in os.listdir(caminho_pasta):

            contador += 1

        return contador

    def preencher_valores_vazios(self, df):

        for i in df.columns:
            df[i] = df[i].fillna(0)

        return df


