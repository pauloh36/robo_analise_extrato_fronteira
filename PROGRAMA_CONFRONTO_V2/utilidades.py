import pandas as pd
import filtros

class Utilidades:

    def __init__(self) -> None:
        pass

    def contador_cods_receita_df(self, df):
        df_contador_codigos = df

        df_contador_codigos['Número do documento'] = df_contador_codigos['Número do documento'].fillna('-')

        df_contador_codigos = df_contador_codigos.loc[(df_contador_codigos['Número do documento'] != '-')]

        df_contador_codigos['CONTADOR_CODS'] = 1

        df_contador_codigos = df_contador_codigos[['Número nota', 'CNPJ', 'CONTADOR_CODS']].groupby(['Número nota', 'CNPJ'])[
                'CONTADOR_CODS'].sum().reset_index()

        return df_contador_codigos

    def informacoes_complementares_notas(self, df):

        f = filtros.Filtros()

        df_informacoes_notas = df.loc[(df['Código Receita'] > 0) , ['Origem nota fiscal', 'Filial', 'CFOP', 'Data efetivação', 'Número nota', 'CNPJ']]

        df_informacoes_notas = df_informacoes_notas.drop_duplicates(subset=['Número nota', 'CNPJ'] , keep='first')

        return df_informacoes_notas
