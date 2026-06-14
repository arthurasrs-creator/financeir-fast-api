from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.database import Base, engine, get_db
from app.models.usuario import Usuario
from app.models.categoria import Categoria

Base.metadata.create_all(bind=engine)

app = FastAPI()

from app.routers.auth_router import router as auth_router
from app.routers.usuario_router import router as usuario_router
from app.routers.categoria_router import router as categoria_router

app.include_router(auth_router)
app.include_router(usuario_router)
app.include_router(categoria_router)

@app.get("/teste-db")
def teste_db(db: Session = Depends(get_db)):
    return {db}

