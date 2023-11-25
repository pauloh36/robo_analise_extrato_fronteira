import path_arquivos
import pandas as pd

class Gravar:

    def __init__(self):
        pass

    def gravar_dicionario(self, dicionario, nome_arquivo):
        p = path_arquivos.Path_arquivos()

        # realizando a gravação
        print('\nGravando arquivo sped... aguarde !')

        writer = pd.ExcelWriter(p.caminho_resultado + '/' + 'CONVERTIDO-' + nome_arquivo,
                                engine='xlsxwriter')

        for aba, df in dicionario.items():
            df.to_excel(writer, sheet_name=aba, index=False)

        writer.close()

        print('\nArquivo salvo com sucesso!\n')


    def gravar_df(self, df):
        p = path_arquivos.Path_arquivos()

        # realizando a gravação
        print('gravando arquivo chaves encontradas ... aguarde !')

        writer = pd.ExcelWriter(p.caminho_resultado + '/' + 'CHAVES_ENCONTRADAS.xlsx',
                                engine='xlsxwriter')

        df.to_excel(writer, sheet_name='resultado', index=False)

        writer.close()

        print('\nArquivo CHAVES ENCONTRADAS salvo com sucesso!\n')