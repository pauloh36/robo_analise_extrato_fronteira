class Identificador_filial:

    def __init__(self):

        self.filial = ''
        self.estado = 'PE'

    def verifica_filial(self, inscricao_arquivo):

        identificador = Identificador_filial()

        if inscricao_arquivo == '0270329-73':

            print('Filial: 47 encontrada')

            identificador.filial = 47

            return identificador.filial
        
        if inscricao_arquivo == '0307990-23':

            print('Filial: 50 encontrada')

            identificador.filial = 50

            return identificador.filial
        
        elif inscricao_arquivo == '0329181-27':

            print('Filial: 55 encontrada')

            identificador.filial = 55

            return identificador.filial
        
        elif inscricao_arquivo == '0334975-67':

            print('Filial: 56 encontrada')

            identificador.filial = 56

            return identificador.filial

        elif inscricao_arquivo == '0372020-90':

            print('Filial: 87 encontrada')

            identificador.filial = 87

            return identificador.filial

        elif inscricao_arquivo == '0523573-17':

            print('Filial: 150 encontrada')

            identificador.filial = 150

            return identificador.filial

        elif inscricao_arquivo == '0525560-00':

            print('Filial: 152 encontrada')

            identificador.filial = 152

            return identificador.filial

        elif inscricao_arquivo == '0671969-42':

            print('Filial: 187 encontrada')

            identificador.filial = 187

            return identificador.filial


        elif inscricao_arquivo == '0784380-12':

            print('Filial: 228 encontrada')

            identificador.filial = 228

            return identificador.filial

        elif inscricao_arquivo == '0824295-02':

            print('Filial: 240 encontrada')

            identificador.filial = 240

            return identificador.filial


        elif inscricao_arquivo == '0838293-00':

            print('Filial: 243 encontrada')

            identificador.filial = 243

            return identificador.filial


        elif inscricao_arquivo == '0838310-37':

            print('Filial: 244 encontrada')

            identificador.filial = 244

            return identificador.filial


        elif inscricao_arquivo == '0877457-98':

            print('Filial: 264 encontrada')

            identificador.filial = 264

            return identificador.filial
        

        elif inscricao_arquivo == '0920425-38':

            print('Filial: 280  encontrada')

            identificador.filial = 280

            return identificador.filial
        
        elif inscricao_arquivo == '0923644-97':

            print('Filial: 293 encontrada')

            identificador.filial = 293

            return identificador.filial
        

        elif inscricao_arquivo == '0967570-19':

            print('Filial: 312 encontrada')

            identificador.filial = 312

            return identificador.filial
        
        elif inscricao_arquivo == '0973594-16':

            print('Filial: 316 encontrada')

            identificador.filial = 316

            return identificador.filial
        
        elif inscricao_arquivo == '1006970-46':

            print('Filial: 323 encontrada')

            identificador.filial = 323

            return identificador.filial
        
        elif inscricao_arquivo == '1026446-91':

            print('Filial: 328 encontrada')

            identificador.filial = 328

            return identificador.filial
        
        elif inscricao_arquivo == '1091884-11':

            print('Filial: 356 encontrada')

            identificador.filial = 356

            return identificador.filial
        
        elif inscricao_arquivo == '1092117-66':

            print('Filial: 312 encontrada')

            identificador.filial = 312

            return identificador.filial
        
        elif inscricao_arquivo == '0967570-19':

            print('Filial: 357 encontrada')

            identificador.filial = 357

            return identificador.filial

        elif inscricao_arquivo == '0381580-35':

            print('Filial: 832 encontrada')

            identificador.filial = 832

            return identificador.filial

        elif inscricao_arquivo == '0382129-35':

            print('Filial: 870 encontrada')

            identificador.filial = 870

            return identificador.filial

        else:

            print('\nERRO FILIAL NÃO ENCONTRADA, VERIFIQUE SE O ARQUIVO ESTÁ NO FORMATO CORRETO\nSCRIPT ENCERRADO !!!')

            exit()

