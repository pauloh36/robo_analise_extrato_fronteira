import pandas as pd
import path_arquivos
import Gravar


class Layout:

    def __init__(self):
        pass

    def alimentar_layout(self, filial, registro_nota, cnpj, n_nota, data_passagem, vlr_icms, vlr_base_icms,
                         uf_fornecedor, n_extrato):
        g = Gravar.Gravar()

        path = path_arquivos.Path_arquivo()

        layout_padrao = pd.read_excel(path.caminho_layout)

        # preenchendo a filial nas linhas da coluna FILIAL

        layout_padrao['ITEM FATURA'] = registro_nota
        layout_padrao['CNPJ'] = cnpj
        layout_padrao['NUM NOTA'] = n_nota
        layout_padrao['DT POSTO FISCAL'] = data_passagem.str.replace('-', '')
        layout_padrao['DT POSTO FISCAL'] = layout_padrao['DT POSTO FISCAL'].str.replace(' ', '')
        layout_padrao['VLR ICMS'] = vlr_icms
        layout_padrao['VLR ICMS ANTEC'] = vlr_icms
        layout_padrao['VLR BASE CALCULO'] = vlr_base_icms
        layout_padrao['VLR BASE ANTEC'] = vlr_base_icms
        layout_padrao['VLR TOTAL NOTA'] = vlr_base_icms
        layout_padrao['UF'] = uf_fornecedor
        layout_padrao['ITEM FATURA'] = registro_nota

        layout_padrao.loc[:, 'FILIAL'] = filial

        g.salvar_arquivo(layout_padrao, filial, n_extrato)

    def alimentar_layout_stacta(self, filial, n_extrato, df):
        g = Gravar.Gravar()

        path = path_arquivos.Path_arquivo()

        layout_padrao = pd.read_excel(path.caminho_layout)

        layout_padrao['ITEM FATURA'] = df.iloc[:, 0]
        layout_padrao['CNPJ'] = df.iloc[:, 4]
        layout_padrao['NUM NOTA'] = df.iloc[:, 5]
        layout_padrao['DT POSTO FISCAL'] = ''
        layout_padrao['DT POSTO FISCAL'] = ''
        layout_padrao['VLR ICMS'] = df.iloc[:, 6]
        layout_padrao['VLR ICMS ANTEC'] = df.iloc[:, 6]
        layout_padrao['VLR BASE CALCULO'] = df.iloc[:, 6]
        layout_padrao['VLR BASE ANTEC'] = df.iloc[:, 6]
        layout_padrao['VLR TOTAL NOTA'] = df.iloc[:, 6]
        layout_padrao['UF'] = df.iloc[:, 3]
        layout_padrao['COD_RECEITA'] = df.iloc[:, 7]

        layout_padrao.loc[:, 'FILIAL'] = filial

        g.salvar_arquivo(layout_padrao, filial, n_extrato)
