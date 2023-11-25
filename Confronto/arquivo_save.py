import variaveis_globais
import os
import pandas as pd


class Arquivo_save:
    def __init__(self):
        self.df = pd.DataFrame()
        self.filial_encontrada = ''

    def leitor_arquivo_save(self, estado_filtro, filial_filtro):
        v = variaveis_globais.Path_arquivos()
        a = Arquivo_save()



        if estado_filtro == 'CE':

            if filial_filtro == 110:

                for file in os.listdir(v.caminho_save):

                    filial_arquivo_save = file.split('.')[1]

                    if filial_arquivo_save == 'f110':
                        print('Arquivo save encontrado : ' + file)

                        a.df = pd.read_csv(os.path.join(v.caminho_save, file), delimiter='\t', encoding='ISO-8859-1')

                        a.df = a.df.iloc[:, 0].str.split(';', expand=True)

                        a.df.iloc[:, 0] = a.df.iloc[:, 0].astype(int)  # coluna cod dos itens

                        # pegando apenas as colunas que vou usar

                        a.df = a.df.iloc[:, [0, 6, 8, 11, 13, 14, 15, 24, 25, 26, 31, 33, 37, 38, 41]]

                        # definindo o nome das colunas

                        a.df.columns = ['Mercadoria', 'GRP_ICM', 'ICM.ENT.EF', 'ICM.SAI.EF', 'ICM.SAI.CML.EF', 'ICM.POB.CML', 'ICM.POB.CON', 'TRIB', '%LUCRO IND.', 'RED.%LUCRO IND.', 'NCM', 'PRC.PAUTA IND', '%.GAR.AS', '%.GAR.AT' , 'CEST']

                        return a.df

            else:

                print('Procurando arquivo save...')

                for file in os.listdir(v.caminho_save):

                    filial_arquivo_save = file.split('.')[1]

                    if ((filial_arquivo_save == 'f080') |
                            (filial_arquivo_save == 'f082') |
                            (filial_arquivo_save == 'f144') |
                            (filial_arquivo_save == 'f158') |
                            (filial_arquivo_save == 'f173') |
                            (filial_arquivo_save == 'f189') |
                            (filial_arquivo_save == 'f304') |
                            (filial_arquivo_save == 'f305') |
                            (filial_arquivo_save == 'f828') |
                            (filial_arquivo_save == 'f836') |
                            (filial_arquivo_save == 'f840') |
                            (filial_arquivo_save == 'f871')):

                        print('Arquivo save encontrado : ' + file)

                        a.df = pd.read_csv(os.path.join(v.caminho_save, file), delimiter='\t', encoding='ISO-8859-1')

                        a.df = a.df.iloc[:, 0].str.split(';', expand=True)

                        a.df.iloc[:, 0] = a.df.iloc[:, 0].astype(int)  # coluna cod dos itens

                        # pegando apenas as colunas que vou usar

                        a.df = a.df.iloc[:, [0, 6, 8, 11, 13, 14, 15, 24, 25, 26, 31, 33, 37, 38, 41]]

                        # definindo o nome das colunas

                        a.df.columns = ['Mercadoria', 'GRP_ICM', 'ICM.ENT.EF', 'ICM.SAI.EF', 'ICM.SAI.CML.EF', 'ICM.POB.CML', 'ICM.POB.CON', 'TRIB', '%LUCRO IND.', 'RED.%LUCRO IND.', 'NCM', 'PRC.PAUTA IND', '%.GAR.AS', '%.GAR.AT' , 'CEST']

                        return a.df






        elif estado_filtro == 'PE':

            if filial_filtro == 187:

                for file in os.listdir(v.caminho_save):

                    filial_arquivo_save = file.split('.')[1]

                    if filial_arquivo_save == 'f187':
                        print('Arquivo save encontrado : ' + file)

                        a.df = pd.read_csv(os.path.join(v.caminho_save, file), delimiter='\t', encoding='ISO-8859-1')

                        a.df = a.df.iloc[:, 0].str.split(';', expand=True)

                        a.df.iloc[:, 0] = a.df.iloc[:, 0].astype(int)  # coluna cod dos itens

                        # pegando apenas as colunas que vou usar

                        a.df = a.df.iloc[:, [0, 6, 8, 11, 13, 14, 15, 24, 25, 26, 31, 33, 37, 38, 41]]

                        # definindo o nome das colunas

                        a.df.columns = ['Mercadoria', 'GRP_ICM', 'ICM.ENT.EF', 'ICM.SAI.EF', 'ICM.SAI.CML.EF', 'ICM.POB.CML', 'ICM.POB.CON', 'TRIB', '%LUCRO IND.', 'RED.%LUCRO IND.', 'NCM', 'PRC.PAUTA IND', '%.GAR.AS', '%.GAR.AT' , 'CEST']

                        return a.df

            else:

                print('Procurando arquivo save...')

                for file in os.listdir(v.caminho_save):

                    filial_arquivo_save = file.split('.')[1]

                    if ((filial_arquivo_save == 'f047') |
                            (filial_arquivo_save == 'f050') |
                            (filial_arquivo_save == 'f055') |
                            (filial_arquivo_save == 'f056') |
                            (filial_arquivo_save == 'f087') |
                            (filial_arquivo_save == 'f150') |
                            (filial_arquivo_save == 'f152') |
                            (filial_arquivo_save == 'f228') |
                            (filial_arquivo_save == 'f240') |
                            (filial_arquivo_save == 'f243') |
                            (filial_arquivo_save == 'f244') |
                            (filial_arquivo_save == 'f264') |
                            (filial_arquivo_save == 'f280') |
                            (filial_arquivo_save == 'f293') |
                            (filial_arquivo_save == 'f312') |
                            (filial_arquivo_save == 'f316') |
                            (filial_arquivo_save == 'f323') |
                            (filial_arquivo_save == 'f328') |
                            (filial_arquivo_save == 'f356') |
                            (filial_arquivo_save == 'f357') |
                            (filial_arquivo_save == 'f832') |
                            (filial_arquivo_save == 'f870')):
                        print('Arquivo save encontrado : ' + file)

                        a.df = pd.read_csv(os.path.join(v.caminho_save, file), delimiter='\t', encoding='ISO-8859-1')

                        a.df = a.df.iloc[:, 0].str.split(';', expand=True)

                        a.df.iloc[:, 0] = a.df.iloc[:, 0].astype(int)  # coluna cod dos itens

                        # pegando apenas as colunas que vou usar

                        a.df = a.df.iloc[:, [0, 6, 8, 11, 13, 14, 15, 24, 25, 26, 31, 33, 37, 38, 41]]

                        # definindo o nome das colunas

                        a.df.columns = ['Mercadoria', 'GRP_ICM', 'ICM.ENT.EF', 'ICM.SAI.EF', 'ICM.SAI.CML.EF', 'ICM.POB.CML', 'ICM.POB.CON', 'TRIB', '%LUCRO IND.', 'RED.%LUCRO IND.', 'NCM', 'PRC.PAUTA IND', '%.GAR.AS', '%.GAR.AT' , 'CEST']

                        return a.df

        elif estado_filtro == 'PB':

            print('Procurando arquivo save...')

            if filial_filtro == 114:

                for file in os.listdir(v.caminho_save):

                    filial_arquivo_save = file.split('.')[1]

                    if filial_arquivo_save == 'f114':
                        print('Arquivo save encontrado : ' + file)

                        a.df = pd.read_csv(os.path.join(v.caminho_save, file), delimiter='\t', encoding='ISO-8859-1')

                        a.df = a.df.iloc[:, 0].str.split(';', expand=True)

                        a.df.iloc[:, 0] = a.df.iloc[:, 0].astype(int)  # coluna cod dos itens

                        # pegando apenas as colunas que vou usar

                        a.df = a.df.iloc[:, [0, 6, 8, 11, 13, 14, 15, 24, 25, 26, 31, 33, 37, 38, 41]]

                        # definindo o nome das colunas

                        a.df.columns = ['Mercadoria', 'GRP_ICM', 'ICM.ENT.EF', 'ICM.SAI.EF', 'ICM.SAI.CML.EF', 'ICM.POB.CML', 'ICM.POB.CON', 'TRIB', '%LUCRO IND.', 'RED.%LUCRO IND.', 'NCM', 'PRC.PAUTA IND', '%.GAR.AS', '%.GAR.AT' , 'CEST']

                        return a.df

            else:

                for file in os.listdir(v.caminho_save):

                    filial_arquivo_save = file.split('.')[1]

                    if ((filial_arquivo_save == 'f074') |
                            (filial_arquivo_save == 'f089') |
                            (filial_arquivo_save == 'f146') |
                            (filial_arquivo_save == 'f199') |
                            (filial_arquivo_save == 'f279') |
                            (filial_arquivo_save == 'f832')):
                        print('Arquivo save encontrado : ' + file)

                        a.df = pd.read_csv(os.path.join(v.caminho_save, file), delimiter='\t', encoding='ISO-8859-1')

                        a.df = a.df.iloc[:, 0].str.split(';', expand=True)

                        a.df.iloc[:, 0] = a.df.iloc[:, 0].astype(int)  # coluna cod dos itens

                        # pegando apenas as colunas que vou usar

                        a.df = a.df.iloc[:, [0, 6, 8, 11, 13, 14, 15, 24, 25, 26, 31, 33, 37, 38, 41]]

                        # definindo o nome das colunas

                        a.df.columns = ['Mercadoria', 'GRP_ICM', 'ICM.ENT.EF', 'ICM.SAI.EF', 'ICM.SAI.CML.EF', 'ICM.POB.CML', 'ICM.POB.CON', 'TRIB', '%LUCRO IND.', 'RED.%LUCRO IND.', 'NCM', 'PRC.PAUTA IND', '%.GAR.AS', '%.GAR.AT' , 'CEST']

                        return a.df
                    
        elif estado_filtro == 'SE':

            print('Procurando arquivo save...')

            for file in os.listdir(v.caminho_save):

                filial_arquivo_save = file.split('.')[1]

                if ((filial_arquivo_save == 'f068') |
                        (filial_arquivo_save == 'f274') |
                        (filial_arquivo_save == 'f862')):
                    print('Arquivo save encontrado : ' + file)

                    a.df = pd.read_csv(os.path.join(v.caminho_save, file), delimiter='\t', encoding='ISO-8859-1')

                    a.df = a.df.iloc[:, 0].str.split(';', expand=True)

                    a.df.iloc[:, 0] = a.df.iloc[:, 0].astype(int)  # coluna cod dos itens

                    # pegando apenas as colunas que vou usar

                    a.df = a.df.iloc[:, [0, 6, 8, 11, 13, 14, 15, 24, 25, 26, 31, 33, 37, 38, 41]]

                    # definindo o nome das colunas

                    a.df.columns = ['Mercadoria', 'GRP_ICM', 'ICM.ENT.EF', 'ICM.SAI.EF', 'ICM.SAI.CML.EF', 'ICM.POB.CML', 'ICM.POB.CON', 'TRIB', '%LUCRO IND.', 'RED.%LUCRO IND.', 'NCM', 'PRC.PAUTA IND', '%.GAR.AS', '%.GAR.AT' , 'CEST']

                    return a.df
                
        elif estado_filtro == 'AC':

            print('Procurando arquivo save...')

            if filial_filtro == 308:

                for file in os.listdir(v.caminho_save):

                    filial_arquivo_save = file.split('.')[1]

                    if filial_arquivo_save == 'f308':
                        print('Arquivo save encontrado : ' + file)

                        a.df = pd.read_csv(os.path.join(v.caminho_save, file), delimiter='\t', encoding='ISO-8859-1')

                        a.df = a.df.iloc[:, 0].str.split(';', expand=True)

                        a.df.iloc[:, 0] = a.df.iloc[:, 0].astype(int)  # coluna cod dos itens

                        # pegando apenas as colunas que vou usar

                        a.df = a.df.iloc[:, [0, 6, 8, 11, 13, 14, 15, 24, 25, 26, 31, 33, 37, 38, 41]]

                        # definindo o nome das colunas

                        a.df.columns = ['Mercadoria', 'GRP_ICM', 'ICM.ENT.EF', 'ICM.SAI.EF', 'ICM.SAI.CML.EF', 'ICM.POB.CML', 'ICM.POB.CON', 'TRIB', '%LUCRO IND.', 'RED.%LUCRO IND.', 'NCM', 'PRC.PAUTA IND', '%.GAR.AS', '%.GAR.AT' , 'CEST']

                        return a.df

            else:

                for file in os.listdir(v.caminho_save):

                    filial_arquivo_save = file.split('.')[1]

                    if ((filial_arquivo_save == 'f141')):
                        print('Arquivo save encontrado : ' + file)

                        a.df = pd.read_csv(os.path.join(v.caminho_save, file), delimiter='\t', encoding='ISO-8859-1')

                        a.df = a.df.iloc[:, 0].str.split(';', expand=True)

                        a.df.iloc[:, 0] = a.df.iloc[:, 0].astype(int)  # coluna cod dos itens

                        # pegando apenas as colunas que vou usar

                        a.df = a.df.iloc[:, [0, 6, 8, 11, 13, 14, 15, 24, 25, 26, 31, 33, 37, 38, 41]]

                        # definindo o nome das colunas

                        a.df.columns = ['Mercadoria', 'GRP_ICM', 'ICM.ENT.EF', 'ICM.SAI.EF', 'ICM.SAI.CML.EF', 'ICM.POB.CML', 'ICM.POB.CON', 'TRIB', '%LUCRO IND.', 'RED.%LUCRO IND.', 'NCM', 'PRC.PAUTA IND', '%.GAR.AS', '%.GAR.AT' , 'CEST']

                        return a.df
                    
        elif estado_filtro == 'AM':

            print('Procurando arquivo save...')

            if filial_filtro == 119:

                for file in os.listdir(v.caminho_save):

                    filial_arquivo_save = file.split('.')[1]

                    if filial_arquivo_save == 'f':
                        print('Arquivo save encontrado : ' + file)

                        a.df = pd.read_csv(os.path.join(v.caminho_save, file), delimiter='\t', encoding='ISO-8859-1')

                        a.df = a.df.iloc[:, 0].str.split(';', expand=True)

                        a.df.iloc[:, 0] = a.df.iloc[:, 0].astype(int)  # coluna cod dos itens

                        # pegando apenas as colunas que vou usar

                        a.df = a.df.iloc[:, [0, 6, 8, 11, 13, 14, 15, 24, 25, 26, 31, 33, 37, 38, 41]]

                        # definindo o nome das colunas

                        a.df.columns = ['Mercadoria', 'GRP_ICM', 'ICM.ENT.EF', 'ICM.SAI.EF', 'ICM.SAI.CML.EF', 'ICM.POB.CML', 'ICM.POB.CON', 'TRIB', '%LUCRO IND.', 'RED.%LUCRO IND.', 'NCM', 'PRC.PAUTA IND', '%.GAR.AS', '%.GAR.AT' , 'CEST']

                        return a.df

            else:

                for file in os.listdir(v.caminho_save):

                    filial_arquivo_save = file.split('.')[1]

                    if ((filial_arquivo_save == 'f118') |
                        (filial_arquivo_save == 'f149') |
                        (filial_arquivo_save == 'f188') |
                        (filial_arquivo_save == 'f281') |
                        (filial_arquivo_save == 'f286') ):
                        print('Arquivo save encontrado : ' + file)

                        a.df = pd.read_csv(os.path.join(v.caminho_save, file), delimiter='\t', encoding='ISO-8859-1')

                        a.df = a.df.iloc[:, 0].str.split(';', expand=True)

                        a.df.iloc[:, 0] = a.df.iloc[:, 0].astype(int)  # coluna cod dos itens

                        # pegando apenas as colunas que vou usar

                        a.df = a.df.iloc[:, [0, 6, 8, 11, 13, 14, 15, 24, 25, 26, 31, 33, 37, 38, 41]]

                        # definindo o nome das colunas

                        a.df.columns = ['Mercadoria', 'GRP_ICM', 'ICM.ENT.EF', 'ICM.SAI.EF', 'ICM.SAI.CML.EF', 'ICM.POB.CML', 'ICM.POB.CON', 'TRIB', '%LUCRO IND.', 'RED.%LUCRO IND.', 'NCM', 'PRC.PAUTA IND', '%.GAR.AS', '%.GAR.AT' , 'CEST']

                        return a.df

        elif estado_filtro == 'AL':

            print('Procurando arquivo save...')

            if filial_filtro == 216:

                for file in os.listdir(v.caminho_save):

                    filial_arquivo_save = file.split('.')[1]

                    if filial_arquivo_save == 'f':
                        print('Arquivo save encontrado : ' + file)

                        a.df = pd.read_csv(os.path.join(v.caminho_save, file), delimiter='\t', encoding='ISO-8859-1')

                        a.df = a.df.iloc[:, 0].str.split(';', expand=True)

                        a.df.iloc[:, 0] = a.df.iloc[:, 0].astype(int)  # coluna cod dos itens

                        # pegando apenas as colunas que vou usar

                        a.df = a.df.iloc[:, [0, 6, 8, 11, 13, 14, 15, 24, 25, 26, 31, 33, 37, 38, 41]]

                        # definindo o nome das colunas

                        a.df.columns = ['Mercadoria', 'GRP_ICM', 'ICM.ENT.EF', 'ICM.SAI.EF', 'ICM.SAI.CML.EF', 'ICM.POB.CML', 'ICM.POB.CON', 'TRIB', '%LUCRO IND.', 'RED.%LUCRO IND.', 'NCM', 'PRC.PAUTA IND', '%.GAR.AS', '%.GAR.AT' , 'CEST']

                        return a.df

            else:

                for file in os.listdir(v.caminho_save):

                    filial_arquivo_save = file.split('.')[1]

                    if ((filial_arquivo_save == 'f098') |
                        (filial_arquivo_save == 'f148') |
                        (filial_arquivo_save == 'f217') |
                        (filial_arquivo_save == 'f220') |
                        (filial_arquivo_save == 'f276') ):
                        print('Arquivo save encontrado : ' + file)

                        a.df = pd.read_csv(os.path.join(v.caminho_save, file), delimiter='\t', encoding='ISO-8859-1')

                        a.df = a.df.iloc[:, 0].str.split(';', expand=True)

                        a.df.iloc[:, 0] = a.df.iloc[:, 0].astype(int)  # coluna cod dos itens

                        # pegando apenas as colunas que vou usar

                        a.df = a.df.iloc[:, [0, 6, 8, 11, 13, 14, 15, 24, 25, 26, 31, 33, 37, 38, 41]]

                        # definindo o nome das colunas

                        a.df.columns = ['Mercadoria', 'GRP_ICM', 'ICM.ENT.EF', 'ICM.SAI.EF', 'ICM.SAI.CML.EF', 'ICM.POB.CML', 'ICM.POB.CON', 'TRIB', '%LUCRO IND.', 'RED.%LUCRO IND.', 'NCM', 'PRC.PAUTA IND', '%.GAR.AS', '%.GAR.AT' , 'CEST']

                        return a.df

        elif estado_filtro == 'RR':

            print('Procurando arquivo save...')

            if filial_filtro == 248:

                for file in os.listdir(v.caminho_save):

                    filial_arquivo_save = file.split('.')[1]

                    if filial_arquivo_save == 'f':
                        print('Arquivo save encontrado : ' + file)

                        a.df = pd.read_csv(os.path.join(v.caminho_save, file), delimiter='\t', encoding='ISO-8859-1')

                        a.df = a.df.iloc[:, 0].str.split(';', expand=True)

                        a.df.iloc[:, 0] = a.df.iloc[:, 0].astype(int)  # coluna cod dos itens

                        # pegando apenas as colunas que vou usar

                        a.df = a.df.iloc[:, [0, 6, 8, 11, 13, 14, 15, 24, 25, 26, 31, 33, 37, 38, 41]]

                        # definindo o nome das colunas

                        a.df.columns = ['Mercadoria', 'GRP_ICM', 'ICM.ENT.EF', 'ICM.SAI.EF', 'ICM.SAI.CML.EF', 'ICM.POB.CML', 'ICM.POB.CON', 'TRIB', '%LUCRO IND.', 'RED.%LUCRO IND.', 'NCM', 'PRC.PAUTA IND', '%.GAR.AS', '%.GAR.AT' , 'CEST']

                        return a.df

            else:

                for file in os.listdir(v.caminho_save):

                    filial_arquivo_save = file.split('.')[1]

                    if ((filial_arquivo_save == 'f179')):
                        print('Arquivo save encontrado : ' + file)

                        a.df = pd.read_csv(os.path.join(v.caminho_save, file), delimiter='\t', encoding='ISO-8859-1')

                        a.df = a.df.iloc[:, 0].str.split(';', expand=True)

                        a.df.iloc[:, 0] = a.df.iloc[:, 0].astype(int)  # coluna cod dos itens

                        # pegando apenas as colunas que vou usar

                        a.df = a.df.iloc[:, [0, 6, 8, 11, 13, 14, 15, 24, 25, 26, 31, 33, 37, 38, 41]]

                        # definindo o nome das colunas

                        a.df.columns = ['Mercadoria', 'GRP_ICM', 'ICM.ENT.EF', 'ICM.SAI.EF', 'ICM.SAI.CML.EF', 'ICM.POB.CML', 'ICM.POB.CON', 'TRIB', '%LUCRO IND.', 'RED.%LUCRO IND.', 'NCM', 'PRC.PAUTA IND', '%.GAR.AS', '%.GAR.AT' , 'CEST']

                        return a.df

        elif estado_filtro == 'RO':

            print('Procurando arquivo save...')

            if filial_filtro == 213:

                for file in os.listdir(v.caminho_save):

                    filial_arquivo_save = file.split('.')[1]

                    if filial_arquivo_save == 'f':
                        print('Arquivo save encontrado : ' + file)

                        a.df = pd.read_csv(os.path.join(v.caminho_save, file), delimiter='\t', encoding='ISO-8859-1')

                        a.df = a.df.iloc[:, 0].str.split(';', expand=True)

                        a.df.iloc[:, 0] = a.df.iloc[:, 0].astype(int)  # coluna cod dos itens

                        # pegando apenas as colunas que vou usar

                        a.df = a.df.iloc[:, [0, 6, 8, 11, 13, 14, 15, 24, 25, 26, 31, 33, 37, 38, 41]]

                        # definindo o nome das colunas

                        a.df.columns = ['Mercadoria', 'GRP_ICM', 'ICM.ENT.EF', 'ICM.SAI.EF', 'ICM.SAI.CML.EF', 'ICM.POB.CML', 'ICM.POB.CON', 'TRIB', '%LUCRO IND.', 'RED.%LUCRO IND.', 'NCM', 'PRC.PAUTA IND', '%.GAR.AS', '%.GAR.AT' , 'CEST']

                        return a.df

            else:

                for file in os.listdir(v.caminho_save):

                    filial_arquivo_save = file.split('.')[1]

                    if ((filial_arquivo_save == 'f072') |
                        (filial_arquivo_save == 'f186') |
                        (filial_arquivo_save == 'f201')):
                        print('Arquivo save encontrado : ' + file)

                        a.df = pd.read_csv(os.path.join(v.caminho_save, file), delimiter='\t', encoding='ISO-8859-1')

                        a.df = a.df.iloc[:, 0].str.split(';', expand=True)

                        a.df.iloc[:, 0] = a.df.iloc[:, 0].astype(int)  # coluna cod dos itens

                        # pegando apenas as colunas que vou usar

                        a.df = a.df.iloc[:, [0, 6, 8, 11, 13, 14, 15, 24, 25, 26, 31, 33, 37, 38, 41]]

                        # definindo o nome das colunas

                        a.df.columns = ['Mercadoria', 'GRP_ICM', 'ICM.ENT.EF', 'ICM.SAI.EF', 'ICM.SAI.CML.EF', 'ICM.POB.CML', 'ICM.POB.CON', 'TRIB', '%LUCRO IND.', 'RED.%LUCRO IND.', 'NCM', 'PRC.PAUTA IND', '%.GAR.AS', '%.GAR.AT' , 'CEST']

                        return a.df              
              




