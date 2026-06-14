from fastapi import APIRouter, Depends

router = APIRouter()

from sqlalchemy.orm import Session

from app.database import Base, engine, get_db

from app.schemas.usuario_schema import UsuarioCreate, UsuarioLogin, UsuarioResponse
from app.services.auth_service import criar_usuario, logar_usuario

@router.post("/register", response_model=UsuarioResponse)
def register(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    return criar_usuario(
        db,
        usuario.nome,
        usuario.email,
        usuario.senha
    )


@router.post("/login", response_model=UsuarioResponse)
def login(usuario: UsuarioLogin, db: Session = Depends(get_db)):
    return logar_usuario(
        db,
        usuario.email,
        usuario.senha
    )
