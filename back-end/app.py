from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Produtor, Fornecedor, Evento, ComentarioProdutor, ComentarioFornecedor, ComentarioEvento
from logger import logger
from schemas import *
from schemas import produtor, fornecedor, evento, comentario
from flask_cors import CORS


#tags para gerar comentarios
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
comentario_tag = Tag(name="ComentarioProdutor", description="Adição de um comentário à um produtos cadastrado na base")
produtor_tag = Tag(name="Produtor", description="Adição, visualização e remoção de produtores à base")
fornecedor_tag = Tag(name="Fornecedor", description="Adição, visualização e remoção de fornecedores à base")
evento_tag = Tag(name="Evento", description="Adição, visualização e remoção de fornecedores à base")


info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

#tela que permiti escolher o tipo de documentação e teste das schemas
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


#adiciona um produtor no banco de dados
@app.post('/produtor', tags=[produtor_tag],
          responses={"200": produtor.ProdutorViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_produto(form: ProdutorSchema):
    """Adiciona um novo produtor ao BD

    """
    produtorAux = Produtor(
        nome=form.nome,
        CPF=form.CPF,
        numero=form.numero,
        funcao=form.funcao,
        salario=form.salario,
        email=form.email,
        curriculum=form.curriculum)

    session = Session()
    session.add(produtorAux)
    session.commit()
    return produtor.apresenta_produtor(produtorAux), 200


#delete um produtor especifico
@app.delete('/produtor', tags=[produtor_tag], 
            responses={"200":produtor.ProdutorDelSchema, "404":ErrorSchema})
def del_produtor(query: produtor.ProdutorBuscaSchema):
    """Delete um novo produtor do DT
    
    """    
    produtor_nome = unquote(unquote(query.nome))
    print(produtor_nome)
    logger.debug(f"Deletando dados sobre produtor #{produtor_nome}")
    session = Session()
    produtor_deletado = session.query(Produtor).filter(Produtor.nome == produtor_nome).delete()
    session.commit()

    if produtor_deletado:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletado produtor #{produtor_nome}")
        return {"mesage": "Produto removido", "id": produtor_nome}
    
    else:
        # se o produtor não foi encontrado
        error_msg = "Produto não encontrado na base :/"
        logger.warning(f"Erro ao deletar produtor #'{produtor_nome}', {error_msg}")
        return {"mesage": error_msg}, 404


#Realiza uma busca por todos os produtores no BD
@app.get('/produtores', tags=[produtor_tag],
         responses={"200":produtor.ListagemProdutoresSchema, "404":ErrorSchema})
def get_produtores():
    """Retorna todos os produtores existentes no BD

    """
    logger.debug(f"Coletando produtores")
    session = Session()
    produtores = session.query(Produtor).all()

    if not produtores:
        return {"produtores": []}, 200
    
    else:
        logger.debug(f"%d rodutos econtrados" % len(produtores))
        print(produtores)
        return produtor.apresenta_produtores(produtores), 200


#procura por um produtor especifico
@app.get('/produtor',tags=[produtor_tag],
         responses={"200":produtor.ProdutorViewSchema, "400":ErrorSchema})
def get_produtor(query: produtor.ProdutorBuscaSchema):
    """Retorna um produtor especifico do BD

    """    
    produtor_nome = query.nome
    session = Session()
    produtor = session.query(Produtor).filter(Produtor.nome == produtor_nome)

    return produtor.apresenta_produtor(produtor), 200

#----------------------------Fornecedores---------------------------------------------

#POST na tabela fornecedor
@app.post('/fornecedor', tags=[fornecedor_tag],
          responses={"200": fornecedor.FornecedorViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_fornecedor(form: FornecedorSchema):
    """Adiciona um novo fornecedor ao BD
    
    """
    fornecedorAux = Fornecedor(
        nome=form.nome,
        RG=form.RG,
        numero=form.numero,
        servico=form.servico,
        email=form.email,
        site=form.site)

    session = Session()
    session.add(fornecedorAux)
    session.commit()
    return fornecedor.apresenta_fornecedor(fornecedorAux), 200


#procura na tabela fornecedor do BD todas os dados registrados
@app.get('/fornecedores', tags=[fornecedor_tag],
         responses={"200":fornecedor.ListagemFornecedoresSchema, "404":ErrorSchema})
def get_fornecedores():
    """Retorna todos os fornecedores presentes no BD
    
    """
    session = Session()
    fornecedores = session.query(Fornecedor).all()
    print(fornecedores)

    if not fornecedores:
        return {"fornecedores": []}, 200
    else:
        print(fornecedores)
        return fornecedor.apresenta_fornecedores(fornecedores), 200


#procura por um fornecedor especifico
@app.get('/fornecedor',tags=[fornecedor_tag],
         responses={"200":fornecedor.FornecedorViewSchema, "400":ErrorSchema})
def get_fornecedor(query: fornecedor.FornecedorBuscaSchema):
    """Retorna um fornecedor especifico do BD
    
    """
    fornecedor_nome = query.nome
    session = Session()
    fornecedorAUX = session.query(Fornecedor).filter(Fornecedor.nome == fornecedor_nome)
    return fornecedor.apresenta_fornecedor(fornecedorAUX), 200


#delete um fornecedor especifico
@app.delete('/fornecedor', tags=[fornecedor_tag], 
            responses={"200":fornecedor.FornecedorDelSchema, "404":ErrorSchema})
def del_fornecedor(query: fornecedor.FornecedorBuscaSchema):
    """Deleta um fornecedor especifico do BD
    
    """
    fornecedor_nome = unquote(unquote(query.nome))
    print(fornecedor_nome)
    logger.debug(f"Deletando dados sobre fornecedor #{fornecedor_nome}")
    session = Session()
    fornecedor_deletado = session.query(Fornecedor).filter(Fornecedor.nome == fornecedor_nome).delete()
    session.commit()

    if fornecedor_deletado:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletado fornecedor #{fornecedor_nome}")
        return {"mesage": "Produto fornecedor movido", "id": fornecedor_nome}
    
    else:
        # se o fornecedor não foi encontrado
        error_msg = "Produto não encontrado na base :/"
        logger.warning(f"Erro ao deletar produtor #'{fornecedor_nome}', {error_msg}")
        return {"mesage": error_msg}, 404

#----------------------------Eventos---------------------------------------------

#POST na tabela evento
@app.post('/evento', tags=[evento_tag],
          responses={"200": evento.EventoViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_evento(form: EventoSchema):
    """Adiciona um novo evento ao DT
    
    """
    eventoAux = Evento(
        nome=form.nome,
        cliente=form.cliente,
        data=form.data,
        tamanho=form.tamanho,
        numero=form.numero,
        email=form.email)

    session = Session()
    session.add(eventoAux)
    session.commit()
    return evento.apresenta_evento(eventoAux), 200


#procura na tabela evento do BD todas os dados registrados
@app.get('/eventos', tags=[evento_tag],
         responses={"200":evento.ListagemEventosSchema, "404":ErrorSchema})
def get_eventos():
    """Retorna todos os eventos presentes no BD
    
    """
    session = Session()
    eventos = session.query(Evento).all()
    print(eventos)

    if not eventos:
        return {"eventos": []}, 200
    else:
        print(eventos)
        return evento.apresenta_eventos(eventos), 200


#procura por um evento especifico
@app.get('/evento',tags=[evento_tag],
         responses={"200":evento.EventoViewSchema, "400":ErrorSchema})
def get_evento(query: evento.EventoBuscaSchema):
    """Retorna um evento especifico do BD
    
    """
    evento_nome = query.nome
    session = Session()
    eventoAUX = session.query(Evento).filter(Evento.nome == evento_nome)
    return evento.apresenta_evento(eventoAUX), 200


#delete um evento especifico
@app.delete('/evento', tags=[evento_tag], 
            responses={"200":evento.EventoDelSchema, "404":ErrorSchema})
def del_evento(query: evento.EventoBuscaSchema):
    """Deleta um evento especifico do BD
    
    """
    evento_nome = unquote(unquote(query.nome))
    print(evento_nome)
    logger.debug(f"Deletando dados sobre evento #{evento_nome}")
    session = Session()
    evento_deletado = session.query(Evento).filter(Evento.nome == evento_nome).delete()
    session.commit()

    if evento_deletado:
        logger.debug(f"Deletado evento #{evento_nome}")
        return {"mesage": "Produto evento movido", "id": evento_nome}
    else:
        error_msg = "Produto não encontrado na base :/"
        logger.warning(f"Erro ao deletar evento #'{evento_nome}', {error_msg}")
        return {"mesage": error_msg}, 404

#--------------------------Comentarios-------------------------------------------------------

#Adiciona um comentario com um produtor registrado
@app.post('/cometario/Produtor', tags=[comentario_tag],
          responses={"200": produtor.ProdutorViewSchema, "404": ErrorSchema})
def add_comentario_produtor(form: comentario.ComentarioSchemaProdutor):
    """Inseri um comentario em um produtor especifico (ID)

    """
    produtor_id  = form.produtor_id
    logger.debug(f"Adicionando comentários ao produtor #{produtor_id}")
    session = Session()
    produtorAUX = session.query(Produtor).filter(Produtor.id == produtor_id).first()

    if not produtorAUX:
        error_msg = "Produtor não encontrado na base :/"
        logger.warning(f"Erro ao adicionar comentário ao produtor '{produtor_id}', {error_msg}")
        return {"mesage": error_msg}, 404

    texto = form.texto
    comentarioAUX = ComentarioProdutor(texto)

    produtorAUX.adiciona_comentario(comentarioAUX)
    session.commit()

    logger.debug(f"Adicionado comentário ao produtor #{produtor_id}")

    return produtor.apresenta_produtor(produtorAUX), 200


#Adiciona um comentario com um fornecedor registrado
@app.post('/cometario/Fornecedor', tags=[comentario_tag],
          responses={"200": fornecedor.FornecedorViewSchema, "404": ErrorSchema})
def add_comentario_fornecedor(form: comentario.ComentarioSchemaFornecedor):
    """Inseri um comentario em um fornecedor especifico (ID)

    """
    fornecedor_id  = form.fornecedor_id
    logger.debug(f"Adicionando comentários ao fornecedor #{fornecedor_id}")
    session = Session()
    fornecedorAUX = session.query(Fornecedor).filter(Fornecedor.id == fornecedor_id).first()

    if not fornecedorAUX:
        error_msg = "Fornecedor não encontrado na base :/"
        logger.warning(f"Erro ao adicionar comentário ao fornecedor '{fornecedor_id}', {error_msg}")
        return {"mesage": error_msg}, 404

    texto = form.texto
    comentarioAUX = ComentarioFornecedor(texto)
    fornecedorAUX.adiciona_comentario(comentarioAUX)
    session.commit()
    logger.debug(f"Adicionado comentário ao fornecedor #{fornecedor_id}")
    return fornecedor.apresenta_fornecedor(fornecedorAUX), 200


#Adiciona um comentario com um evento registrado
@app.post('/cometario/Evento', tags=[comentario_tag],
          responses={"200": evento.EventoViewSchema, "404": ErrorSchema})
def add_comentario_evento(form: comentario.ComentarioSchemaEvento):
    """Inseri um comentario em um evento especifico (ID)

    """
    evento_id  = form.evento_id
    logger.debug(f"Adicionando comentários ao evento #{evento_id}")
    session = Session()
    eventoAUX = session.query(Evento).filter(Evento.id == evento_id).first()

    if not eventoAUX:
        error_msg = "Evento não encontrado na base :/"
        logger.warning(f"Erro ao adicionar comentário ao evento '{evento_id}', {error_msg}")
        return {"mesage": error_msg}, 404

    texto = form.texto
    comentarioAUX = ComentarioEvento(texto)
    eventoAUX.adiciona_comentario(comentarioAUX)
    session.commit()
    logger.debug(f"Adicionado comentário ao evento #{evento_id}")
    return evento.apresenta_evento(eventoAUX), 200

