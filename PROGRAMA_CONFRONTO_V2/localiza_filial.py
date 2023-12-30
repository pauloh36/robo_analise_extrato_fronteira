import pandas as pd
import relacao_filiais

class Localiza_Filial():

    def __init__(self) -> None:
        pass

    def localiza_filial(self, df):

        print('\nLocalizando Filial...')

        estado = ''
        relacaoFiliais = relacao_filiais.Relacao_Filiais()

        filial = df.iloc[1,1]

        for e , f in relacaoFiliais.filiais.items():


            for filial_dicionario in f:
                
                if filial == filial_dicionario:

                    estado = e

            if e == '':

                print('ERRO, FILIAL NÃO ENCONTRADA!!!\nPROGRAMA ENCERRADO')
                exit()

        print('Filial = '+str(filial)+'\nEstado = '+str(estado))

        return filial , estado

