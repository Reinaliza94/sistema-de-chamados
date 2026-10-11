# Model chamados
from sqlalchemy import Column, Integer, String, DateTime
from models.conexao import Base


class Chamados(Base):
    __tablename__ = "chamados"

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(200))
    descricao = Column(String(500))
    data_abertura = Column(DateTime)
    data_fechamento = Column(DateTime)
    status = Column(String(20))
    prioridade = Column(String(20))
    categoria = Column(String(100))
    id_usuario = Column(Integer)
    responsavel_tecnico = Column(String(200))