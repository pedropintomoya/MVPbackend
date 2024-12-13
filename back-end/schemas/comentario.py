from pydantic import BaseModel


class ComentarioSchemaProdutor(BaseModel):
    """ Define como um novo comentário a ser inserido deve ser representado
    """
    produtor_id: int = 1
    texto: str = "Só comprar se o preço realmente estiver bom!"


class ComentarioSchemaFornecedor(BaseModel):
    """ Define como um novo comentário a ser inserido deve ser representado
    """
    fornecedor_id: int = 1
    texto: str = "Só comprar se o preço realmente estiver bom!"


class ComentarioSchemaEvento(BaseModel):
    """ Define como um novo comentário a ser inserido deve ser representado
    """
    evento_id: int = 1
    texto: str = "Só comprar se o preço realmente estiver bom!"
