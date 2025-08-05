import sqlite3
import jwt
import datetime

SECRET = "segredo" 

def autenticar(username, senha):
    db = sqlite3.connect('database/industrias_wayne.db')
    cursor = db.cursor()
    cursor.execute('SELECT username, nome, cargo FROM usuarios WHERE username = ? AND senha = ?', (username, senha))
    user = cursor.fetchone()
    db.close()
    if user:
        return {"username": user[0], "nome": user[1], "cargo": user[2]}
    return None

def criar_token(user):
    payload ={
        "username": user["username"],
        "nome": user["nome"],
        "cargo": user["cargo"],
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=4)
    }
    return jwt.encode(payload, SECRET, algorithm="HS256")

def verificar_token(auth_header):
    if not auth_header:
        return None
    try:
        token = auth_header.split(" ")[1]
        payload = jwt.decode(token, SECRET, algorithms=["HS256"])
        return {
            "username": payload["username"],
            "nome": payload["nome"],
            "cargo": payload["cargo"]
        }
    except Exception:
        return None