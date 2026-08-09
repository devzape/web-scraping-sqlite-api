# 🕷️ Web Scraping API Pro

API REST construida con **FastAPI** que realiza *web scraping* automatizado de múltiples páginas, procesa los datos con **BeautifulSoup** y los almacena de forma normalizada en una base de datos **SQLite** mediante **SQLAlchemy**.

<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi" />
  <img src="https://img.shields.io/badge/BeautifulSoup-43B02A?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white" />
</p>

## 🛠️ Tecnologías

- **Python 3.10+**
- **FastAPI** — framework web de alto rendimiento
- **SQLAlchemy** — ORM para persistencia en SQLite
- **BeautifulSoup4** — extracción de datos desde HTML
- **Pydantic** — validación y tipado de las respuestas
- **Uvicorn** — servidor ASGI

## ⚙️ Cómo correr el proyecto localmente

```bash
# 1. Clonar el repositorio
git clone https://github.com/devzape/web-scraping-sqlite-api.git
cd web-scraping-sqlite-api

# 2. Crear y activar un entorno virtual
python -m venv venv
source venv/bin/activate   # En Windows: venv\Scripts\activate

# 3. Instalar dependencias
pip install fastapi uvicorn sqlalchemy beautifulsoup4 requests

# 4. Levantar el servidor
uvicorn main:app --reload
```

La API queda disponible en `http://127.0.0.1:8000` y la documentación interactiva en `http://127.0.0.1:8000/docs`.

## 📌 ¿Qué hace?

1. Dispara el scraping de una o varias páginas web
2. Parsea el HTML con BeautifulSoup y extrae la info relevante
3. Normaliza y guarda los datos en SQLite vía SQLAlchemy
4. Expone los datos scrapeados por endpoints REST, con paginación (`skip` / `limit`)

## 📁 Estructura del proyecto

```
web-scraping-sqlite-api/
├── main.py            # Endpoints de la API y lógica de scraping
├── database.py        # Configuración de SQLAlchemy y modelo de la BD
└── requirements.txt   # Dependencias del proyecto
```

## 🚧 Próximas mejoras

- [ ] Agregar `requirements.txt` al repo (falta subirlo)
- [ ] Manejo de errores si la página scrapeada cambia de estructura
- [ ] Tests automatizados con Pytest
- [ ] Programar el scraping con un scheduler (ej. `APScheduler`)

---

> 💡 Nota: agregar un `.gitignore` para excluir entornos virtuales y bases de datos locales.
