import pandas as pd
import path_arquivos


class Gravar:
    def __init__(self):
        self.writer = ''

    def salvar_arquivo(self, df_gravar, filial, n_extrato):
        p = path_arquivos.Path_arquivo()

        gravar = Gravar()

        gravar.writer = pd.ExcelWriter(
            p.caminho_resultado + '/' + '' + str(filial) + 'E_LAYOUT_' + str(n_extrato) + '.xlsx',
            engine='xlsxwriter')

        df_gravar.to_excel(gravar.writer, sheet_name='Plan1', index=False)

        gravar.writer.close()

        print('Arquivo salvo ! \n')
