from sqlalchemy.orm import Session
from models import User

def create_user(db: Session, username: str, email: str, password_hash: str):
    
    # Step 1: check username
    user_by_username = db.query(User).filter_by(username=username).first()

    # Step 2: check email
    user_by_email = db.query(User).filter_by(email=email).first()

    if user_by_username or user_by_email:
        return None

    user = User(
        username=username,
        email=email,
        password_hash=password_hash
    )

    db.add(user)
    db.commit()

    return user

def get_all_users(db: Session):
    