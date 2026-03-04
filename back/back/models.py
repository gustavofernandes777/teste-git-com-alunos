from sqlalchemy import Column, Integer, String, ForeignKey
# Importa a base declarativa e o recurso de relacionamento entre tabelas
from sqlalchemy.orm import declarative_base , relationship

Base = declarative_base () 

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True)
    nome = Column (String)
    email = Column (String)
    animais= relationship("Animais", back_populates="usuario")

#animais

class Animais(Base):
    __tablename__ = "animais"
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    nome = Column(String)
    especie = Column(String)

    usuario = relationship("Usuario", back_populates="animais")



class Veterinário(Base):
    __tablename__ = "Veterinários"
    id = Column(Integer, primary_key=True)
    nome = Column (String)
    email = Column (String)
    telefone = Column (String)

    