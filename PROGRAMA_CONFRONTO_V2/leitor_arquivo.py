import os
import pandas as pd
import path_arquivos
import localiza_filial
import logica_confronto
import gravar_excel
import validador
import utilidades


class Leitor_Arquivo():

    def __init__(self) -> None:
        pass

    def leitor_arquivo(self):



        localizaFilial = localiza_filial.Localiza_Filial()
        l = logica_confronto.Logica_confronto()
        g = gravar_excel.Gravar_excel()
        p = path_arquivos.Path_arquivos()
        v = validador.Validador()
        u = utilidades.Utilidades()

        v.validador_pasta_vazia(p.pasta_arquivo_confronto_original)

        print('Localizando arquivos... \nQtde de arquivos: '+str(u.contador_arquivos_pasta(p.pasta_arquivo_confronto_original)))

        for file in os.listdir(p.pasta_arquivo_confronto_original):

            if file.endswith(('.xls', '.xlsx')):

                df_atual = pd.read_excel(os.path.join(p.pasta_arquivo_confronto_original, file))

                print('\n...............................')
                print('\nArquivo encontrado - ' + str(file))

                if v.validor_colunas(df_atual) != 41:
                    print('ERRO - COLUNAS INVALIDAS VERIFIQUE\nARQUIVO : ' + file)

                    os.rename(os.path.join(p.pasta_arquivo_confronto_original, file),
                              os.path.join(p.pasta_arquivo_confronto_original, '[ERRO-COLUNAS]' + file))

                filial_atual, estado_atual, status_filial = localizaFilial.localiza_filial(df_atual)

                if status_filial == 'ERRO':
                    os.rename(os.path.join(p.pasta_arquivo_confronto_original, file),
                              os.path.join(p.pasta_arquivo_confronto_original, '[ERRO-FILIAL]' + file))

                else:

                    dicionario_df_final = l.logica_principal(df_atual, filial_atual, estado_atual)

                    g.gravacao_excel(dicionario_df_final, file, filial_atual, estado_atual)

            else:

                print('\nArquivo no formato invalido - ' + file)

                os.rename(os.path.join(p.pasta_arquivo_confronto_original, file),
                          os.path.join(p.pasta_arquivo_confronto_original, '[ERRO-FORMATO]' + file))
