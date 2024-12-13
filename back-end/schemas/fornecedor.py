from pydantic import BaseModel
from typing import Optional, List
from model.fornecedor import Fornecedor

from schemas import ComentarioSchemaFornecedor

class FornecedorSchema(BaseModel):
    nome: str = "Mechler Soluções"
    RG: int = 6234567342
    numero: int = 123456789
    servico: str = "Urbanismo"
    email: str = "teste@teste.com"
    site: str = "mechlersolucoes.com"

class FornecedorBuscaSchema(BaseModel):
    nome: str = "Teste"

class FornecedorDelSchema(BaseModel):
    mesage: str
    nome: str

class FornecedorViewSchema(BaseModel):
    id: int = 1
    nome: str = "Mechler Soluções"
    RG: int = 6234567342
    numero: int = 123456789
    servico: str = "Urbanismo"
    email: str = "teste@teste.com"
    site: str = "mechlersolucoes.com"
    total_comentaros: int = 1
    comentarios:List[ComentarioSchemaFornecedor]


class ListagemFornecedoresSchema(BaseModel):
    """ Define como uma listagem de fornecedores  será retornada.
    """
    produtores:List[FornecedorSchema]


def apresenta_fornecedor(fornecedor: Fornecedor):
    return {
        "nome": fornecedor.nome,
        "RG": fornecedor.RG,
        "numero": fornecedor.numero,
        "servico": fornecedor.servico,
        "email": fornecedor.email,
        "site": fornecedor.site,
        "comentarios": [{"texto": c.texto} for c in fornecedor.comentarios]
    }


def apresenta_fornecedores(fornecedores: list[Fornecedor]):
    result = []
    for fornecedor in fornecedores:
        result.append({
            "nome": fornecedor.nome,
            "RG": fornecedor.RG,
            "numero": fornecedor.numero,
            "servico": fornecedor.servico,
            "email": fornecedor.email,
            "site": fornecedor.site,
        })
    return {"fornecedores": result}
