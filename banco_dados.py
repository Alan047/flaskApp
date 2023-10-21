import sqlite3



conn = sqlite3.connect('banco_flask.db')

cur = conn.cursor()

# cur.execute('''CREATE TABLE IF NOT EXISTS posts
#                (nome TEXT, texto TEXT)''')

# conn.commit()
conn.close()

def inserir(nome, texto):
    with sqlite3.connect('banco_flask.db') as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO postagens (nome, texto) VALUES (?, ?)", (nome, texto))
def show_table():
    with sqlite3.connect('banco_flask.db') as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM postagens")
        resultados = cur.fetchall()
        print(resultados)
        return resultados
def deletar(nome):
    with sqlite3.connect('banco_flask.db') as conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM postagens WHERE texto=?", (nome,))
        conn.commit()





