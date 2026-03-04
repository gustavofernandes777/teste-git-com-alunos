from flask import Flask, request, jsonify
from flask_cors import CORS
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Usuario

app = Flask(__name__)
CORS(app)
engine = create_engine("sqlite:///daabase.db")
Base.metadata.create_all(engine)
Session = sessionmaker (bind=engine)

@app.route('/usuarios', methods=["POST"])
def add_usuario():
    s= Session()
    data = request.json
    u = Usuario(nome=data["nome"], email=data["email"])
    s.add(u)
    s.commit()
    return jsonify({"message": "Usuário criado"})


@app.route("/usuarios/<int:id>", methods=["PUT"])
def update_usuario(id):
    s = Session()
    u = s.query(Usuario).get(id)
    data = request.json
    u.nome = data["nome"]
    u.email = data["email"]
    s.commit()
    return jsonify({"message": "Usuário atualizado!"})

@app.route("/usuarios/<int:id>", methods=["DELETE"])
def delete_usuario(id):
    s = Session()
    u = s.query(Usuario).get(id)
    s.delete(u)
    s.commit()
    return jsonify({"message": "Usuário deletado!"})



@app.route('/usuarios', methods=["GET"])
def get_usuarios():
    s = Session()
    usuarios = s.query(Usuario).all()
    return jsonify([{"id": u.id, "nome": u.nome, "email": u.email} for u in usuarios])

if __name__ == "__main__":
    app.run(debug=True)
    