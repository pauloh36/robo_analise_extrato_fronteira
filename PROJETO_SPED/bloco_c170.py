import pandas as pd
import importador_layout
import leitor_arquivo_chaves_acesso_uf_AL
import path_arquivos


class Bloco_c170:

    def __init__(self):
        self.caminho_layout_c170 = 'BLOCO_C170.xlsx'

    def correcao_bloco_c170(self, df_c170_original):

        print('Iniciando correção do bloco C170...')

        b = Bloco_c170()
        importador = importador_layout.Importador_layout()
        leitor_chaves = leitor_arquivo_chaves_acesso_uf_AL.Ler_arquivo_chaves_acesso()
        p = path_arquivos.Path_arquivos()

        # importando o layout

        df_layout_c170 = importador.importa_layout(b.caminho_layout_c170)

        # df com as chaves de acesso

        df_chaves = leitor_chaves.ler_arquivo_chaves_sem_filtro()

        df_chaves = df_chaves.drop(columns='ID_DT_INI')
        df_chaves = df_chaves.drop(columns='ID_DT_FIN')
        df_chaves = df_chaves.drop(columns='ANO')
        df_chaves = df_chaves.drop(columns='MES')
        df_chaves = df_chaves.drop(columns='REF')

        # criando o df para moficação

        df_modificado = pd.DataFrame()

        # df c170 sem erros
        df_c170_notas_sem_erro = b.bloco_c170_sem_erros(df_c170_original)

        # df c170 com erros
        df_c170_notas_com_erro = b.bloco_c170_com_erros(df_c170_original)

        # quebrando a coluna COD PART retornando o segundo desmembramento
        # para obter o cnpj do participante da nf , e preenchendo com 0 a esquerda para
        # termos 14 digitos e pegando as colunas necessarias para realizar o merge ...

        df_modificado['COD_PART'] = df_c170_notas_com_erro['COD_PART']
        df_modificado['CNPJ'] = df_c170_notas_com_erro['COD_PART'].str.split('-', expand=True)[1].str.zfill(14)
        df_modificado['NUM_DOC'] = df_c170_notas_com_erro['NUM_DOC'].astype(str).str.zfill(9)

        # porcorrendo todas as colunas do frame das notas com erros , vamos adicionar as colunas que não existem
        # no frame modificados onde estão com os campos corrigidos

        for c in df_c170_notas_com_erro.columns:

            if c in df_modificado.columns:

                pass

            else:

                df_modificado[c] = df_c170_notas_com_erro[c]


        # pegando as informações corretas das notas que estão com problema , mesclando meu frame das chaves com as notas

        df_modificado = pd.merge(df_modificado, df_chaves, on=['CNPJ', 'NUM_DOC'], how='left')

        df_modificado = df_modificado.drop(columns='CNPJ')

       #df_modificado = pd.merge(df_modificado, df_c170_modificado_notas_com_erro, on=['CNPJ', 'NUM_DOC'], how='left')

        df_final = pd.concat([df_c170_notas_sem_erro, df_modificado], ignore_index=True)

        print('Processo no bloco C170 finalizado\n')

        return df_final

    def bloco_c170_sem_erros(self, df_c170_original):

        print('Procurando campos sem erros...')

        # df original do bloco c170 e alterando a colunma NUM_DOC para o merge

        df_c170_notas_sem_erro = df_c170_original
        df_c170_notas_sem_erro['NUM_DOC'] = df_c170_notas_sem_erro['NUM_DOC'].astype(str).str.zfill(9)
        df_c170_notas_sem_erro = df_c170_original.loc[
            (df_c170_original['COD_MOD'] == 65) | (df_c170_original['COD_MOD'] == 55)]

        print('Foram encontradas '+str(len(df_c170_notas_sem_erro))+' linhas sem erros')

        return df_c170_notas_sem_erro

    def bloco_c170_com_erros(self, df_c170_original):

        # filtro para encontrar as notas com divergencia no df original

        print('\nProcurando campos com erros...')

        df_c170_notas_com_erro = df_c170_original.loc[
            (df_c170_original['COD_MOD'] != 65) & (df_c170_original['COD_MOD'] != 55)]
        df_c170_notas_com_erro['NUM_DOC'] = df_c170_notas_com_erro['NUM_DOC'].astype(str).str.zfill(9)

        df_c170_notas_com_erro = df_c170_notas_com_erro.drop(columns='CHV_NFE')
        df_c170_notas_com_erro = df_c170_notas_com_erro.drop(columns='COD_SIT')
        df_c170_notas_com_erro = df_c170_notas_com_erro.drop(columns='COD_MOD')
        df_c170_notas_com_erro = df_c170_notas_com_erro.drop(columns='SER')

        print('Foram encontradas ' + str(len(df_c170_notas_com_erro)) + ' linhas com erros\n')

        return df_c170_notas_com_erro


