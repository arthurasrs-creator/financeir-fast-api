from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.database import Base, engine, get_db
from app.models.usuario import Usuario

Base.metadata.create_all(bind=engine)

app = FastAPI()

from app.routers.auth_router import router as auth_router

app.include_router(auth_router)

@app.get("/teste-db")
def teste_db(db: Session = Depends(get_db)):
    return {db}

