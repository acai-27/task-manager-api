Project Title
# Task Manager API
Features
## Features

- Create Tasks
- Read Tasks
- Update Tasks
- Delete Tasks
- SQLite Database
- FastAPI
- SQLAlchemy ORM
- Pydantic Validation
Project Structure
## Project Structure

app/
├── main.py
├── db.py
├── model.py
├── schema.py
├── crud.py
└── routes/
    └── tasks.py
Installation
## Installation

```bash
pip install -r requirements.txt

---

## Run Server

```md id="’wini124"
## Run Server

```bash
uvicorn app.main:app --reload

---

## API Endpoints

```md id="’wini125"
| Method | Endpoint | Description |
|---|---|---|
| GET | /tasks | Get all tasks |
| GET | /tasks/{id} | Get single task |
| POST | /tasks | Create task |
| PUT | /tasks/{id} | Update task |
| DELETE | /tasks/{id} | Delete task |
Tech Stack
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic