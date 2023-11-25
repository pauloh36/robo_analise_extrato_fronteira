import pandas as pd


class Aba_save:

    def __init__(self):
        pass

    def cria_aba_save(self, df_original):
        df_ipi_mercadoria_atc = df_original.loc[
            (df_original['Valor IPI atacadão']) > 0, ['Número nota', 'Mercadoria', 'Valor IPI atacadão']]

        df_itens_mercadoria_fam9 = df_original

        df_itens_mercadoria_fam9 = df_itens_mercadoria_fam9[
            ['Origem nota fiscal', 'Tributação', 'Número nota', 'CFOP', 'CNPJ', 'Razão social', 'Mercadoria',
             'Descrição Mercadoria', 'Valor icms atacadao']]

        # filtro apenas itens com código de tributação

        df_itens_mercadoria_fam9 = df_itens_mercadoria_fam9[
            (df_itens_mercadoria_fam9['Tributação'] == 702) | (df_itens_mercadoria_fam9['Tributação'] == 703) | (
                    df_itens_mercadoria_fam9['Tributação'] == 710) | (
                    df_itens_mercadoria_fam9['Tributação'] == 715)]

        #  removo a fam9 e converto para int

        df_itens_mercadoria_fam9["Número nota"] = df_itens_mercadoria_fam9["Número nota"].astype(str).str.slice(0, -1)
        df_itens_mercadoria_fam9["Número nota"] = df_itens_mercadoria_fam9["Número nota"].astype(int)

        # filtro para remover as notas que não retornaram valores

        df_itens_mercadoria_fam9 = df_itens_mercadoria_fam9[(df_itens_mercadoria_fam9['Valor icms atacadao'] > 0)]

        # colocando as ordem das colunas

        resultado = pd.merge(df_itens_mercadoria_fam9, df_ipi_mercadoria_atc, on=['Número nota', 'Mercadoria'],
                             how='left')

        resultado['Valor IPI atacadão'] = resultado['Valor IPI atacadão'].fillna(0)

        return resultado
