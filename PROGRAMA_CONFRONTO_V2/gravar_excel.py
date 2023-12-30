import path_arquivos
import pandas as pd


class Gravar_excel:

    def __init__(self) -> None:
        pass

    def gravacao_excel(self, df_dicionario, file, filial, estado):

        print('Iniciando Gravação...')

        p = path_arquivos.Path_arquivos()

        file = file.replace('.xlsx', '')
        file = file.replace('.xls', '')

        writer = pd.ExcelWriter(
            p.pasta_rescultado_confronto + '/' + estado + '_' + str(filial) + '_' + file + '_ANALISE' + '.xlsx',
            engine='xlsxwriter')

        writer_asterisco = pd.ExcelWriter(
            p.pasta_notas_nao_efetivadas + '/' + estado + '_' + str(
                filial) + '_' + file + '_NFS_NAO_EFETIVADAS' + '.xlsx',
            engine='xlsxwriter')

        for aba, df in df_dicionario.items():

            df.to_excel(writer, sheet_name=aba, index=False)

            if aba == 'ASTERISCO':
                df.to_excel(writer_asterisco, sheet_name=aba, index=False)

        writer.close()
        writer_asterisco.close()

        print('Gravação finalizada - arquivo:  ' + file)
