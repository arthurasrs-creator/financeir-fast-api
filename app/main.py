from fastapi import FastAPI, Depends
from app.database import Base, engine, get_db
from app.models.usuario import Usuario

Base.metadata.create_all(bind=engine)

app = FastAPI()

from sqlalchemy.orm import Session
@app.get("/test-db")
def test_db(db: Session = Depends(get_db)):
    return {"msg": "db funcionando"}

#print(Base.metadata.tables.keys())

from fastapi import Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.usuario_schema import UsuarioCreate, UsuarioLogin
from app.services.usuario_service import criar_usuario, login

@app.post("/usuarios")
def criar(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    return criar_usuario(
        db, 
        usuario.nome,
        usuario.email,
        usuario.senha
    )

@app.post("/login")
def criar(dados: UsuarioLogin, db: Session = Depends(get_db)):
    usuario = login(
        db, 
        dados.email,
        dados.senha
    )

    return usuario