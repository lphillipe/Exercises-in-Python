from database import SessionLocal
from models import User

def create_user():
    db = SessionLocal()
    
    user = User(
        username="Luis Phillipe", 
        email="phillipe@gmail.com", 
        password_hash="123456"
    )
    
    user2 = User(
        username="Oceana",
        email="gatamatos@gmail.com",
        password_hash="123456"
    )
    db.add(user2)
    db.commit()

    print(f"Usuário criado com ID {user.id}")

    db.close()

if __name__== "__main__":
    create_user()