from database import SessionLocal
from models import User


def update_user_email(user_id, new_email):
    db = SessionLocal()

    user = db.query(User).filter_by(id=user_id).first()

    if not user:
        print("Usuário não encontrado")
        db.close()
        return

    user.email = new_email

    db.commit()

    print("Email atualizado com sucesso")

    db.close()

# testando
