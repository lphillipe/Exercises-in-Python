from sqlalchemy.orm import Session
from models import User


#Function Create

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

#Function Read
def get_all_users(db: Session):
    users = db.query(User).all()
    return users

def get_user_by_id(db: Session, user_id: int):
    user = db.query(User).filter_by(id=user_id).first()
    return user

def get_user_by_username(db: Session, username: str):
    user = db.query(User).filter_by(username=username).first()
    return user

#Function Update

def update_user_email(db: Session, user_id: int, new_email: str):
    user = db.query(User).filter_by(id=user_id).first()

    if user is None:
        return None

    email_exists = db.query(User).filter_by(email=new_email).first()

    if email_exists:
        return None

    user.email = new_email

    db.commit()

    return user


    
