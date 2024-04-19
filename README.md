# Simulador de investimentos em renda fixa - Cooperativa de crédito

O projeto "Simulador de investimentos em renda fixa" é uma aplicação desenvolvida para cooperativas de crédito, permitindo que os usuários simulem investimentos em renda fixa, como LCAs, LCIs, RDCs e muitos outros. Através da inserção de parâmetros como valor aplicado, prazo e taxa de juros, os usuários podem calcular a rentabilidade esperada de seus investimentos. Além disso, a aplicação oferece a funcionalidade de salvar simulações realizadas para referência futura. O projeto utiliza Flask como framework web em Python, integrado com SQLAlchemy para manipulação de banco de dados MySQL.

## Objetivo
Projeto MVP para o fim da primeira Sprint/Modulo do curso de pós-graduação em Engenharia de Software da PUC Rio

## Pré-requisitos

Certifique-se de ter os seguintes requisitos antes de começar:

- Python 3.12 instalado
- pip (gerenciador de pacotes do Python) instalado
- mysql server

## Instalação

1. Clone o repositório:

```
git clone https://github.com/gustavogalmeida/flask_mvp_simulador-de-investimentos_puc_rio.git
```

2. Navegue até o diretório do projeto:
```
cd flask_mvp_simulador-de-investimentos_puc_rio
```
3. Instale as dependências do Python:
```
pip install -r requirements.txt
```
4. Crie o banco de dados e tabelas rodando o script
```
python prepara_banco.py
```
## Uso

1. Inicie o servidor Flask:
```
python app.py
```
2. Abra o navegador e acesse http://127.0.0.1:5000 ou clique [aqui](http://127.0.0.1:5000), para ver a aplicação em execução.

## Estrutura do projeto

/flask_mvp_simulador-de-investimentos_puc_rio
│  
│   prepara_banco.py  
│   readme.md  
│   requirements.txt  
│   run.py  
├───app  
│   │   init.py  
│   │   helpers.py  
│   │   models.py  
│   │   views.py  
│   │  
│   ├───templates  
│   │   │   index.html  
│   │  
│   └───static  
│   │   │   style.css  

## Contribuição
Contribuições são bem-vindas! Para sugestões de melhorias, abra uma issue neste repositório.

## Licença
Este projeto está licenciado sob a Licença MIT.