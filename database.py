from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuramos SQLite
DATABASE_URL = "sqlite:///./frases.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Definimos cómo se ve nuestra tabla en la base de datos
class FraseDB(Base):
    __tablename__ = "frases"
    id = Column(Integer, primary_key=True, index=True)
    texto = Column(String)
    autor = Column(String)

# Creamos las tablas
def init_db():
    Base.metadata.create_all(bind=engine)