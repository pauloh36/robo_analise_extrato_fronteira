import pandas as pd
import os
import path_arquivos
import layout_padrao
import identificador_filial


class Leitor:
    def __init__(self):
        self.lista = []
        self.arquivo_atual = ''
        self.nome_arquivo_filial = ''
        self.filial = ''
        self.registro_nota = ''
        self.cnpj = ''
        self.n_nota = ''
        self.data_passagem = ''
        self.vlr_icms = ''
        self.vlr_base_icms = ''
        self.uf_fornecedor = ''
        self.chave = ''

    def leitor_arquivo(self):
        l = Leitor()
        arquivo = path_arquivos.Path_arquivo()
        layout = layout_padrao.Layout()
        identificador = identificador_filial.Identificador_filial()

        lista_df_completa_extrato_comum = []

        for file in os.listdir(arquivo.caminho_arquivo_comum):
            print('Processando o arquivo: ' + file)

            caminho_arquivo_atual = os.path.join(arquivo.caminho_arquivo_comum, file)

            l.arquivo_atual = pd.read_excel(caminho_arquivo_atual)

            inscricao_arquivo = l.arquivo_atual.iloc[7, 1]

            n_extrato = l.arquivo_atual.iloc[13, 6]

            l.filial = identificador.verifica_filial(inscricao_arquivo)

            qtde_linhas_frame = len(l.arquivo_atual)

            l.arquivo_atual = l.arquivo_atual.iloc[16:(qtde_linhas_frame - 7)]

            df_informacoes_extrato = pd.DataFrame()


            df_informacoes_extrato['ITEM FATURA'] = l.arquivo_atual.iloc[:, 0]
            df_informacoes_extrato['CNPJ'] = l.arquivo_atual.iloc[:, 6]
            df_informacoes_extrato['NUM NOTA'] = l.arquivo_atual.iloc[:, 2].astype(int)
            df_informacoes_extrato['DT POSTO FISCAL'] = l.arquivo_atual.iloc[:, 1]
            df_informacoes_extrato['DT POSTO FISCAL'] = df_informacoes_extrato['DT POSTO FISCAL'].str.replace(' ', '')
            #df_informacoes_extrato['VLR ICMS'] = l.arquivo_atual.iloc[:, 5]
            #df_informacoes_extrato['VLR ICMS ANTEC'] = l.arquivo_atual.iloc[:, 5]
            df_informacoes_extrato['VLR BASE CALCULO'] = l.arquivo_atual.iloc[:, 4]
            df_informacoes_extrato['VLR BASE ANTEC'] = l.arquivo_atual.iloc[:, 4]
            df_informacoes_extrato['VLR TOTAL NOTA'] = l.arquivo_atual.iloc[:, 4]
            df_informacoes_extrato['UF'] = l.arquivo_atual.iloc[:, 3]
            df_informacoes_extrato.loc[:, 'FILIAL'] = l.filial



            lista_df_completa_extrato_comum.append(df_informacoes_extrato)
            print('Arquivo adicionado na lista -  ' + file)

            os.remove(caminho_arquivo_atual)

        df_final = pd.concat(lista_df_completa_extrato_comum)

        return df_final
