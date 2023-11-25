import pandas as pd


class Ler_arquivo:

    def __init__(self):

        pass

    def ler_arquivo_xls(self, caminho):

        df = pd.read_excel(caminho)

        if df is None:

            print('\nERRO - ARQUIVO NÃO ENCONTRADO!!!'+caminho+'\nEXECUÇÃO INTERROMPIDA')

            exit()

        return df