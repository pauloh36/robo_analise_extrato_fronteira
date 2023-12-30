import os
import pandas as pd
import layout_padrao

class Validador:

    def __init__(self):
        pass

    def validador_pasta_vazia(self, caminho_arquivo):

        print('Validando pasta...')

        contador = 0

        for file in os.listdir(caminho_arquivo):

            contador += 1

        if contador == 0:
            print('\nERRO - PASTA VAZIA , INSIRA OS ARQUIVO OU AGUARDA A PASTA ATUALIZAR\nPasta: '+caminho_arquivo)
            exit()

    def validor_colunas(self, df_original):

        layout = layout_padrao.Layouy_padrao()

        df = pd.DataFrame(df_original)
        contador = 0
        contador_colunas = 0

        for coluna in df.columns:

            for i in layout.colunas_essencias:

                if coluna == i:
                    contador += 1

                    contador_colunas += 1

        return contador_colunas

    def validador_asterisco(self, df):

        qtde_linhas_df = len(df)
        qtde_asterisco = 0
        status_asterisco = ''

        for i in range(qtde_linhas_df):

            if df.loc[i, 'Origem nota fiscal'] == '**********':
                qtde_asterisco += 1

        if qtde_linhas_df == qtde_asterisco:

            status_asterisco = 'ERRO'


        return status_asterisco

