from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.categoria import Categoria

def criar_categoria(db: Session, nome:str):
    categoria = db.query(Categoria).filter_by(nome=nome).first()
    if categoria:
        raise HTTPException(
            status_code=409,
            detail="categoria duplicada"
        )
    
    nova_categoria = Categoria(nome=nome)

    db.add(nova_categoria)
    db.commit()
    db.refresh(nova_categoria)

    return nova_categoria

def listar_categorias(db:Session):
    categorias = db.query(Categoria).all()

    return categorias

def listar_categoria(db:Session, id:int):
    categoria = db.query(Categoria).filter_by(id=id).first()
    if not categoria:
        raise HTTPException(
            status_code=404,
            detail="categoria nao encontrada"
        )
    
    return categoria

def deletar_categoria(db:Session, id:int):
    categoria = db.query(Categoria).filter_by(id=id).first()
    if not categoria:
        raise HTTPException(
            status_code=404,
            detail="categoria nao encontrada"
        )
    
    db.delete(categoria)
    db.commit()