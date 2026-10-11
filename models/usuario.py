from sqlalchemy import Column, Integer, String
from models.conexao import Base


class Usuarios(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(200))
    email = Column(String(50))
    senha = Column(String(100))
    departamento = Column(String(200))
    ramal = Column(String(15))
    status = Column(String(15))