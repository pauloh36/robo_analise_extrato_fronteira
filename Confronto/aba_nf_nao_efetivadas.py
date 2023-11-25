import pandas as pd

class Aba_nf_nao_efetivadas:
 
    def __init__(self):
        pass

    def aba_asterisco(self, df, uf_arquivo):
       
        if uf_arquivo == 'AC':

            frameAsterisco = df[
            (df['Origem nota fiscal'] == '**********') & (df['Valor icms sefaz'] > 0.0)]

            soma_asterisco = frameAsterisco['Valor icms sefaz'].sum()

            frameAsterisco.loc[frameAsterisco.index.max() + 1, 'Valor icms sefaz'] = soma_asterisco

            frameAsterisco['Justificativa'] = ''

            frameAsterisco = frameAsterisco[
            ['Origem nota fiscal', 'Filial', 'Número nota', 'CNPJ', 'Razão social', 'Valor icms sefaz',
            'Código Receita', 'Justificativa']]

            return frameAsterisco



        elif uf_arquivo == 'AM':

            frameAsterisco = df[
            (df['Origem nota fiscal'] == '**********') & (df['Código Receita'] != 1316.0) & (
            df['Código Receita'] != 1342.0) & (df['Valor icms sefaz'] > 0.0)]

            soma_asterisco = frameAsterisco['Valor icms sefaz'].sum()

            frameAsterisco.loc[frameAsterisco.index.max() + 1, 'Valor icms sefaz'] = soma_asterisco

            frameAsterisco['Justificativa'] = ''

            frameAsterisco = frameAsterisco[
            ['Origem nota fiscal', 'Filial', 'Número nota', 'CNPJ', 'Razão social', 'Valor icms sefaz',
            'Código Receita', 'Justificativa']]

            return frameAsterisco
        

        elif uf_arquivo == 'AL':

            frameAsterisco = df[(df['Origem nota fiscal'] == '**********') & (df['Valor icms sefaz'] > 0.0)]

            soma_asterisco = frameAsterisco['Valor icms sefaz'].sum()

            frameAsterisco.loc[frameAsterisco.index.max() + 1, 'Valor icms sefaz'] = soma_asterisco

            frameAsterisco['Justificativa'] = ''

            frameAsterisco = frameAsterisco[
            ['Origem nota fiscal', 'Filial', 'Número nota', 'CNPJ', 'Razão social', 'Valor icms sefaz',
            'Código Receita', 'Justificativa']]

            return frameAsterisco
        

        elif uf_arquivo == 'CE':

            frameAsterisco = df[
            (df['Origem nota fiscal'] == '**********') & (df['Valor icms sefaz'] > 0.0)]

            frameAsterisco = frameAsterisco.loc[
            (frameAsterisco['Código Receita'] == 1031.0) | (frameAsterisco['Código Receita'] == 2020.0)]

            soma_asterisco = frameAsterisco['Valor icms sefaz'].sum()

            frameAsterisco.loc[frameAsterisco.index.max() + 1, 'Valor icms sefaz'] = soma_asterisco

            frameAsterisco['Justificativa'] = ''

            frameAsterisco = frameAsterisco[
            ['Origem nota fiscal', 'Filial', 'Número nota', 'CNPJ', 'Razão social', 'Valor icms sefaz',
            'Código Receita', 'Justificativa']]

            return frameAsterisco
        
        elif uf_arquivo == 'PB':

            frameAsterisco = df[
            (df['Origem nota fiscal'] == '**********') & (df['Código Receita'] != 1154.0) & (
            df['Valor icms sefaz'] > 0.0)]

            soma_asterisco = frameAsterisco['Valor icms sefaz'].sum()

            frameAsterisco.loc[frameAsterisco.index.max() + 1, 'Valor icms sefaz'] = soma_asterisco

            frameAsterisco['Justificativa'] = ''

            frameAsterisco = frameAsterisco[
            ['Origem nota fiscal', 'Filial', 'Número nota', 'CNPJ', 'Razão social', 'Valor icms sefaz',
            'Código Receita', 'Justificativa']]

            return frameAsterisco
        
        elif uf_arquivo == 'PE':

            frameAsterisco = df[
            (df['Origem nota fiscal'] == '**********') & (df['Número do documento'] != '-') & (
            df['Valor icms sefaz'] > 0.0)]

            soma_asterisco = frameAsterisco['Valor icms sefaz'].sum()

            # contando a quantidade de linhas do frame e acrecentando + 1
            # inserindo o valor total da coluna 'Valor icms sefaz'

            # frameAsterisco.loc[qtde_linhas,'Valor icms sefaz'] = soma_asterisco

            qtde_linhas = len(frameAsterisco) + 1

            frameAsterisco.loc[frameAsterisco.index.max() + 1, 'Valor icms sefaz'] = soma_asterisco

            frameAsterisco['Justificativa'] = ''

            frameAsterisco = frameAsterisco[
            ['Origem nota fiscal', 'Filial', 'Item Fatura', 'Número nota', 'CNPJ', 'Razão social',
            'Valor base calculo sefaz', 'Valor icms sefaz', 'Justificativa']]

            return frameAsterisco
        
        elif uf_arquivo == 'RO':

            frameAsterisco = df[
            (df['Origem nota fiscal'] == '**********') & (df['Valor icms sefaz'] > 0.0)]

            soma_asterisco = frameAsterisco['Valor icms sefaz'].sum()

            frameAsterisco.loc[frameAsterisco.index.max() + 1, 'Valor icms sefaz'] = soma_asterisco

            frameAsterisco['Justificativa'] = ''

            frameAsterisco = frameAsterisco[
            ['Origem nota fiscal', 'Filial', 'Número nota', 'CNPJ', 'Razão social', 'Valor icms sefaz',
            'Código Receita', 'Justificativa']]


            return frameAsterisco
        

        elif uf_arquivo == 'RR':

            frameAsterisco = df.loc[
            (df['Origem nota fiscal'] == '**********') & (df['Valor icms sefaz'] != 0.0)]

            frameAsterisco.loc[:, 'Justificativa'] = ''

            soma_total_asteriso = frameAsterisco.loc[:, 'Valor icms sefaz'].sum()

            # pegando o total de linhas do frame e acrecentando + 1

            total_linhas_asteriso = len(frameAsterisco) + 1

            # escrever no final do total asterisco

            frameAsterisco.loc[total_linhas_asteriso, 'Valor icms sefaz'] = soma_total_asteriso

            # colunas utilizadas

            frameAsterisco = frameAsterisco.loc[:,
            ['Origem nota fiscal', 'Filial', 'Item Fatura', 'Número nota', 'CNPJ', 'Razão social',
            'Valor base calculo sefaz', 'Valor icms sefaz', 'Código Receita', 'Justificativa']]



            return frameAsterisco
        

        elif uf_arquivo == 'SE':

            frameAsterisco = df[
            (df['Origem nota fiscal'] == '**********') & (df['Código Receita'] != 712.0) & (
            df['Valor icms sefaz'] > 0.0)]

            soma_asterisco = frameAsterisco['Valor icms sefaz'].sum()

            frameAsterisco.loc[frameAsterisco.index.max() + 1, 'Valor icms sefaz'] = soma_asterisco

            frameAsterisco['Justificativa'] = ''

            frameAsterisco = frameAsterisco[
            ['Origem nota fiscal', 'Filial', 'Número nota', 'CNPJ', 'Razão social', 'Valor icms sefaz',
            'Código Receita', 'Justificativa']]

            return frameAsterisco
        


        

        
        


