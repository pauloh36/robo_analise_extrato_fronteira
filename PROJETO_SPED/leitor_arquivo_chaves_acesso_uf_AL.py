import path_arquivos
import encontra_chaves_acesso
import gravar

class Ler_arquivo_chaves_acesso:

    def __init__(self):
        pass

    def ler_arquivo_chaves_al_c100(self, ref_arquivo, cnpj_arquivo):
        p = path_arquivos.Path_arquivos()
        e = encontra_chaves_acesso.Encontra_chaves_acesso()
        g = gravar.Gravar()

        # metodo para retornar as chaves do arquivos , necessario informar a pasta dos arquivos

        df_chaves = e.localiza_chaves_al(p.caminho_chaves)

        # essa coluna vai ser sempre 02 , foi o que o thomas falou

        df_chaves['COD_SIT'] = '02'

        # pegando o ano  a apartir da chave de acesso

        df_chaves['ANO'] = df_chaves.iloc[:, 0].str[2:4]

        # pegando o ano  a apartir da chave de acesso

        df_chaves['MES'] = df_chaves.iloc[:, 0].str[4:6]

        df_chaves['REF'] = (df_chaves['MES'].astype(str).str.zfill(2) + '/' + df_chaves['ANO'].astype(str))

        df_chaves['ID_DT_INI'] = '01/'+df_chaves['REF']
        df_chaves['ID_DT_FIN'] = '30/'+df_chaves['REF']

        # pegando o cnpj a apartir da chave de acesso

        df_chaves['CNPJ'] = df_chaves.iloc[:, 0].str[6:20]

        # pegando o n° da nf a apartir da chave de acesso

        df_chaves['NUM_DOC'] = df_chaves.iloc[:, 0].str[25:34]

        # pegando o modelo da nf a apartir da chave de acesso

        df_chaves['COD_MOD'] = df_chaves.iloc[:, 0].str[20:22]

        # pegando a serie da nf a apartir da chave de acesso

        df_chaves['SER'] = df_chaves.iloc[:, 0].str[22:25]

        # removendo as chaves duplicadas

        frame_final_chaves = df_chaves.drop_duplicates(subset=['CHV_NFE'], keep='first')

        qtde_linhas_frame_final = len(frame_final_chaves.loc[(frame_final_chaves['CNPJ'] == cnpj_arquivo)])

        print('\nTotal de chaves encontradas nos arquivos para o cnpj: '+str(cnpj_arquivo)+' Qtde: '+str(qtde_linhas_frame_final))

        # retornando o frame final

        g.gravar_df(frame_final_chaves)

        return frame_final_chaves

    def ler_arquivo_chaves_sem_filtro(self):
        p = path_arquivos.Path_arquivos()
        e = encontra_chaves_acesso.Encontra_chaves_acesso()
        g = gravar.Gravar()

        # metodo para retornar as chaves do arquivos , necessario informar a pasta dos arquivos

        df_chaves = e.localiza_chaves_al(p.caminho_chaves)

        # essa coluna vai ser sempre 02 , foi o que o thomas falou

        df_chaves['COD_SIT'] = '02'

        # pegando o ano  a apartir da chave de acesso

        df_chaves['ANO'] = df_chaves.iloc[:, 0].str[2:4]

        # pegando o ano  a apartir da chave de acesso

        df_chaves['MES'] = df_chaves.iloc[:, 0].str[4:6]

        df_chaves['REF'] = (df_chaves['MES'].astype(str).str.zfill(2) + '/' + df_chaves['ANO'].astype(str))

        df_chaves['ID_DT_INI'] = '01/'+df_chaves['REF']
        df_chaves['ID_DT_FIN'] = '30/'+df_chaves['REF']

        # pegando o cnpj a apartir da chave de acesso

        df_chaves['CNPJ'] = df_chaves.iloc[:, 0].str[6:20]

        # pegando o n° da nf a apartir da chave de acesso

        df_chaves['NUM_DOC'] = df_chaves.iloc[:, 0].str[25:34]

        # pegando o modelo da nf a apartir da chave de acesso

        df_chaves['COD_MOD'] = df_chaves.iloc[:, 0].str[20:22]

        # pegando a serie da nf a apartir da chave de acesso

        df_chaves['SER'] = df_chaves.iloc[:, 0].str[22:25]

        # removendo as chaves duplicadas

        frame_final_chaves = df_chaves.drop_duplicates(subset=['CHV_NFE'], keep='first')

        qtde_linhas_frame_final = len(frame_final_chaves)

        print('\nTotal de chaves encontradas nos arquivo')

        # retornando o frame final

        g.gravar_df(frame_final_chaves)

        return frame_final_chaves
