from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from datetime import datetime
from typing import Union

from  model import Base


class ComentarioProdutor(Base):
    __tablename__ = 'comentario'

    id = Column(Integer, primary_key=True)
    texto = Column(String(4000))
    data_insercao = Column(DateTime, default=datetime.now())

    # Definição do relacionamento entre o comentário e um produtor.
    # Aqui está sendo definido a coluna 'produtor' que vai guardar
    # a referencia ao produtor, a chave estrangeira que relaciona
    # um produtor ao comentário.
    produtor = Column(Integer, ForeignKey("produtor.pk_produtor"), nullable=False)

    def __init__(self, texto:str, data_insercao:Union[DateTime, None] = None):
        """
        Cria um Comentário

        Arguments:
            texto: o texto de um comentário.
            data_insercao: data de quando o comentário foi feito ou inserido
                           à base
        """
        self.texto = texto
        if data_insercao:
            self.data_insercao = data_insercao

class ComentarioFornecedor(Base):
    __tablename__ = 'comentarioFornecedor'

    id = Column(Integer, primary_key=True)
    texto = Column(String(4000))
    data_insercao = Column(DateTime, default=datetime.now())

    # Definição do relacionamento entre o comentário e um fornecedor.
    # Aqui está sendo definido a coluna 'fornecedor' que vai guardar
    # a referencia ao fornecedor, a chave estrangeira que relaciona
    # um fornecedor ao comentário.
    fornecedor = Column(Integer, ForeignKey("fornecedor.pk_fornecedor"), nullable=False)

    def __init__(self, texto:str, data_insercao:Union[DateTime, None] = None):
        """
        Cria um Comentário

        Arguments:
            texto: o texto de um comentário.
            data_insercao: data de quando o comentário foi feito ou inserido
                           à base
        """
        self.texto = texto
        if data_insercao:
            self.data_insercao = data_insercao

class ComentarioEvento(Base):
    __tablename__ = 'comentarioEvento'

    id = Column(Integer, primary_key=True)
    texto = Column(String(4000))
    data_insercao = Column(DateTime, default=datetime.now())

    # Definição do relacionamento entre o comentário e um evento.
    # Aqui está sendo definido a coluna 'evento' que vai guardar
    # a referencia ao evento, a chave estrangeira que relaciona
    # um evento ao comentário.
    evento = Column(Integer, ForeignKey("eventos.pk_eventos"), nullable=False)

    def __init__(self, texto:str, data_insercao:Union[DateTime, None] = None):
        """
        Cria um Comentário

        Arguments:
            texto: o texto de um comentário.
            data_insercao: data de quando o comentário foi feito ou inserido
                           à base
        """
        self.texto = texto
        if data_insercao:
            self.data_insercao = data_insercao
