# Laskin

[![CodeFactor](https://www.codefactor.io/repository/github/vsevolodbazhan/laskin/badge)](https://www.codefactor.io/repository/github/vsevolodbazhan/laskin)
[![Requirements Status](https://requires.io/github/vsevolodbazhan/laskin/requirements.svg?branch=dev)](https://requires.io/github/vsevolodbazhan/laskin/requirements/?branch=dev)

The microservice for [Tomoru](https://tomoru.ru) that adds support for mathematical operations.

## Installation

```bash
pip install -r requirements.txt
```

or [Poetry](https://python-poetry.org):

```bash
poetry install
```

Poetry will install dev-dependencies as well. So use that if you are planning to contribute.

## Startup

Run development server with:

```bash
python app.py
```

or run production server with:

```bash
gunicorn app:app
```

## License

[MIT](https://github.com/vsevolodbazhan/laskin/blob/master/LICENSE)
