from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.usuario import Usuario

def listar_usuarios(db:Session):
    usuarios = db.query(Usuario).all()

    return usuarios

def listar_usuario(db: Session, id: int):
    usuario = db.query(Usuario).filter_by(id=id).first()
    if not usuario:
        raise HTTPException(
            status_code=404,
            detail="usuario nao encontrado"
        )
    
    return usuario

def deletar_usuario(db: Session, id: int):
    usuario = db.query(Usuario).filter_by(id=id).first()
    if not usuario:
        raise HTTPException(
            status_code=404,
            detail="usuario nao encontrado"
        )
    
    db.delete(usuario)
    db.commit()