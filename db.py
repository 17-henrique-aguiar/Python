import sqlite3

def get_connection():
    return sqlite3.connect("loja.db", check_same_thread=False)

def criar_tabela():
    conn = get_connection()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS carrinho (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            produto TEXT,
            preco REAL
        )    
    ''')
    conn.commit()
    conn.close()

def adicionar_item(produto, preco):
    conn = get_connection()
    c = conn.cursor()
    c.execute("INSERT INTO carrinho (produto, preco) VALUES (?, ?)", (produto, preco))
    conn.commit()
    conn.close()

def listar_carrinho():
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT id, produto, preco FROM carrinho")
    itens = c.fetchall()
    conn.close()
    return itens

def remover_item(item_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute("DELETE FROM carrinho WHERE id = ?", (item_id,))
    conn.commit()
    conn.close()
