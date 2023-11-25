import pandas as pd
import variaveis_globais


class Grava_arquivo:
    def __init__(self):
        self.write = ''
        self.estado = ''

    def salvar_arquivo(self, df_gravar):
        v = variaveis_globais.Path_arquivos()

        gravar = Grava_arquivo()

        gravar.estado = 'PE'

        gravar.writer = pd.ExcelWriter(v.caminho_nfs_nao_efetivadas + '/' + gravar.estado + '_NFS_NAO_EFETIVADAS' + '.xlsx',
                                       engine='xlsxwriter')

        df_gravar.to_excel(gravar.writer, sheet_name='RESUMO_NFS_NAO_EFETIVADAS')

        gravar.writer.close()

        print('\n Arquivo salvo ! ')
