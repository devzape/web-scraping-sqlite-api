from bs4 import BeautifulSoup
from database import FraseDB, SessionLocal, init_db
from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
import requests

# 1. Inicializamos la base de datos y la app
init_db()

app = FastAPI(
    title="Scraper API Pro con Paginación y Aleatoriedad",
    description=(
        "API robusta que extrae frases, usa base de datos y permite paginar"
        " aleatoriamente."
    ),
)


# 2. Esquemas Pydantic
class FraseResponse(BaseModel):
  id: int
  texto: str
  autor: str

  class Config:
    from_attributes = True


# 3. Dependencia de Base de Datos
def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()


# 4. Función de Scraping Multipage
def hacer_scraping_completo(db: Session):
  url_base = "http://quotes.toscrape.com"
  url_actual = "/page/1/"

  while url_actual:
    try:
      respuesta = requests.get(url_base + url_actual, timeout=5)
      respuesta.raise_for_status()
    except requests.RequestException:
      raise HTTPException(
          status_code=503,
          detail="Error de conexión al intentar extraer los datos de la web.",
      )

    soup = BeautifulSoup(respuesta.text, "html.parser")
    bloques_frases = soup.find_all("div", class_="quote")

    for bloque in bloques_frases:
      texto = bloque.find("span", class_="text").text
      autor = bloque.find("small", class_="author").text

      if not db.query(FraseDB).filter(FraseDB.texto == texto).first():
        nueva_frase = FraseDB(texto=texto, autor=autor)
        db.add(nueva_frase)

    boton_siguiente = soup.find("li", class_="next")
    if boton_siguiente:
      url_actual = boton_siguiente.find("a")["href"]
    else:
      url_actual = None

  db.commit()


# 5. Endpoints (GET y POST)
@app.get("/frases", response_model=list[FraseResponse])
def obtener_frases(
    limit: int = 5, offset: int = 0, db: Session = Depends(get_db)
):
  if db.query(FraseDB).count() == 0:
    hacer_scraping_completo(db)

  frases = (
      db.query(FraseDB).order_by(func.random()).offset(offset).limit(limit).all()
  )
  return frases


@app.post("/frases/refrescar")
def refrescar_frases(db: Session = Depends(get_db)):
  db.query(FraseDB).delete()
  db.commit()

  hacer_scraping_completo(db)

  total_frases = db.query(FraseDB).count()
  return {
      "mensaje": (
          "Base de datos actualizada con éxito y mezclada aleatoriamente."
      ),
      "total_frases_guardadas": total_frases,
  }