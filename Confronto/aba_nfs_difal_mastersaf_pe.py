import pandas as pd
import variaveis_globais
import utilidades

class Aba_nfs_difal_mastersaf:

    def __init__(self):

        pass

    def aba_nfs_difal_mastersaf(self, filial_arquivo):

        vg = variaveis_globais.Path_arquivos()
        u = utilidades.Utilidades()

        # lendo o arquivo

        df = pd.read_excel(vg.caminho_notas_pagas_difal_pe)

        # colunas que vamos utilizar

        df = df.loc[:, ['cod_estab', 'data_fiscal', 'cpf_cgc', 'num_docfis', 'cod_cfo', 'dif_aliq_trib_icms', 'vlr_contab']]

        df['cod_estab'] = df['cod_estab'].astype(str).apply(u.limpar_e_converter_dados_para_int)
        df['cod_cfo'] = df['cod_cfo'].astype(str).apply(u.limpar_e_converter_dados_para_int)
        df['vlr_contab'] = df['vlr_contab'].astype(str).apply(u.limpar_e_converter_dados_para_float)
        df['num_docfis'] = df['num_docfis'].astype(str).apply(u.limpar_e_converter_dados_para_int)
        df['cpf_cgc'] = df['cpf_cgc'].astype(str).apply(u.limpar_cnpj)

        # filtro

        df = df.loc[df['cod_estab'] == filial_arquivo]

        # renomeando algumas colunas

        df = df.rename(columns={'cod_estab': 'FILIAL_MS'})
        df = df.rename(columns={'cpf_cgc': 'CNPJ'})

        # formatando alguns dados


        return df

