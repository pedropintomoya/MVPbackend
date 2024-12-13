# Back-End

Projeto MPV do curso de desenvolvimento full-stack basico da PUC-RJ

Pedro Pinto Moya

Para poder implementar a solução proposta pelo projeto, criei 3 tabelas distintas no banco de dados (produtor, fornecedor, evento) assim como tabelas de comentários para cada um deles. Utilizei das mesmas chamadas propostas nas aulas durante o periodo. Foram criadas chamadas diferentes para cada uma das tabelas.

## Execução

Utilizei das mesmas ferramentas mostradas na aula 3. Vale ressaltar que, por alguma razão, não consegui instalar as bibliotecas com a versão mais recente do python. Tive que realizar um downgrade para uma versão mais antiga (3.12.3). 

Assim como nos exemplos em aula, primeiro precisamos instalar os requerimentos presentes no requirements.txt.
Para isso, basta executar o comando:

```
pip install -r requirements.txt
```

No terminal com diretório na pasta back-end.
Para inicializar o servidor, basta rodar o comando

```
flask run --host 0.0.0.0 --port 5000
```
ou
```
flask run --host 0.0.0.0 --port 5000 --reload
```

Também na pasta back-end. 
Abrindo o local (http://localhost:5000/#/) em seu navegador levara a abertura da API, onde é possível ver as chamadas do servidor pelo SWAGGER.