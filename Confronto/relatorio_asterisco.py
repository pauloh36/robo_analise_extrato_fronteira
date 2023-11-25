import pandas as pd
import grava_arquivo


class Relatorio_asterisco:
    lista_relatorio_asterisco = []
    df = pd.DataFrame()

    def adicionar_lista(self, lista):
        r = Relatorio_asterisco()
        r.lista_relatorio_asterisco.append(lista)

        return r.lista_relatorio_asterisco

    def concatenar(self):
        r = Relatorio_asterisco()

        r.df = pd.concat(r.lista_relatorio_asterisco)

        return r.df

    def resumo_asterisco(self, df_final):
        g = grava_arquivo.Grava_arquivo()

        df_final = df_final.loc[:,['FILIAL', 'VALOR_ICMS_SEFAZ']].groupby(['FILIAL']).sum()

        g.salvar_arquivo(df_final)
