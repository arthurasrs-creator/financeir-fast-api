from sqlalchemy.orm import Session
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.usuario import Usuario

def criar_usuario(db: Session, nome:str, email:str, senha:str):
    senha_hash = generate_password_hash(senha)
    usuario = Usuario(nome=nome, email=email, senha=senha_hash)

    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    
    return usuario

def logar_usuario(db: Session, email:str, senha:str):
    usuario = (db.query(Usuario).filter(Usuario.email == email).first())
    if not usuario:
        return None
    
    if not check_password_hash(usuario.senha, senha):
        return "senha incorreta"
    
    return usuario