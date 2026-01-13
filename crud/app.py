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

    user3 = User(
        username="João",
        email="joaozinho@gmail.com",
        password_hash="123456"
    )

    user4 = User(
        username="Francisco",
        email="joaozinho@gmail.com",
        password_hash="123456"
    )
    db.add(user4)
    db.commit()

    print(f"Usuário criado com ID {user4.id}")

    db.close()

if __name__== "__main__":
    create_user()