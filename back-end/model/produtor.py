from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base, ComentarioProdutor

class Produtor(Base):
    __tablename__ = 'produtor'

    id = Column("pk_produtor", Integer, primary_key=True)
    nome = Column(String(), unique=True)
    CPF = Column(Integer, unique = True)
    numero = Column(Integer)
    funcao = Column(String())
    salario = Column(Integer)
    email = Column(String())
    curriculum = Column(String())
    data_insercao = Column(DateTime, default=datetime.now())

    comentarios = relationship("ComentarioProdutor")



    def __init__(self, nome:str, CPF:int, numero:int, funcao:str, salario:int, 
                 email:str, curriculum:str, data_insercao:Union[DateTime, None] = None):
        
        self.nome = nome
        self.CPF = CPF
        self.numero = numero
        self.funcao = funcao
        self.salario = salario
        self.email = email
        self.curriculum = curriculum

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao        

    def adiciona_comentario(self, comentario:ComentarioProdutor):
        """ Adiciona um novo comentário ao Produto
        """
        self.comentarios.append(comentario)   
