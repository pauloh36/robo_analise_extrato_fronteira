import os
import estado_pe
import estado_ac
import estado_pb
import estado_se
import estado_rr
import estado_am
import estado_al
import estado_ce
import estado_ro
import variaveis_globais
import validador
import arquivo_save
import utilidades
import ler_arquivo_externo


class Filtro_estado:

    # construtor

    def __init__(self):
        pass

    def principal(self):

        f = Filtro_estado()
        a = arquivo_save.Arquivo_save()
        vg = variaveis_globais.Path_arquivos()
        v = validador.Validador()
        u = utilidades.Utilidades()
        ler = ler_arquivo_externo.Ler_arquivo()

        ac = estado_ac.Estado_ac()
        al = estado_al.Estado_al()
        pb = estado_pb.Estado_pb()
        ce = estado_ce.Estado_ce()
        ro = estado_ro.Estado_ro()
        se = estado_se.Estado_se()
        am = estado_am.Estado_am()
        rr = estado_rr.Estado_rr()
        pe = estado_pe.Estado_pe()

        v.validador_pasta_vazia(vg.caminho_arquivo)

        for file in os.listdir(vg.caminho_arquivo):

            path_arquivo_xlsx = os.path.join(vg.caminho_arquivo, file)

            frameOriginal = ler.ler_arquivo_xls(path_arquivo_xlsx)

            filial_arquivo = u.localiza_filial(frameOriginal)

            uf_arquivo = u.localiza_estado_arquivo(filial_arquivo)

            # validando o arquivo atual

            print('\nValidando arquivo...')

            v.validador_arquivos_necessarios()

            if v.validador_arquivo_vazio(frameOriginal) == 'vazio':

                print('ATENÇÃO ARQUIVO VAZIO : ' + file + '\n')

                # renomeando o arquivo que foi encontrado vazio

                os.rename(path_arquivo_xlsx, vg.caminho_arquivo + '/' + '[ARQUIVO-VAZIO]-' + file)

            elif v.validador_asterisco(frameOriginal) == 'ERRO':

                print('ATENÇÃO O ARQUIVO POSSUI APENAS ASTERISCO\nESSE ARQUIVO NÃO SERÁ PROCESSADO : ' + file + '\n')

                # renomeando o arquivo que foi encontrado vazio

                os.rename(path_arquivo_xlsx, vg.caminho_arquivo + '/' + '[APENAS-ASTERISCO]-' + file)

            elif uf_arquivo is None:

                print('\nFILIAL: '+str(filial_arquivo)+' -  NÃO ENCONTRADA VERIFIQUE O ARQUIVO OU OS PARAMETROS DE CONFIGURAÇÃO')

                os.rename(path_arquivo_xlsx, vg.caminho_arquivo + '/' + '[FILIAL-INVALIDA]-' + file)

            elif v.validor_colunas(frameOriginal) != 41:

                print('\nARQUIVO INVALIDO: ' + file + '\nVERIFIQUE SE TODAS COLUNAS ESTÃO PRESENTES\n')

                os.rename(path_arquivo_xlsx, vg.caminho_arquivo + '/' + '[ERRO-COLUNAS]-' + file)

            #elif v.valida_cods_receita(frameOriginal, uf_arquivo) != 'OK':

             #   print('\nERRO NA VALIDAÇÃO DOS CODS DE RECEITA NO ARQUIVO: ' + file)

              #  os.rename(path_arquivo_xlsx, vg.caminho_arquivo + '/' + '[ERRO-COD-RECEITA]-' + file)

            else:

                if uf_arquivo == 'PE':
                    print("Filial " + uf_arquivo + ": " + str(filial_arquivo) + " encontrada")

                    df_save = a.leitor_arquivo_save(uf_arquivo, filial_arquivo)

                    pe.logica_pe(file, filial_arquivo, vg.caminho_arquivo, vg.caminho_nfs_nao_efetivadas,
                                 vg.caminho_itens_antecipado_pe, vg.caminho_correcoes_difal, df_save)

                    os.remove(path_arquivo_xlsx)

                if uf_arquivo == 'AC':
                    print("Filial " + uf_arquivo + ": " + str(filial_arquivo) + " encontrada")

                    df_save = a.leitor_arquivo_save(uf_arquivo, filial_arquivo)

                    ac.logica_ac(file, vg.caminho_arquivo, vg.caminho_nfs_nao_efetivadas, filial_arquivo, df_save)

                    os.remove(path_arquivo_xlsx)

                if uf_arquivo == 'PB':
                    print("Filial " + uf_arquivo + ": " + str(filial_arquivo) + " encontrada")

                    df_save = a.leitor_arquivo_save(uf_arquivo, filial_arquivo)

                    pb.logica_pb(file, vg.caminho_arquivo, vg.caminho_nfs_nao_efetivadas, filial_arquivo, df_save)

                    os.remove(path_arquivo_xlsx)

                if uf_arquivo == 'SE':
                    print("Filial " + uf_arquivo + ": " + str(filial_arquivo) + " encontrada")

                    df_save = a.leitor_arquivo_save(uf_arquivo, filial_arquivo)

                    se.logica_se(file, vg.caminho_arquivo, vg.caminho_nfs_nao_efetivadas, filial_arquivo, df_save)

                    os.remove(path_arquivo_xlsx)

                if uf_arquivo == 'RR':
                    print("Filial " + uf_arquivo + ": " + str(filial_arquivo) + " encontrada")

                    df_save = a.leitor_arquivo_save(uf_arquivo, filial_arquivo)

                    rr.logica_rr(file, vg.caminho_arquivo, vg.caminho_nfs_nao_efetivadas, filial_arquivo, df_save)

                    os.remove(path_arquivo_xlsx)

                if uf_arquivo == 'AM':
                    print("Filial " + uf_arquivo + ": " + str(filial_arquivo) + " encontrada")

                    df_save = a.leitor_arquivo_save(uf_arquivo, filial_arquivo)

                    am.logica_am(file, vg.caminho_arquivo, vg.caminho_nfs_nao_efetivadas, filial_arquivo, df_save)

                    os.remove(path_arquivo_xlsx)

                if uf_arquivo == 'AL':
                    print("Filial " + uf_arquivo + ": " + str(filial_arquivo) + " encontrada")

                    df_save = a.leitor_arquivo_save(uf_arquivo, filial_arquivo)

                    al.logica_al(file, vg.caminho_arquivo, vg.caminho_nfs_nao_efetivadas, filial_arquivo, df_save)

                    os.remove(path_arquivo_xlsx)

                if uf_arquivo == 'CE':
                    print("Filial " + uf_arquivo + ": " + str(filial_arquivo) + " encontrada")

                    df_save = a.leitor_arquivo_save(uf_arquivo, filial_arquivo)

                    ce.logica_ce(file, vg.caminho_arquivo, vg.caminho_nfs_nao_efetivadas, filial_arquivo, df_save)

                    os.remove(path_arquivo_xlsx)

                if uf_arquivo == 'RO':
                    print("Filial " + uf_arquivo + ": " + str(filial_arquivo) + " encontrada")

                    df_save = a.leitor_arquivo_save(uf_arquivo, filial_arquivo)

                    ro.logica_ro(file, vg.caminho_arquivo, vg.caminho_nfs_nao_efetivadas, filial_arquivo, df_save)

                    os.remove(path_arquivo_xlsx)

                # contador de processos
                u.incrementar_contador()
