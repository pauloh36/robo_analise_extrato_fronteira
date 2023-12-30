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

            df_atual = pd.read_excel(os.path.join(p.pasta_arquivo_confronto_original, file))

            print('Arquivo encontrado - '+str(file))

            filial_atual , estado_atual = localizaFilial.localiza_filial(df_atual)

            dicionario_df_final = l.logica_principal(df_atual, filial_atual, estado_atual)

            g.gravacao_excel(dicionario_df_final, filial_atual, estado_atual)
