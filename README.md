# Brain Agriculture - API de Gerenciamento de Produtores Rurais

## Índice
- [Introdução](#introdução)
- [Funcionalidades](#funcionalidades)
- [Instalação](#instalação)
  - [Pré-requisitos](#pré-requisitos)
  - [Configuração do Backend](#configuração-do-backend)
- [Endpoints da API](#endpoints-da-api)
- [Testes](#testes)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Melhorias Futuras](#melhorias-futuras)

## Introdução
O Brain Agriculture é uma API desenvolvida com FastAPI para gerenciamento de produtores rurais, suas fazendas e cultivos. Oferece operações CRUD robustas com validação de dados e endpoints analíticos para visualização em dashboard.

## Funcionalidades
- **Gestão de Produtores**: Operações CRUD para produtores rurais
- **Gestão de Fazendas**: CRUD para fazendas associadas aos produtores
- **Gestão de Cultivos**: CRUD para cultivos nas fazendas
- **Validação de Dados**: Inclui validação de CPF/CNPJ e consistência de áreas (área agrícola + vegetação ≤ área total)
- **Dashboard Analítico**: Endpoints para dados agregados como total de fazendas, hectares totais e distribuição por estado, cultura e uso do solo
- **Banco de Dados**: PostgreSQL com Docker
- **Testes**: Testes unitários e de integração com Pytest

## Instalação

### Pré-requisitos
- Docker e Docker Compose instalados
- Git

### Configuração do Backend
1. Clone o repositório:

   ```bash
   git clone https://github.com/josejonatasoliveira/brain_agriculture_v2.git
   cd brain_agriculture
   ```

2. Configure as variáveis de ambiente:

   ```bash
   cp .env.example .env
   ```
   Edite o arquivo `.env` com suas credenciais do PostgreSQL.

3. Inicie os containers com Docker Compose:

   ```bash
   docker-compose up -d --build
   ```

4. Execute as migrations para criar as tabelas:

   ```bash
   docker-compose exec app alembic upgrade head
   ```

A API estará disponível em:

```bash
http://localhost:8000
```

### Como Executar

#### Rodar a Aplicação
```bash
docker-compose up -d
```

#### Rodar os Testes
```bash
docker-compose exec app pytest tests/
```

#### Rodar as Migrations
Para criar nova migration:

```bash
docker-compose exec app alembic revision --autogenerate -m "descrição das alterações"
```

Para aplicar migrations:

```bash
docker-compose exec app alembic upgrade head
```

## Endpoints da API
A documentação da API (OpenAPI/Swagger UI) está disponível em:

```bash
http://localhost:8000/docs
```

Principais endpoints:

### Produtores:
- `POST /producers/`: Cria novo produtor
- `GET /producers/`: Lista todos produtores
- `GET /producers/{producer_id}`: Busca produtor por ID
- `PUT /producers/{producer_id}`: Atualiza produtor
- `DELETE /producers/{producer_id}`: Remove produtor

### Fazendas:
- `POST /farms/`: Cria nova fazenda
- `GET /farms/`: Lista todas fazendas
- `GET /farms/{farm_id}`: Busca fazenda por ID
- `PUT /farms/{farm_id}`: Atualiza fazenda
- `DELETE /farms/{farm_id}`: Remove fazenda

### Cultivos:
- `POST /cultures/`: Cria novo cultivo
- `GET /cultures/`: Lista todos cultivos
- `GET /cultures/{culture_id}`: Busca cultivo por ID
- `PUT /cultures/{culture_id}`: Atualiza cultivo
- `DELETE /cultures/{culture_id}`: Remove cultivo

### Dashboard:
- `GET /dashboard/total_farms`: Total de fazendas
- `GET /dashboard/total_hectares`: Área total em hectares
- `GET /dashboard/farms_by_state`: Fazendas por estado
- `GET /dashboard/farms_by_culture`: Fazendas por tipo de cultivo
- `GET /dashboard/farms_by_soil_use`: Distribuição de uso do solo

## Testes
Para executar todos os testes:

```bash
docker-compose exec app pytest tests/
```

## Estrutura do Projeto
```text
brain_agriculture/
├── app/
│   ├── main.py
│   ├── models/
│   ├── routes/
│   ├── config/
│   └── utils/
├── tests/
├── alembic/
├── .env.example
├── docker-compose.yml
├── Dockerfile
└── requirements.txt
```

## Melhorias Futuras
- Autenticação e autorização
- Frontend com React
- Integração com mapas (GIS)
- Exportação de relatórios
- Notificações e alertas

