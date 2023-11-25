import os


class Validador:

    def __init__(self):
        pass

    def validador_pasta_vazia(self, caminho_arquivo_atual):

        contador = 0

        for file in os.listdir(caminho_arquivo_atual):
            contador += 1

        if contador == 0:

            print('\nA PASTA: '+caminho_arquivo_atual+' - ESTÁ VAZIA !!! \nVERIFIQUE OS ARQUIVOS OU AGUARDE A PASTA ATUALIZAR\nPROGRAMA ENCERRADO ')

            exit()

        else:

            pass

    # verifica se o arquivo está vazio
    def validador_arquivo_vazio(self, frameOriginal):

        contador = len(frameOriginal)
        tipo_arquivo = ''

        if contador == 0:
            tipo_arquivo = 'vazio'

        return tipo_arquivo
    
    def verifica_existencia_bloco(self, lista_blocos_arquivo, bloco_procurado):

        status_bloco = ''

        if bloco_procurado in lista_blocos_arquivo:

            status_bloco = 'OK'

            pass
            
        else:

            status_bloco = 'NAO_ENCONTRADO'

        return status_bloco

             
