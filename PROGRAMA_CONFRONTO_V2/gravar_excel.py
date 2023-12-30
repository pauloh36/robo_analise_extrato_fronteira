import path_arquivos
import pandas as pd

class Gravar_excel:

    def __init__(self) -> None:
        pass

    def gravacao_excel(self, df_dicionario, filial, estado):

        print('Iniciando Gravação...')

        p = path_arquivos.Path_arquivos()

        writer = pd.ExcelWriter(p.pasta_rescultado_confronto + '/RESULTADO' + '.xlsx', engine='xlsxwriter')

        for aba , df in df_dicionario.items():

            df.to_excel(writer, sheet_name=aba , index=False)

        writer.close()

        print('Gravação finalizada !!!')