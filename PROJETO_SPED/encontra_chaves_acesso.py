import pandas as pd
import os


class Encontra_chaves_acesso:

    def __init__(self):
        pass

    def localiza_chaves_al(self, caminho):

        print('\nLocalizando chaves...')

        lista_chaves_localizadas = []

        for file in os.listdir(caminho):

            df_chave_atual = pd.read_excel(os.path.join(caminho, file), engine='openpyxl')

            # contador de colunas

            qtd_colunas = len(df_chave_atual.columns)
            qtde_linhas = len(df_chave_atual)

            for c in range(qtd_colunas):

                try:

                    df_chave_atual.iloc[:, c] = df_chave_atual.iloc[:, c].replace(',', '.')
                    df_chave_atual.iloc[:, c] = df_chave_atual.iloc[:, c].fillna(0)
                    df_chave_atual.iloc[:, c] = df_chave_atual.iloc[:, c].astype(str)

                except:

                    pass

                for l in range(qtde_linhas):

                    if len(df_chave_atual.iloc[l, c]) == 44:
                        lista_chaves_localizadas.append(df_chave_atual.iloc[l, c])

        df_chaves_acesso = pd.DataFrame(lista_chaves_localizadas)

        df_chaves_acesso = df_chaves_acesso.rename(columns={0: 'CHV_NFE'})

        return df_chaves_acesso
