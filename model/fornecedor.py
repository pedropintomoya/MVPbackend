from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base, ComentarioFornecedor

class Fornecedor(Base):
    __tablename__ = 'fornecedor'

    id = Column("pk_fornecedor", Integer, primary_key=True)
    nome = Column(String(), unique=True)
    RG = Column(Integer, unique = True)
    numero = Column(Integer)
    servico = Column(String())
    email = Column(String())
    site = Column(String())
    comentarios = relationship("ComentarioFornecedor")


    def __init__(self, nome:str, RG:int, numero:int, servico:str, email:str, site:str,
                 data_insercao:Union[DateTime, None] = None):
        self.nome = nome
        self.RG = RG
        self.numero = numero
        self.servico = servico
        self.email = email
        self.site = site

        if data_insercao:
            self.data_insercao = data_insercao       
        


    def adiciona_comentario(self, comentario:ComentarioFornecedor):
        """ Adiciona um novo comentário ao Produto
        """
        self.comentarios.append(comentario)   



