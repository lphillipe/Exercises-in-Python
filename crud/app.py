from database import SessionLocal
from models import User


def delete_user_by_id(user_id):
    db = SessionLocal()

    user = db.query(User). filter_by(id=user_id).first()

    if not user:
        print("Usuário não encontrado")
        db.close()
        return

    db.delete(user)
    db.commit()

    print("Usuário deletado com sucesso")

    db.close

#Testing

delete_user_by_id(2)
delete_user_by_id(2)
delete_user_by_id(10)