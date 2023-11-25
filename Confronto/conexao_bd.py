import sqlite3
import variaveis_globais


class conexao_bd:

    def __init__(self):
        pass

    def insert_frame_sefaz_banco(self, df):
        vg = variaveis_globais.Path_arquivos()

        conn = sqlite3.connect(vg.caminho_bd)
        cursor = conn.cursor()

        df['Número do documento'].fillna('-')

        df = df.iloc[(df['Número do documento'] != '-')]

        df.to_sql('Confronto', conn, if_exists='append', index=False)

        conn.commit()

        # cursor.execute('CREATE TABLE "Confronto" ("ID"	INTEGER,"NF"	REAL,"ORIGEM_NF"	TEXT,"FILIAL"	REAL,"CFOP"	REAL,"CNPJ"	REAL,"FORNECEDOR"	TEXT,"VALOR_ICMS_SEFAZ"	REAL,"VALOR_ICMS_ATACADAO"	REAL,"ITEM_FATURA"	TEXT,"BASE_SEFAZ"	REAL,"JUSTIFICATIVA"	TEXT,PRIMARY KEY("ID" AUTOINCREMENT));')

        conn.close()

    def remover_notas_vazias(self):
        vg = variaveis_globais.Path_arquivos()

        conn = sqlite3.connect(vg.caminho_bd)

        cursor = conn.cursor()

        cursor.execute('DELETE FROM Confronto WHERE NF IS NULL')

        conn.commit()
        conn.close()

    def remover_nf_duplicadas(self):
        vg = variaveis_globais.Path_arquivos()

        conn = sqlite3.connect(vg.caminho_bd)

        cursor = conn.cursor()

        cursor.execute(
            'CREATE TEMPORARY TABLE NOTAS_A_MANTER AS SELECT MIN(ID) AS NOTA_A_MANTER FROM Confronto GROUP BY NF;')

        cursor.execute('DELETE FROM Confronto WHERE ID NOT IN (SELECT NOTA_A_MANTER FROM NOTAS_A_MANTER);')

        conn.commit()
        conn.close()
