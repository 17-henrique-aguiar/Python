import sqlite3

# cria banco e a tabela se não existir
def criar_banco():
    conn = sqlite3.connect("chamada.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chamada (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            aluno TEXT NOT NULL,
            dia_semana TEXT NOT NULL,
            presente INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Salvar as presenças no banco
def salvar_presenca(presencas):
    conn = sqlite3.connect("chamada.db")
    cursor = conn.cursor()
    for aluno, dias in presencas.items():
        for dia, presente in dias.items():
            cursor.execute("INSERT INTO chamada (aluno, dia_semana, presente) VALUES (?,?,?)",
                           (aluno, dia, presente))
    conn.commit()
    conn.close()