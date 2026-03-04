from flask import Flask, request, jsonify
from flask_cors import CORS
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Usuario, Animal, Veterinario#, Consulta

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

#rotas animais
@app.route('/animais', methods=["POST"])
def add_animais():
    s= Session()
    data = request.json
    u = Animal(nome=data["nome"], especie=data["especie"], usuario_id=data["usuario_id"])
    s.add(u)
    s.commit()
    return jsonify({"message": "Animal criado!"})

@app.route("/animais/<int:id>", methods=["PUT"])
def update_animais(id):
    s = Session()
    u = s.query(Animal).get(id)
    data = request.json
    u.nome = data["nome"]
    u.especie = data["especie"]
    s.commit()
    return jsonify({"message": "Animal atualizado!"})



@app.route("/animais/<int:id>", methods=["DELETE"])
def delete_animais(id):
    s = Session()
    u = s.query(Animal).get(id)
    s.delete(u)
    s.commit()
    return jsonify({"message": "Animal deletado!"})



@app.route('/animais', methods=["GET"])
def get_animais():
    s = Session()
    animais = s.query(Animal).all()
    return jsonify([{"id": a.id, "nome": a.nome, "especie": a.especie, "usuario_id": a.usuario_id} for a in animais])

    

#rotas veterinario
#  
@app.route('/veterinario', methods=["GET"])   
def get_Veterinario():
    s = Session()
    veterinario = s.query(Veterinario).all()
    return jsonify([{"id": u.id, "nome": u.nome, "email": u.email, "telefone": u.telefone} for u in veterinario])
  


@app.route("/veterinario/<int:id>", methods=["DELETE"])
def delete_veterinario(id):
    s = Session()
    u = s.query(Veterinario).get(id)
    s.delete(u)
    s.commit()
    return jsonify({"message": "Veterinário deletado!"})

@app.route("/veterinário/<int:id>", methods=["PUT"])
def update_veterinario(id):
    s = Session()
    u = s.query(Veterinario).get(id)
    data = request.json
    u.nome = data["nome"]
    u.email = data["email"]
    u.telefone = data["telefone"]
    s.commit()
    return jsonify({"message": "Veterinário atualizado!"})

@app.route("/veterinario", methods=["POST"])
def add_veterinario():
    s= Session()
    data = request.json
    u = Veterinario(nome=data["nome"], email=data["email"], telefone=data["telefone"])
    s.add(u)
    s.commit()
    return jsonify({"message": "Veterinário criado"})

if __name__ == "__main__":
    app.run(debug=True)