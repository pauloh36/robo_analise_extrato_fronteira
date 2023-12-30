import leitor_arquivo
import pandas as pd

pd.set_option('mode.chained_assignment', None)

class Principal():

    print('---------------- Iniciando Script ----------------\n')

    l = leitor_arquivo.Leitor_Arquivo()

    l.leitor_arquivo()

    print('\n---------------- Processo finalizado  ----------------')