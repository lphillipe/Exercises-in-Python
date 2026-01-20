from database import engine, SessionLocal, Base
from crud import (
    create_user,
    get_all_users,
    get_user_by_id,
    update_user_username,
    update_user_email,
    delete_user_by_id,
    delete_user_by_username
)

def create_tables():
    Base.metadata.create_all(bind=engine)

def main():
    db = SessionLocal()

    #Testing CREATE
    user1 = create_user(db, "Joaquim", "joaquim@gmail.com", "123")
    user2 = create_user(db, "Maria", "maria@gmail.com", "123")
    user3 = create_iser(db, "Joaquim", "duplicado@gmail.com", "123")

    print(user1)
    print(user2)
    print(user3)
    