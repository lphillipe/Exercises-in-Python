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
    