from database import SessionLocal
from models import User

def create_user():
    db = SessionLocal()
    
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

if __name__== "__main__":
    create_user()