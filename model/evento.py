from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base, ComentarioEvento

class Evento(Base):
    __tablename__ = 'eventos'

    id = Column("pk_eventos", Integer, primary_key=True)
    nome = Column(String(), unique=True)
    cliente = Column(String(), unique = True)
    data = Column(String())
    tamanho = Column(String())
    numero = Column(Integer)
    email = Column(String())
    comentarios = relationship("ComentarioEvento")


    def __init__(self, nome:str, cliente:str, data:str, tamanho:str ,numero:int,  email:str,
                 data_insercao:Union[DateTime, None] = None):
        self.nome = nome
        self.cliente = cliente
        self.data = data
        self.tamanho = tamanho
        self.numero = numero
        self.email = email
        if data_insercao:
            self.data_insercao = data_insercao       
        
    def adiciona_comentario(self, comentario:ComentarioEvento):
        """ Adiciona um novo comentário ao Produto
        """
        self.comentarios.append(comentario)   


        
