import instalador_pacotes
import relatorio_asterisco
import conversor_xls
import filtro_estado
import variaveis_globais
import time
import conexao_bd
import utilidades

import pandas as pd

# não informar os avisos

pd.set_option('mode.chained_assignment', None)


class pricipal():
    vg = variaveis_globais.Path_arquivos()
    conversor = conversor_xls.conversor()
    u = utilidades.Utilidades()

    banco = conexao_bd.conexao_bd()

    print('\n------------------------- Script iniciado ! -------------------------')
    print('\nScript desenvolvido por : ' + vg.autor)
    print(vg.versao)
    print('\nHistorico de arquivos gerados \nQtde de arquivos gerados: ' + str(u.ler_contador()))

    # linhas para instalar os pacotes caso necessario

    #instalador = instalador_pacotes.instalador()

    #instalador.metodo_instalador_pacote()

    conversor.conversor_xls()
    print('\nAguardando a atualização da pasta...')

    time.sleep(10)

    # chamando a classe filtro estado e executando o metodo principal dela

    p = filtro_estado.Filtro_estado()

    p.principal()

    # ----------- relatório asterisco PE ----------

    # relatorio = r.concatenar()

    # if relatorio.empty:
    #   pass

    # else:

    #   print('\nGerando relatório de notas não efetivadas')

    #  r.resumo_asterisco(relatorio)

    print(
        '\n\nFAVOR EXCLUIR OS ARQUIVOS DEPOIS DE UTILIZAR !!!\n\nOs arquivos foram gerados no diretório: ' + vg.caminho_arquivo + '\n\n ------------------------- Processo Conluído ! ------------------------- ')
