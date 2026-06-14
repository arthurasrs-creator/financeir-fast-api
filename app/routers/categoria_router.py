from fastapi import APIRouter, Depends

router = APIRouter(prefix="/categorias", tags=["Categoria"])

from sqlalchemy.orm import Session
from app.schemas.categoria_schema import CategoriaResponse, CategoriaCreate
from app.database import get_db
from app.services.categoria_service import criar_categoria, listar_categorias, listar_categoria, deletar_categoria

@router.post("", response_model=CategoriaResponse)
def create_categoria(categoria: CategoriaCreate, db: Session = Depends(get_db)):
    return criar_categoria(db, categoria.nome)

@router.get("", response_model=list[CategoriaResponse])
def read_categorias(db: Session = Depends(get_db)):
    return listar_categorias(db)

@router.get("/{id}", response_model=CategoriaResponse)
def read_categoria(id:int, db: Session = Depends(get_db)):
    return listar_categoria(db, id)

@router.delete("/{id}", status_code=204)
def delete_categoria(id:int, db: Session = Depends(get_db)):
    deletar_categoria(db, id)