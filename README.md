# 🧑‍💻 CRUD de Usuários em Python

Este projeto é uma aplicação simples de **CRUD (Create, Read, Update, Delete)** de usuários feita com **Python puro** em interface de terminal. Ele permite gerenciar uma pequena base de dados de usuários simulada com dicionários em memória.

## 📋 Funcionalidades

- ✅ Criar usuários com nome e idade  
- ✅ Listar todos os usuários cadastrados  
- ✅ Buscar usuários por ID  
- ✅ Atualizar dados de um usuário existente  
- ✅ Deletar usuários pelo ID  
- ✅ Menu interativo no terminal

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- Sem dependências externas

## 🚀 Como Executar

1. Certifique-se de ter o Python instalado (versão 3.6 ou superior).
2. Salve o código em um arquivo chamado `crud_usuarios.py`.
3. Execute o script pelo terminal:

```bash
python crud_usuarios.py
```
Siga as instruções do menu para interagir com a aplicação.

# 🧠 Estrutura do Projeto
O sistema armazena os dados dos usuários em um dicionário Python com o formato:
```
usuarios = {
    1: {"nome": "João", "idade": 30},
    2: {"nome": "Maria", "idade": 25}
}
```
Cada operação (criar, listar, buscar, atualizar, deletar) é implementada como uma função separada, e o programa exibe um menu interativo com as opções disponíveis.

# 🎯 Objetivo
Este projeto foi desenvolvido com fins educacionais para treinar lógica de programação, manipulação de estruturas de dados em Python e interação via terminal.
