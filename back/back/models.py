from sqlalchemy import Column, Integer, String, ForeignKey
# Importa a base declarativa e o recurso de relacionamento entre tabelas
from sqlalchemy.orm import declarative_base , relationship

Base = declarative_base () 

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True)
    nome = Column (String)
    email = Column (String)
    animais= relationship("Animais", back_populates="usuarios")

#animais

class Animais(Base):
    __tablename__ = "animais"
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    nome = Column(String)
    especie = Column(String)

    usuario = relationship("Usuario", back_populates="animais")
    consulta= relationship("Consulta", back_populates="animais")



class Veterinario(Base):
    __tablename__ = "veterinarios"
    id = Column(Integer, primary_key=True)
    nome = Column (String)
    email = Column (String)
    telefone = Column (String)
    consulta= relationship("Consulta", back_populates="veterinarios")

class Consulta(Base):
    __tablename__ = "consultas"
    id = Column(Integer, primary_key=True)
    animal_id = Column(Integer, ForeignKey("animais.id"))
    veterinario_id = Column(Integer, ForeignKey("veterinarios.id"))
    data = Column(String)
    veterinario = relationship("Veterinario", back_populates="consultas")
    animais = relationship("Animais", back_populates="consultas")