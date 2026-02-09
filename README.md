# Little Lemon API - Capstone Project 🍋

## O Projeto Escolhido 🎯

Este projeto é uma API robusta desenvolvida como parte do **Capstone Project** do curso **Meta Back-End Developer Professional Certificate**. O objetivo foi criar um sistema de backend completo para o restaurante fictício "Little Lemon", permitindo que clientes consultem o cardápio e reservem mesas, enquanto gerentes e administradores possuem controle total sobre o inventário e as operações.

A aplicação foi construída utilizando **Django** e **Django REST Framework (DRF)**, focando em boas práticas de design de API, segurança, autenticação e performance.

## Funcionalidades Implementadas ⚙️

O sistema desenvolvido conta com as seguintes funcionalidades principais:

* **Gestão de Cardápio (Menu API)**: Endpoints completos (CRUD) para listar, criar, atualizar e deletar itens do cardápio.
* **Sistema de Reservas**: Permite que usuários autenticados reservem mesas para datas e horários específicos.
* **Autenticação Robusta**: Implementação de autenticação baseada em Tokens e Session utilizando a biblioteca **Djoser**.
* **Controle de Acesso (Permissões)**:
    * **Clientes**: Podem visualizar o menu e fazer reservas.
    * **Gerentes**: Podem gerenciar itens do menu e entregadores.
    * **Administradores**: Acesso total ao sistema.
* **Filtragem, Ordenação e Paginação**: Recursos avançados para facilitar a busca de itens no cardápio por preço, categoria, etc.
* **Throttling (Limitação de Taxa)**: Proteção da API contra excesso de requisições, garantindo estabilidade.
* **Testes Automatizados**: Testes unitários para garantir a integridade dos endpoints e regras de negócio.

## Tecnologias Utilizadas 🛠️

* **Python**: Linguagem principal do projeto.
* **Django**: Framework web de alto nível para desenvolvimento rápido.
* **Django REST Framework (DRF)**: Ferramenta poderosa para construção de Web APIs.
* **Djoser**: Biblioteca para autenticação e gerenciamento de usuários.
* **Pipenv**: Gerenciamento de dependências e ambiente virtual.
* **SQLite/MySQL**: Banco de dados para persistência das informações.
* **Insomnia / Postman**: Ferramentas utilizadas para testar as requisições da API.

## Estrutura do Projeto 📁

```bash
Little-Lemon/
├── littlelemon/            # Configurações principais do projeto (Settings, URLs base)
├── restaurant/             # App principal contendo a lógica de negócio
│   ├── migrations/         # Arquivos de migração do banco de dados
│   ├── models.py           # Modelos de dados (Menu, Booking, etc.)
│   ├── serializers.py      # Serializadores para conversão de dados
│   ├── urls.py             # Rotas específicas da API
│   └── views.py            # Controladores (ViewSets e Generics)
├── media/                  # Arquivos de mídia (imagens dos pratos)
├── manage.py               # Utilitário de linha de comando do Django
├── Pipfile                 # Arquivo de definição de dependências
├── Pipfile.lock            # Arquivo de bloqueio de versões
├── db.sqlite3              # Banco de dados local (padrão)
└── README.md               # Este arquivo

```

## Endpoints Principais da API 🔗

Aqui estão algumas das rotas disponíveis para teste:

| Método | Endpoint | Descrição | Permissão |
| --- | --- | --- | --- |
| `GET` | `/api/menu-items/` | Lista todos os pratos | Qualquer um |
| `POST` | `/api/menu-items/` | Adiciona um novo prato | Gerente/Admin |
| `GET` | `/api/bookings/` | Lista as reservas | Usuário Autenticado |
| `POST` | `/api/token/login/` | Gera token de acesso | Qualquer um |
| `POST` | `/api/users/` | Cria um novo usuário | Qualquer um |

## Como Rodar o Projeto 🚀

Para rodar a API localmente, siga os passos abaixo:

### 1. Clonar o Repositório 🧑‍💻

Clone o repositório utilizando o comando Git:

```bash
git clone [https://github.com/MatheusFigueiredo7/Little-Lemon.git](https://github.com/MatheusFigueiredo7/Little-Lemon.git)

```

### 2. Navegar até o Diretório 📂

```bash
cd Little-Lemon

```

### 3. Instalar Dependências 📦

Certifique-se de ter o `pipenv` instalado e execute:

```bash
pipenv install
pipenv shell

```

### 4. Configurar o Banco de Dados 🗄️

Aplique as migrações para criar as tabelas necessárias:

```bash
python manage.py migrate

```

### 5. Executar o Servidor 🌐

Inicie o servidor de desenvolvimento:

```bash
python manage.py runserver

```

A API estará disponível em `http://127.0.0.1:8000/`.

## Testando a API 🧪

Para testar os endpoints:

1. Acesse `http://127.0.0.1:8000/api/menu-items/` no navegador ou via Insomnia/Postman.
2. Para funcionalidades administrativas, crie um superusuário:
```bash
python manage.py createsuperuser

```


3. Faça login no painel administrativo em `http://127.0.0.1:8000/admin/`.

---
