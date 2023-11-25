import path_arquivos


class Utilidades:

    def __init__(self):
        pass

    def ler_contador(self):

        p = path_arquivos.Path_arquivos()

        try:
            with open(p.caminho_contador, 'r') as arquivo:
                valor = int(arquivo.read())
                return valor
        except FileNotFoundError:
            return 0  # Valor padrão se o arquivo não existir

    # Função para incrementar o contador e salvar o novo valor no arquivo
    def incrementar_contador(self):

        p = path_arquivos.Path_arquivos()

        u = Utilidades()

        valor_atual = u.ler_contador()
        novo_valor = valor_atual + 1

        with open(p.caminho_contador, 'w') as arquivo:
            arquivo.write(str(novo_valor))
