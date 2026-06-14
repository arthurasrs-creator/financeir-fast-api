from fastapi import HTTPException
from sqlalchemy.orm import Session
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.usuario import Usuario

def criar_usuario(db: Session, nome:str, email:str, senha:str):
    usuario = (db.query(Usuario).filter(Usuario.email == email).first())
    if usuario:
        raise HTTPException(
            status_code=409,
            detail="email já em uso"
        )
    senha_hash = generate_password_hash(senha)

    novo_usuario = Usuario(nome=nome, email=email, senha=senha_hash)

    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    
    return novo_usuario

def logar_usuario(db: Session, email:str, senha:str):
    usuario = (db.query(Usuario).filter(Usuario.email == email).first())
    if not usuario:
        raise HTTPException(
            status_code=404,
            detail="usuario nao encontrado"
        )
    
    if not check_password_hash(usuario.senha, senha):
        raise HTTPException(
            status_code=401,
            detail="senha incorreta"
        )
    
    return usuario