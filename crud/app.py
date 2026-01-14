from database import SessionLocal
from models import User

#def create_user(username, email):
    db = SessionLocal()

    #error handling
    user_exists = db.query(User).filter_by(email=email).first()

    if user_exists:
        print(f"Email já cadastrado")
        db.close()
        return
    
    #Create Users
    user = User(
        username=username, 
        email=email, 
        password_hash="123456"
    )
    db.add(user)
    db.commit()

    print(f"Usuário criado com ID {user.id}")

    db.close()
def get_all_users():
    db = SessionLocal()
    users = db.query(User).all()

    for user in users:
        print(user.id, user.username, user.email)
    db.close()

def get_user_by_id(user_id):
    db = SessionLocal()

    user = db.query(User).filter_by(id=user_id).first()

    if user:
        print(user.username, user.email)
    else:
        print("Usuário não encontrado")

    db.close()

def get_user_by_email(email):
    db = SessionLocal()

    user = db.query(User).filter_by(email=email).first()

    if user:
        print(user.id, user.username)
    else:
        print("Email não encontrado")

    db.close()
    
if __name__== "__main__":
