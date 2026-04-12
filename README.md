# FastAPI Cars API

A simple FastAPI project using MySQL and SQLAlchemy.

## Features

- Add a car
- List cars
- Dockerized MySQL + API

## Project structure

```text
fastapi_cars_app/
├── app/
│   ├── __init__.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   └── schemas.py
├── .env.example
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## Setup

1. Copy the environment file:

```bash
cp .env.example .env
```

2. Start the app:

```bash
docker compose up --build
```

3. Open the API docs:

```text
http://localhost:8000/docs
```

## API endpoints

### Create a car

`POST /cars`

Request body:

```json
{
  "brand": "Toyota",
  "model": "Corolla",
  "year": 2022,
  "color": "White"
}
```

### List cars

`GET /cars`

## Notes

- The API creates the `cars` table automatically on startup.
- This is a simple starter project, suitable for learning or extension.
