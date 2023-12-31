import pandas as pd
import os
import path_arquivos
import Gravar
import utilidades
import identificador_filial
import layout_padrao


class Leitor_arquivo_stracta:

    def __init__(self):
        pass

    def leitor_arquivo(self):

        p = path_arquivos.Path_arquivo()
        g = Gravar.Gravar()
        u = utilidades.Utilidades()
        identifica_filial = identificador_filial.Identificador_filial()
        layout_p = layout_padrao.Layout()

        lista_df_completa_extrato_stracta = []

        for arquivo in os.listdir(p.caminho_arquivo_stracta):

            if arquivo.endswith('.xlsx'):

                df_arquivo_atual = pd.read_excel(os.path.join(p.caminho_arquivo_stracta, arquivo), engine='openpyxl')

                print('\nProcessando o arquivo ' + arquivo + '\n')

                # obtendo algumas informações do arquivo

                inscricao_arquivo = df_arquivo_atual.iloc[0, 1]
                filial = identifica_filial.verifica_filial(inscricao_arquivo)
                n_extrato = df_arquivo_atual.iloc[4, 1]

                # identificado a tributação de cada nota

                df_arquivo_atual = u.preenche_tributacao(df_arquivo_atual)

                # filtrando o frame

                df_arquivo_atual = u.filtro_df(df_arquivo_atual)

                df_infomacoes = pd.DataFrame()


                df_infomacoes['ITEM FATURA'] = df_arquivo_atual.iloc[:, 0]
                #df_infomacoes['CNPJ'] = df_arquivo_atual.iloc[:, 4]
                #df_infomacoes['NUM NOTA'] = df_arquivo_atual.iloc[:, 5]
                #df_infomacoes['DT POSTO FISCAL'] = ''
                #df_infomacoes['DT POSTO FISCAL'] = ''
                df_infomacoes['VLR ICMS'] = df_arquivo_atual.iloc[:, 6]
                df_infomacoes['VLR ICMS ANTEC'] = df_arquivo_atual.iloc[:, 6]
                #df_infomacoes['VLR BASE CALCULO'] = df_arquivo_atual.iloc[:, 6]
                #df_infomacoes['VLR BASE ANTEC'] = df_arquivo_atual.iloc[:, 6]
                #df_infomacoes['VLR TOTAL NOTA'] = df_arquivo_atual.iloc[:, 6]
                #df_infomacoes['UF'] = df_arquivo_atual.iloc[:, 3]
                df_infomacoes['COD_RECEITA'] = df_arquivo_atual.iloc[:, 7]
                #df_infomacoes.loc[:, 'FILIAL'] = filial

                lista_df_completa_extrato_stracta.append(df_infomacoes)

                print('Arquivo adicionado na lista -  ' + arquivo)

                os.remove(os.path.join(p.caminho_arquivo_stracta, arquivo))

            else:

                print('\nATENÇÃO O ARQUIVO: ' + arquivo + ' NÃO ESTÁ NO FORMATO XLSX\nFAVOR CONVERTER PARA XLSX')

        df_final = pd.concat(lista_df_completa_extrato_stracta)

        return df_final
