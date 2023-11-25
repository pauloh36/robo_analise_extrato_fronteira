import pyexcel as p
import os
import variaveis_globais


class conversor:

    def __init__(self):

        pass

    def conversor_xls(self):

        vg = variaveis_globais.Path_arquivos()

        print('\nIniciando conversão de XLS par XLSX')

        for file in os.listdir(vg.caminho_arquivo):

            if file.endswith('.xls'):

                print("convertendo arquivo: " + file)

                p.save_book_as(file_name=os.path.join(vg.caminho_arquivo, file),
                               dest_file_name=os.path.join(vg.caminho_arquivo, file + ".xlsx"))

                path_arquivo_xls = os.path.join(vg.caminho_arquivo, file)
                path_arquivo_xlsx = os.path.join(vg.caminho_arquivo, file)

                os.remove(path_arquivo_xls)

                print("conversão concluida !")

            else:

                print("Arquivo: " + file + " não está no formato xls... passando para o proximo arquivo")

        print('Processo de conversão concluido')


