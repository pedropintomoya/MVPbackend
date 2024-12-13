from pydantic import BaseModel
from typing import Optional, List
from model.evento import Evento

from schemas import ComentarioSchemaEvento

class EventoSchema(BaseModel):
    nome: str = "Baile de casamento"
    cliente: str = "Júlia Alves Cavalcanti"
    data: str = "2025-10-17"
    tamanho: str = "Medio"
    numero: int = 1168068598
    email: str = "cavalcanti85@gmail.com"

class EventoBuscaSchema(BaseModel):
    nome: str = "Teste"

class EventoDelSchema(BaseModel):
    mesage: str
    nome: str

class EventoViewSchema(BaseModel):
    id: int = 1
    nome: str = "Baile de casamento"
    cliente: str = "Júlia Alves Cavalcanti"
    data: str = "2025-10-17"
    tamanho: str = "Medio"
    numero: int = 1168068598
    email: str = "cavalcanti85@gmail.com"
    comentarios:List[ComentarioSchemaEvento]


class ListagemEventosSchema(BaseModel):
    """ Define como uma listagem de fornecedores  será retornada.
    """
    produtores:List[EventoSchema]




def apresenta_eventos(eventos: list[Evento]):
    result = []
    for evento in eventos:
        result.append({
            "nome": evento.nome,
            "cliente": evento.cliente,
            "data": evento.data,
            "tamanho": evento.tamanho,
            "numero": evento.numero,
            "email": evento.email,
        })
    return {"eventos": result}


def apresenta_evento(evento: Evento):
    return {
        "nome": evento.nome,
        "cliente": evento.cliente,
        "data": evento.data,
        "tamanho": evento.tamanho,
        "numero": evento.numero,
        "email": evento.email,
    }
