import os
import pandas as pd
import path_arquivos
import localiza_filial
import logica_confronto
import gravar_excel


class Leitor_Arquivo():

    def __init__(self) -> None:
        pass

    def leitor_arquivo(self):

        print('Localizando arquivos')

        p = path_arquivos.Path_arquivos()
        localizaFilial = localiza_filial.Localiza_Filial()
        l = logica_confronto.Logica_confronto()
        g = gravar_excel.Gravar_excel()

        for file in os.listdir(p.pasta_arquivo_confronto_original):

            if file.endswith(('.xls', '.xlsx')):

                df_atual = pd.read_excel(os.path.join(p.pasta_arquivo_confronto_original, file))

                print('\n...............................')
                print('\nArquivo encontrado - ' + str(file))

                filial_atual, estado_atual, status = localizaFilial.localiza_filial(df_atual)

                if status == 'ERRO':
                    os.rename(os.path.join(p.pasta_arquivo_confronto_original, file),
                              os.path.join(p.pasta_arquivo_confronto_original, '[ERRO-FILIAL]' + file))

                else:

                    dicionario_df_final = l.logica_principal(df_atual, filial_atual, estado_atual)

                    g.gravacao_excel(dicionario_df_final, file, filial_atual, estado_atual)

            else:

                print('\nArquivo no formato invalido - ' + file)

                os.rename(os.path.join(p.pasta_arquivo_confronto_original, file),
                          os.path.join(p.pasta_arquivo_confronto_original, '[ERRO-FORMATO]' + file))
