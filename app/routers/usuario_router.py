from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

from app.database import get_db
from app.schemas.usuario_schema import UsuarioResponse
from app.services.usuario_service import listar_usuarios, listar_usuario, deletar_usuario

@router.get("", response_model=list[UsuarioResponse])
def read_usuarios(db: Session = Depends(get_db)):
    usuarios = listar_usuarios(db)
    
    return usuarios

@router.get("/{id}", response_model=UsuarioResponse)
def read_usuario(id:int, db: Session = Depends(get_db)):
    usuario = listar_usuario(db, id=id)

    return usuario

@router.delete("/{id}", status_code=204)
def delete_usuario(id:int, db: Session = Depends(get_db)):
    deletar_usuario(db, id=id)
