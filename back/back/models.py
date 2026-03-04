from sqlalchemy import Column, Integer, String, ForeignKey
# Importa a base declarativa e o recurso de relacionamento entre tabelas
from sqlalchemy.orm import declarative_base , relationship

Base = declarative_base () 

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True)
    nome = Column (String)
    email = Column (String)

class Veterinário(Base):
    __tablename__ = "Veterinários"
    id = Column(Integer, primary_key=True)
    nome = Column (String)
    email = Column (String)
    telefone = Column (String)

    