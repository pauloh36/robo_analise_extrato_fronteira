import variaveis_globais
import pandas as pd
import ler_arquivo_externo
import utilidades


class Aba_difal:

    def __init__(self):
        pass

    def frame_difal(self, df):
        vg = variaveis_globais.Path_arquivos()

        # --------------------  logica DIFAL  -----------------------

        frameDifal = df.loc[df['CFOP'].isin(vg.cfop_uso_consumo)]

        frameDifal['OBS'] = ''

        frameDifal = frameDifal[
            ['Origem nota fiscal', 'Número nota', 'CFOP', 'CNPJ', 'Razão social', 'Valor icms sefaz', 'Código Receita',
             'OBS']]

        # --------------------  FIM logica DIFAL  -----------------------

        return frameDifal


    # metodo para verificar se as notas do extrato já foram pagas em algum momento , com base na planilha externa extraida do mastersaf
    def frame_nfs_pagas_difal_pe(self):

        # criando um objeto da nossa classe utilidades

        u = utilidades.Utilidades()

        #criando objeto para utilizar o metodo para ler o arquivo em excel

        ler = ler_arquivo_externo.Ler_arquivo()

        # objeto com o caminho do arquivo contendo as notas
        vg = variaveis_globais.Path_arquivos()

        # nosso dataframe com as informações

        df_notas_pagas_difal_pe = ler.ler_arquivo_xls(vg.caminho_notas_pagas_difal_pe)

        # pegando as colunas que vamos utilizar

        df_notas_pagas_difal_pe = df_notas_pagas_difal_pe[['cod_estab', 'cpf_cgc', 'num_docfis']]

        # renomeando as colunas

        df_notas_pagas_difal_pe = df_notas_pagas_difal_pe.rename(columns={'cod_estab': 'FILIAL_MS'})
        df_notas_pagas_difal_pe = df_notas_pagas_difal_pe.rename(columns={'cpf_cgc': 'CNPJ'})
        df_notas_pagas_difal_pe = df_notas_pagas_difal_pe.rename(columns={'num_docfis': 'Número nota'})

        # transformando elas em string ou int

        df_notas_pagas_difal_pe['FILIAL_MS'] = df_notas_pagas_difal_pe['FILIAL_MS'].astype(int)
        df_notas_pagas_difal_pe['CNPJ'] = df_notas_pagas_difal_pe['CNPJ'].astype(str)
        df_notas_pagas_difal_pe['Número nota'] = df_notas_pagas_difal_pe['Número nota'].astype(int)

        # mascara para o campo CNPJ pois na planilha padrao vem apenas os numeros, usando um metodo externo

        df_notas_pagas_difal_pe['CNPJ'] = df_notas_pagas_difal_pe['CNPJ'].apply(u.limpar_cnpj)

        # retorno meu frame para quem o invocou

        return df_notas_pagas_difal_pe
