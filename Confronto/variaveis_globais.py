# caminho das pastas

class Path_arquivos:

    def __init__(self):

        #versão

        self.versao = 'Data da ultima atualização: 12/10/2023'
        self.autor = 'PH :) '

        # bd

        self.caminho_bd = "/content/drive/MyDrive/FILES_PY/PROGRAMA_CONFRONTO_PRODUCAO/bd_confronto.sqlite3"

        # caminho dos arquivos

        self.caminho_arquivo = "C:/Users/paulo/Downloads/camila/ARQUIVOS CONFRONTO"

        self.caminho_save = 'C:/Users/paulo/Downloads/camila/SAVE'

        self.caminho_nfs_nao_efetivadas = 'C:/Users/paulo/Downloads/camila/NOTAS NÃO EFETIVADAS'

        self.caminho_itens_antecipado_pe = 'C:/Users/paulo/Downloads/camila/ARQUIVOS_AUXILIARES_PE/pagamento_antecipado.xlsx'

        self.caminho_correcoes_difal = "C:/Users/paulo/Downloads/camila/ARQUIVOS_AUXILIARES_PE/aliquota_difal.xlsx"

        self.caminho_retido_fornecedor = 'C:/Users/paulo/Downloads/camila/RETIDO_FORNECEDOR/INCRICOES-RETIDO-FORNECEDOR.xlsx'

        self.caminho_notas_pagas_difal_pe = 'C:/Users/paulo/Downloads/camila/ARQUIVOS_AUXILIARES_PE/PE_NFS_DIFAL_PAGAS.xlsx'

        self.contador_processos = 'C:/Users/paulo/Documents/Projetos/Confronto/config/contador_processos.txt'

        self.uf_fornecedores = 'C:/Users/paulo/Downloads/camila/FORNECEDORES.xlsx'

        # cfop

        self.cfop_uso_consumo = [2556, 2551, 2552, 2557, 2949, 2920, 2923, 2911, 2908, 2407]

        self.colunas_confronto = ['Origem nota fiscal',
                             'Filial',
                             'Tributação',
                             'Número do documento',
                             'Data Vencimento Documento',
                             'Número nota',
                             'Item Fatura',
                             'CFOP',
                             'Data emissão Sefaz',
                             'Data emissão Atacadão',
                             'Data efetivação',
                             'Data posto fiscal',
                             'CNPJ',
                             'Razão social',
                             'Mercadoria',
                             'Descrição Mercadoria',
                             'alq_org',
                             'alq_des',
                             'Valor total nota sefaz',
                             'Valor IPI sefaz',
                             'Valor base calculo sefaz',
                             'Valor ICMS substituto sefaz',
                             'Valor ICMS antecipado sefaz',
                             'Valor ICMS diferencial sefaz',
                             'Valor icms sefaz',
                             'Valor total nota atacadão',
                             'Valor IPI atacadão',
                             'Valor base calculo atacadão',
                             'Valor icms atacadao',
                             'Crédito Antecip',
                             'Cred ICMS Retido(layout)',
                             'Valor divergência',
                             'Valor total base de calculo substituto',
                             'Valor total ICMS substituto',
                             'Código Receita',
                             'UF',
                             'Nota Devolução',
                             'Valor Total Nf Dev.',
                             'Valor Base. Calc. subst. Nf Dev.',
                             'Valor total ICMS substituto Nf Dev.',
                             'Cobrado Anteriormente no Documento']

        self.filiais_pb = [74, 89, 114, 146, 199, 279, 829]
        self.filiais_ac = [141, 308]
        self.filiais_am = [118, 119, 149, 188, 281, 286]
        self.filiais_se = [68, 109, 274, 862]
        self.filiais_pe = [47, 50, 55, 56, 87, 150, 152, 187, 228, 240, 243, 244, 264, 280, 293, 312, 316, 323, 328,
                           356, 357, 832, 870]
        self.filiais_ce = [80, 82, 110, 144, 158, 173, 189, 304, 305, 828, 836, 840, 871]
        self.filiais_rr = [179, 248]
        self.filiais_al = [98, 148, 216, 217, 220, 273, 881]
        self.filiais_ro = [72, 186, 201, 213]