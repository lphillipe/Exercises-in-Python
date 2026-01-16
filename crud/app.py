from database import SessionLocal
from models import User


def update_email_by_username(username, new_email):
    db = SessionLocal()

    user = db.query(User).filter_by(username=username).first()

    if not user:
        print("Usuário não encontrado")
        db.close()
        return

    email_exists = db.query(User).filter_by(email=new_email).first()

    if email_exists:
        print("Email já está em uso")
        db.close()
        return

    user.email = new_email
    db.commit()

    print("Email atualizado com sucesso")

    db.close()

# testando

update_email_by_username("Oceana", "oceana2@gmail.com")
update_email_by_username("Kai", "xxt@gmail.com")
