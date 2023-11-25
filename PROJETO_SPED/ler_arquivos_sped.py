import path_arquivos
import pandas as pd
import os
import leitor_abas
import bloco_c100
import bloco_c170
import utilidades
import gravar
import validador


class Ler_arquivo_sped:

    def __init__(self):

        self.caminho_arquivo_atual = ''
        self.nome_arquivo_atual = ''
        self.ano_arquivo = ''
        self.mes_arquivo = ''
        self.ref_arquivo = ''
        self.cnpj_arquivo = ''

    def ler_arquivo(self):

        ler_arquivo = Ler_arquivo_sped()
        c100 = bloco_c100.Bloco_c100()
        c170 = bloco_c170.Bloco_c170()
        p = path_arquivos.Path_arquivos()
        g = gravar.Gravar()
        u = utilidades.Utilidades()
        v = validador.Validador()

        # objeto para ler as abas

        ler_abas = leitor_abas.Leitor_abas()

        # criando um dicionario
        dataframes = {}

        # verificando todos os arquivos na pasta

        for file in os.listdir(p.caminho_arquivo):

            u.incrementar_contador()

            ler_arquivo.nome_arquivo_atual = file

            lista_periodo_ref_arquivo = []
            lista_nome_abas_arquivo = []

            ler_arquivo.caminho_arquivo_atual = os.path.join(p.caminho_arquivo, file)

            print('---- Processando o arquivo ----\n' + file)

            arquivo_excel = pd.ExcelFile(ler_arquivo.caminho_arquivo_atual)

            abas = ler_abas.ler_abas_arquivo(ler_arquivo.caminho_arquivo_atual)

            # para cada aba inseira ela mesma no dicionario
            for i in abas:

                lista_nome_abas_arquivo.append(i)

                print('processando a aba: ' + i)

                if i == '0000':

                    print('\nAba "0000" encontrada\nProcurando as informações do arquivo...')

                    dados_da_aba = pd.read_excel(arquivo_excel, sheet_name=i)

                    dataframes[i] = dados_da_aba

                    # pegando o mes e ano do arquivo sped

                    qtde_linhas_aba_0000 = len(dados_da_aba)

                    # contador criado para extrair o periodo ref do arquivo aba "0000", isso é por que as vezes um mesmo arquivo possui varias referencias

                    for i in range(qtde_linhas_aba_0000):
                        ler_arquivo.ano_arquivo = int(pd.to_datetime(dados_da_aba.loc[i, 'DT_INI']).year)
                        ler_arquivo.ano_arquivo = int(str(ler_arquivo.ano_arquivo)[2:])

                        ler_arquivo.mes_arquivo = int(pd.to_datetime(dados_da_aba.loc[i, 'DT_INI']).month)

                        ler_arquivo.mes_arquivo = str(ler_arquivo.mes_arquivo).zfill(2)

                        ler_arquivo.ref_arquivo = str(ler_arquivo.mes_arquivo) + '/' + str(ler_arquivo.ano_arquivo)

                        lista_periodo_ref_arquivo.append(ler_arquivo.ref_arquivo)

                    # pegando o cnpj da filial do arquivo

                    ler_arquivo.cnpj_arquivo = dados_da_aba.loc[0, 'CNPJ'].astype(str)

                    print('Filial CNPJ: ' + ler_arquivo.cnpj_arquivo)

                    # printando as datas encontradas 

                    for referencia in lista_periodo_ref_arquivo:
                        print('Data do arquivo encontrada: ' + referencia)

                    print('\n')

                elif i == 'C100':

                    print('\nEncontrei o bloco C100')

                    # lendo a nossa aba baseado no nosso contador

                    dados_da_aba = pd.read_excel(arquivo_excel, sheet_name=i)

                    # contando as linhas do frame C100

                    # obtendo as chaves de acesso já formatadas

                    dataframes[i] = c100.correcao_bloco_c100(ler_arquivo.cnpj_arquivo, lista_periodo_ref_arquivo)

                elif i == 'C170':

                    print('\nEncontrei o bloco C170')

                    df_c170_original = pd.read_excel(arquivo_excel, sheet_name=i)

                    dataframes[i] = c170.correcao_bloco_c170(df_c170_original)

                else:

                    pass

                    # essa parte vai inserir as outras abas no arquivo para realizar a gravação , 
                    # no momento vamos tirar as abas que não vão ser altera pois consume muito tempo de processamento

                    # dados_da_aba = pd.read_excel(arquivo_excel, sheet_name=i)

                    # dataframes[i] = dados_da_aba

                # verificando se existe o bloco c100 , caso contrario crie o bloco

            if (v.verifica_existencia_bloco(lista_nome_abas_arquivo, 'C100')) == 'OK':

                pass

            else:

                print('\nBloco C100 não foi encontrado no arquivo, criando bloco ...')

                # lendo a nossa aba baseado no nosso contador

                dados_da_aba = pd.read_excel(arquivo_excel, sheet_name=i)

                # obtendo as chaves de acesso já formatadas

                dataframes['C100'] = c100.correcao_bloco_c100(ler_arquivo.cnpj_arquivo, lista_periodo_ref_arquivo)

            g.gravar_dicionario(dataframes, ler_arquivo.nome_arquivo_atual)
