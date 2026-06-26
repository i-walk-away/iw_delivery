# IW delivery

FastAPI-based project to showcase and implement the Three-Tier-Architecture.

## About this project

IW Delivery is a backend project simulating a simple operator-assisted food delivery service. The concept is that
the user selects items from the menu, specifies their address and places an order, after which an operator collects it
and dispatches the delivery to the user.

## Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Alembic](https://alembic.sqlalchemy.org/en/latest/)
- [MySQL](https://www.mysql.com/)
- [Docker](https://www.docker.com/)
- [uv](https://github.com/astral-sh/uv)

## Documentation

API specification: [docs/api_specification](docs/api_specification.md) 

## Setup & Installation

- Clone the repository

- Make `.env` file like this:

```bash
cp .env.example .env
```

- Run the following command to build the project:  
  `docker-compose up --build`

- Apply database migrations:

```bash
docker exec -it iw_delivery uv run alembic upgrade head 
```