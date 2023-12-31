import leitor_arquivo_comum
import leitor_arquivo_stracta
import sobre
import Gravar
import utilidades


class Principal:
    s = sobre.Sobre()
    g = Gravar.Gravar()
    u = utilidades.Utilidades()

    print('\n--------------------- Iniciando Script ------------------\n')
    print('Script desenvolvido por : ' + s.autor + '\n')
    print('Data da ultima atualização : ' + s.data_ultima_atualizacao + '\n')

    leitor_stracta = leitor_arquivo_stracta.Leitor_arquivo_stracta()
    leitor_comum = leitor_arquivo_comum.Leitor()

    print('\n-------- Lendo arquivos eStracta --------\n')
    stracta = leitor_stracta.leitor_arquivo()
    print('\n-------- Lendo arquivos Comum --------\n')
    comum = leitor_comum.leitor_arquivo()

    print('\nMesclando as informações...\n')

    df_mesclado_final = u.mesclar_extratos(stracta, comum)

    g.salvar_arquivo(df_mesclado_final, 'ARQUIVO_MESCLADO', 10)

    print('\n--------------------- Processo concluido ------------------')
