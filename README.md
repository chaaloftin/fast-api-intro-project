# Fast API Intro Project

An into to FastAPI via their User Guide tutorial

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed the latest version of [Python](https://www.python.org/downloads/).
- You have installed [Poetry](https://python-poetry.org/docs/#installation).

## Installation

To install this project, follow these steps and then :

```bash
git clone https://github.com/your-username/your-project
cd your-project
poetry shell
poetry install
uvicorn main:app --reload # start the server at http://127.0.0.1:8000


# The command uvicorn main:app refers to:
# main: the file main.py (the Python "module").
# app: the object created inside of main.py with the line app = FastAPI().
# --reload: make the server restart after code changes. Only use for development.
```

You should be able to navigate to the following links successfully after completing the previous steps

- `http://127.0.0.1:8000` - Root Get Request
- `http://127.0.0.1:8000/docs#/` - OpenAPI Documentation
- `http://127.0.0.1:8000/openapi.json` - Raw JSON schema

## Troubleshooting

### Interpreter Issues

Get the path to your venv interpreter and then set this path in your IDE

```bash
poetry shell
poetry env info
```
