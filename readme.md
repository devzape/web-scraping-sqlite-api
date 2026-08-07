# 🚀 Web Scraping API Pro

Una API REST robusta y moderna construida con **FastAPI**, **SQLAlchemy** y **BeautifulSoup**. El sistema realiza *web scraping* automatizado de múltiples páginas, almacena y normaliza los datos en una base de datos relacional SQLite, y expone endpoints con paginación, aleatoriedad y validación de esquemas.

---

## 🛠️ Tecnologías Utilizadas

*   **Python 3.10+**
*   **FastAPI**: Framework web de alto rendimiento para construir APIs.
*   **SQLAlchemy**: ORM para la gestión y persistencia de bases de datos relacionales.
*   **BeautifulSoup4**: Librería para la extracción de datos (Web Scraping) desde documentos HTML.
*   **Pydantic**: Validación de datos y tipado estricto para las respuestas de la API.
*   **Uvicorn**: Servidor ASGI ultrarrápido.

---

## 📂 Estructura del Proyecto

```text
├── database.py       # Configuración de SQLAlchemy y modelo de la Base de Datos
├── main.py           # Endpoints de la API, lógica de scraping y manejo de errores
├── requirements.txt  # Dependencias del proyecto
└── README.md         # Documentación oficial