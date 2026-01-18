from database import SessionLocal
from models import User


def delete_user_by_username(username):
    db = SessionLocal()

    user = db.query(User). filter_by(username=username).first()

    if not user:
        print("Usuário não encontrado")
        db.close()
        return

    db.delete(user)
    db.commit()

    print("Usuário deletado com sucesso")

    db.close()

#Testing

delete_user_by_username("joão")
delete_user_by_username("maria")