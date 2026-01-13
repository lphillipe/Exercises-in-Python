from database import engine, Base
from models import User

def create_user():
    db = SessionLocal()
    
    user = User(
        username="Luis Phillipe", 
        email="phillipe@gmail.com", 
        password_has="123456"
    )

    db.add(user)
    db.commit()

    print(f"Usuário criado com ID {user.id}")

    db.close()

if __name__== "__main__":
    create_user()