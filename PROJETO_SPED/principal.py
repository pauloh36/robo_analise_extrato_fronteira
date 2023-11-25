import ler_arquivos_sped
import sobre
import pandas as pd
import utilidades
import warnings
import validador
import path_arquivos

# ignorando os avisos ou alertas
pd.set_option('mode.chained_assignment', None)
warnings.filterwarnings("ignore", category=UserWarning)


class Principal:
    ler = ler_arquivos_sped.Ler_arquivo_sped()
    s = sobre.Sobre()
    u = utilidades.Utilidades()
    v = validador.Validador()
    p = path_arquivos.Path_arquivos()

    print('\nScript desenvolvido por: ' + s.autor)
    print('Data da ultima atualização: ' + s.data_ultima_atualizacao + '\n')
    print('Historico qtde de arquivos processados : ' + str(u.ler_contador()) + '\n')

    print('Realizando validação das pastas...\n')

    # verificando se as pastas estão vazias
    v.validador_pasta_vazia(p.caminho_arquivo)
    v.validador_pasta_vazia(p.caminho_chaves)
    v.validador_pasta_vazia(p.caminho_layout)

    ler.ler_arquivo()

    print('\n\n--------------- PROCESSO CONCLUIDO ------------------------')
