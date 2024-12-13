from pydantic import BaseModel
from typing import Optional, List
from model.produtor import Produtor

from schemas import ComentarioSchemaProdutor

class ProdutorSchema(BaseModel):
    nome: str = "Marcos Werneck"
    CPF: int = 12345678901
    numero: int = 123456789
    funcao: str = "carregador"
    salario: float = 150
    email: str = "teste@teste.comm"
    curriculum: str = "linkdolinkedin.com"

class ProdutorBuscaSchema(BaseModel):
    nome: str = "Teste"

class ProdutorDelSchema(BaseModel):
    mesage: str
    nome: str

class ProdutorViewSchema(BaseModel):
    id: int = 1
    nome: str = "Marcos Werneck"
    CPF: int = 12345678901
    numero: int = 123456789
    funcao: str = "carregador"
    salario: float = 150
    email: str = "teste@teste.comm"
    curriculum: str = "linkdolinkedin.com"
    total_comentaros: int = 1
    comentarios:List[ComentarioSchemaProdutor]

class ListagemProdutoresSchema(BaseModel):
    """ Define como uma listagem de produtores será retornada.
    """
    produtores:List[ProdutorSchema]



def apresenta_produtores(produtores: list[Produtor]):
    result = []
    for produtor in produtores:
        result.append({
            "nome": produtor.nome,
            "CPF": produtor.CPF,
            "numero": produtor.numero,
            "funcao": produtor.funcao,
            "salario": produtor.salario,
            "email": produtor.email,
            "curriculum": produtor.curriculum
        })
    return {"produtores": result}


def apresenta_produtor(produtor: Produtor):
    return {
        "nome": produtor.nome,
        "CPF": produtor.CPF,
        "numero": produtor.numero,
        "funcao": produtor.funcao,
        "salario": produtor.salario,
        "email": produtor.email,
        "curriculum": produtor.curriculum,
        "comentarios": [{"texto": c.texto} for c in produtor.comentarios]
    }
