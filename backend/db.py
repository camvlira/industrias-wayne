import sqlite3
def init_db():
    db = sqlite3.connect('database/industrias_wayne.db')
    cursor = db.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS recursos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            tipo TEXT NOT NULL,
            descricao TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            senha TEXT NOT NULL,
            nome TEXT NOT NULL,
            cargo TEXT NOT NULL
        )
    ''')

    usuarios_padrao= [
        ('bruce', 'batman', 'Bruce Wayne', 'admin'),
        ('alfred', 'alfred123', 'Alfred Pennyworth', 'gerente'),
        ('lucius', 'lucius123', 'Lucius Fox', 'funcionario'),
        ('barbara', 'barbara123', 'Barbara Gordon', 'funcionario')
    ]

    for u in usuarios_padrao:
        cursor.execute('''
            INSERT OR IGNORE INTO usuarios (username, senha, nome, cargo)
            VALUES (?, ?, ?, ?)
        ''', u)

    db.commit()
    db.close()

def get_db():
    conn= sqlite3.connect('database/industrias_wayne.db')
    conn.row_factory= sqlite3.Row
    return conn