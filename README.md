# kris-Datavault
A full-stack web application built with Flask, React (Vite), and PostgreSQL, containerized with Docker Compose.
Manage “items” (title, description, price) via a clean React UI and a Flask REST API.

Features

* Flask API with SQLAlchemy & Alembic migrations

* PostgreSQL running in Docker

* React (Vite) frontend with live API integration

* CORS-enabled backend for local dev

* CI tests with Pytest & GitHub Actions

* One-command local start using Docker Compose


Tech Stack
* Layer	Technology
* Frontend	React + Vite + Fetch
* Backend	Flask, Flask-CORS, SQLAlchemy
* Database	PostgreSQL
* Infra	Docker, Docker Compose
* CI	GitHub Actions, pytest
* Lang	Python 3.11+/JS (ES6+)

flask-pg-compose/
│
├─ app/
│  ├─ app.py              # Flask app entrypoint (routes & factory)
│  ├─ models.py           # SQLAlchemy models
│  ├─ seed.py             # DB seed data
│  ├─ requirements.txt    # Python deps
│  └─ start.sh            # Wait for DB, run migrations, start Flask
│
├─ frontend/
│  ├─ src/                # React components
│  ├─ public/             # Static assets
│  ├─ vite.config.js      # Dev server + proxy to Flask
│  └─ package.json
│
├─ tests/
│  └─ test_items.py       # Backend API tests
│
├─ docker-compose.yml
├─ Dockerfile
└─ README.md


Getting Started

git clone https://github.com/<your-username>/kris-datavault.git
cd kris-datavault


Environment (local dev)

Create .env in the project root:

POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=appdb
POSTGRES_HOST=db

Run everything with Docker
docker compose up --build

Backend (Flask): http://localhost:5001

Frontend (Vite): http://localhost:5173

PI Examples

GET all items

curl http://localhost:5001/items

POST a new item

curl -X POST http://localhost:5001/items \
  -H "Content-Type: application/json" \
  -d '{"title":"Website Hosting","description":"Managed hosting plan","price":19.99}'


Tests (CI & Local)

Run backend tests locally:

pytest -v tests/


Deployment

This stack can run anywhere with Docker:

Render.com / Fly.io / Railway.app

Any VPS with Docker installed

Manual start on a remote host:

docker compose up -d --build


Author

Kristian Atalla

LinkedIn: https://www.linkedin.com/in/kristian-atalla-6a279b253/

GitHub: https://github.com/kr1stiann

