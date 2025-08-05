from flask import Flask, request, jsonify
from flask_cors import CORS
from db import init_db, get_db
from models import autenticar, criar_token, verificar_token

app = Flask(__name__)
CORS(app)
init_db()

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    user = autenticar(data["username"], data["password"])
    if user:
        token = criar_token(user)
        return jsonify({"token": token, "nome": user["nome"], "cargo": user["cargo"]})
    return jsonify({"error": "Credenciais inválidas"}), 401

@app.route("/recursos", methods=["GET", "POST"])
def recursos():
    user = verificar_token(request.headers.get("Authorization"))
    if not user:
        return jsonify({"error": "Não autorizado"}), 403
    db = get_db()
    if request.method == "POST":
        if user["cargo"] != "admin":
            return jsonify({"error": "Permissão negada"}), 403
        data = request.json
        db.execute("INSERT INTO recursos (nome, tipo, descricao) VALUES (?, ?, ?)",
                   (data["nome"], data["tipo"], data["descricao"]))
        db.commit()
        return jsonify({"msg": "Criado com sucesso"})
    recursos = db.execute("SELECT * FROM recursos").fetchall()
    return jsonify([dict(r) for r in recursos])

@app.route("/recursos/<int:id>", methods=["DELETE"])
def remover_recurso(id):
    user = verificar_token(request.headers.get("Authorization"))
    if not user:
        return jsonify({"error": "Não autorizado"}), 403
    if user["cargo"] != "admin":
        return jsonify({"error": "Permissão negada"}), 403

    db = get_db()
    db.execute("DELETE FROM recursos WHERE id = ?", (id,))
    db.commit()
    return jsonify({"msg": "Recurso removido"})

if __name__ == "__main__":
    app.run(debug=True)