import pandas as pd


class Leitor_abas:

    def __init__(self):
        pass

    def ler_abas_arquivo(self, arquivo):

        arquivo_excel = pd.ExcelFile(arquivo)

        abas = arquivo_excel.sheet_names

        return abas
