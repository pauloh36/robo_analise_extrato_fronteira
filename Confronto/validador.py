import variaveis_globais
import os
import pandas as pd
import cod_receita


class Validador:

    def __init__(self):

        pass

    # metodo para validar se a pasta está vazia
    def validador_pasta_vazia(self, caminho_arquivo_atual):

        contador = 0

        for file in os.listdir(caminho_arquivo_atual):
            contador += 1

        if contador == 0:

            print('\nA PASTA ESTÁ VAZIA !!! \nVERIFIQUE OS ARQUIVOS OU AGUARDE A PASTA ATUALIZAR ')

            exit()

        else:

            print('\nQuantidade de arquivos localizados : ' + str(contador) + '\n')

    # verifica se o arquivo está vazio
    def validador_arquivo_vazio(self, frameOriginal):

        contador = len(frameOriginal)
        tipo_arquivo = ''

        if contador == 0:
            tipo_arquivo = 'vazio'

        return tipo_arquivo

    # verificar se todas as colunas do confronto original existem
    def validor_colunas(self, frameOriginal):

        vg = variaveis_globais.Path_arquivos()

        df = pd.DataFrame(frameOriginal)
        contador = 0
        contador_colunas = 0

        for coluna in df.columns:

            for i in vg.colunas_confronto:

                if coluna == i:
                    contador += 1

                    contador_colunas += 1

        return contador_colunas

    def valida_cods_receita(self, df, uf_arquivo):

        lista_cod_no_arquivo = []
        cr = cod_receita.Cod_receita()

        frame_cods_receita = df

        frame_cods_receita = frame_cods_receita[['Código Receita']].fillna("-")

        frame_cods_receita = frame_cods_receita.loc[(frame_cods_receita['Código Receita'] != "-")].astype(int)

        frame_cods_receita = frame_cods_receita.drop_duplicates(subset=['Código Receita'], keep='first')

        for i in range(len(frame_cods_receita)):
            lista_cod_no_arquivo.append(frame_cods_receita.iloc[i, 0])

        if uf_arquivo == 'AC':

            if all(item in cr.codigo_ac for item in lista_cod_no_arquivo):
                return 'OK'

        elif uf_arquivo == 'AL':

            return 'OK'

        elif uf_arquivo == 'AM':

            if all(item in cr.codigo_am for item in lista_cod_no_arquivo):
                return 'OK'

        elif uf_arquivo == 'CE':

            return 'OK'

        elif uf_arquivo == 'PB':

            if all(item in cr.codigo_pb for item in lista_cod_no_arquivo):
                return 'OK'

        elif uf_arquivo == 'PE':

            return 'OK'

        elif uf_arquivo == 'RO':

            return 'OK'

        elif uf_arquivo == 'RR':

            return 'OK'

        elif uf_arquivo == 'SE':

            if all(item in cr.codigo_se for item in lista_cod_no_arquivo):
                return 'OK'

        else:

            return 'ERRO'

    # verifica se alguns arquivos necessarios existem antes de começar o processo
    def validador_arquivos_necessarios(self):

        vg = variaveis_globais.Path_arquivos()

        if os.path.exists(vg.caminho_notas_pagas_difal_pe):

            pass

        else:

            print('\nERRO - ARQUIVO: ' + vg.caminho_notas_pagas_difal_pe + ' NÃO ENCONTRADO')

            exit()

        if os.path.exists(vg.caminho_correcoes_difal):

            pass

        else:

            print('\nERRO - ARQUIVO: ' + vg.caminho_correcoes_difal + ' NÃO ENCONTRADO')

            exit()

        if os.path.exists(vg.caminho_retido_fornecedor):

            pass

        else:

            print('\nERRO - ARQUIVO: ' + vg.caminho_retido_fornecedor + ' NÃO ENCONTRADO')

            exit()

        if os.path.exists(vg.uf_fornecedores):

            pass

        else:

            print('\nERRO - ARQUIVO: ' + vg.caminho_retido_fornecedor + ' NÃO ENCONTRADO')

            exit()

    def validador_asterisco(self, df):

        qtde_linhas_df = len(df)
        qtde_asterisco = 0
        status = ''

        for i in range(qtde_linhas_df):

            if df.loc[i, 'Origem nota fiscal'] == '**********':
                qtde_asterisco += 1

        if qtde_linhas_df == qtde_asterisco:

            status = 'ERRO'


        return status


