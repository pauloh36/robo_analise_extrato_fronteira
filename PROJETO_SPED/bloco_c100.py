import pandas as pd
import os
import path_arquivos
import importador_layout
import leitor_arquivo_chaves_acesso_uf_AL


class Bloco_c100:

    def __init__(self) -> None:
        self.nome_arquivo_layou_bloco_c100 = 'BLOCO_C100.xlsx'

    def correcao_bloco_c100(self, cnpj_arquivo, ref_arquivo):
        b = Bloco_c100()

        leitor_chaves = leitor_arquivo_chaves_acesso_uf_AL.Ler_arquivo_chaves_acesso()

        importador = importador_layout.Importador_layout()

        df_layout_solicitado = importador.importa_layout(b.nome_arquivo_layou_bloco_c100)

        print('Realizando correções no bloco C100... aguarde !')

        frame_final_chaves = leitor_chaves.ler_arquivo_chaves_al_c100(ref_arquivo, cnpj_arquivo)

        # filtro por modelo da nota e CNPJ que está no arquivo

        frame_final_chaves = frame_final_chaves[(frame_final_chaves.loc[:, 'COD_MOD'] == '65') & (
                        frame_final_chaves.loc[:, 'CNPJ'] == cnpj_arquivo)]
        
        # filtrando com as ref que foram encontradas no arquivo aba "0000"
        
        frame_final_chaves = frame_final_chaves.loc[frame_final_chaves['REF'].isin(ref_arquivo)]

        # pegando apenas as colunas que vamos utilizar na junção

        frame_final_chaves = frame_final_chaves[['ID_DT_INI', 'ID_DT_FIN','COD_MOD', 'COD_SIT', 'SER', 'NUM_DOC', 'CHV_NFE']]

        # concatenando o frame vazio com o frame preenchido

        df_layout_solicitado = pd.concat([df_layout_solicitado, frame_final_chaves], ignore_index=True)

        # preenchendo o restante das informações

        df_layout_solicitado['ID_CNPJ'] = cnpj_arquivo

        df_layout_solicitado['REG'] = 'C001'
        df_layout_solicitado['IND_MOV'] = '0'
        df_layout_solicitado['REG.1'] = 'C100'
        df_layout_solicitado['IND_OPER'] = '1'

        # preenchendo com hifen as colunas não utilizadas

        df_layout_solicitado['IND_EMIT'] = "0"
        df_layout_solicitado['COD_PART'] = ""
        df_layout_solicitado['VL_DESC'] = "-"
        df_layout_solicitado['VL_ABAT_NT'] = "-"
        df_layout_solicitado['VL_MERC'] = "-"
        df_layout_solicitado['IND_FRT'] = "-"
        df_layout_solicitado['VL_FRT'] = "-"
        df_layout_solicitado['VL_SEG'] = "-"
        df_layout_solicitado['VL_OUT_DA'] = "-"
        df_layout_solicitado['VL_BC_ICMS'] = "-"
        df_layout_solicitado['VL_ICMS'] = "-"
        df_layout_solicitado['VL_BC_ICMS_ST'] = "-"
        df_layout_solicitado['VL_ICMS_ST'] = "-"
        df_layout_solicitado['VL_IPI'] = "-"
        df_layout_solicitado['VL_PIS'] = "-"
        df_layout_solicitado['VL_COFINS'] = "-"
        df_layout_solicitado['VL_PIS_ST'] = "-"
        df_layout_solicitado['VL_COFINS_ST'] = "-"

        df_layout_solicitado['DT_DOC'] = "-"
        df_layout_solicitado['DT_E_S'] = "-"
        df_layout_solicitado['VL_DOC'] = "-"
        df_layout_solicitado['IND_PGTO'] = "-"
        

        print('Processo no bloco C100 finalizado\n')

        return df_layout_solicitado
