from sqlalchemy.orm import Session
from app.models.usuario import Usuario
from werkzeug.security import generate_password_hash, check_password_hash

def criar_usuario(db: Session, nome:str, email:str, senha:str):

    print(type(senha))
    print(repr(senha))
    print(len(senha))


    senha_hash = generate_password_hash(senha)
    usuario = Usuario(
        nome=nome,
        email=email,
        senha=senha_hash
    )

    db.add(usuario)
    db.commit()
    db.refresh(usuario)

    return usuario

def login(db: Session, email:str, senha:str):
    usuario = (
        db.query(Usuario)
        .filter(Usuario.email == email)
        .first()
    )
    if not usuario:
        return None
    
    if not check_password_hash(usuario.senha, senha):
        return False
    
    return usuario