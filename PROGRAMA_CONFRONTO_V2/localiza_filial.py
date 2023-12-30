import pandas as pd
import relacao_filiais


class Localiza_Filial():

    def __init__(self) -> None:
        self.status = ''

    def localiza_filial(self, df):

        l = Localiza_Filial()

        print('\nLocalizando Filial...')

        estado = ''
        relacaoFiliais = relacao_filiais.Relacao_Filiais()

        filial = df.iloc[1, 1]

        for e, f in relacaoFiliais.filiais.items():

            for filial_dicionario in f:

                if filial == filial_dicionario:
                    estado = e

                    l.status = 'OK'

        if estado == '':

            print('ERRO, FILIAL NÃO ENCONTRADA NO ARQUIVO')
            l.status = 'ERRO'

        print('Filial = ' + str(filial) + '\nEstado = ' + str(estado))

        return filial, estado, l.status
