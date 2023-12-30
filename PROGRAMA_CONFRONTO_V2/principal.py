import leitor_arquivo
import pandas as pd
import sobre

pd.set_option('mode.chained_assignment', None)


class Principal:
    l = leitor_arquivo.Leitor_Arquivo()
    s = sobre.Sobre()

    print('\n*************************************')
    print(
        '\nScript desenvolvido por: ' + s.autor + '\n' + s.mensagem + '\nVersão: ' + s.versao + '\nData da ultima atualização: ' + s.data_ultima_atualizacao + '\n' + s.sugestao)
    print('\n*************************************')

    print('\n---------------- Iniciando Script ----------------\n')

    l.leitor_arquivo()

    print('\n---------------- Processo finalizado  ----------------')

    print('\nLEMBRE-SE DE APAGAR OS ARQUIVOS APÓS UTILIZAR O SISTEMA')
