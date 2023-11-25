import pandas as pd
import path_arquivos
import os

class Importador_layout:

    def __init__(self):

        self.layout_solicitado = ''

    def importa_layout(self, nome_arquivo):

        p = path_arquivos.Path_arquivos()
        importador = Importador_layout()


        for file in os.listdir(p.caminho_layout):

            if file == nome_arquivo:

                print('Layout encontrado: '+nome_arquivo)

                importador.layout_solicitado = pd.read_excel(os.path.join(p.caminho_layout, file))

                return importador.layout_solicitado

            else:

                pass

