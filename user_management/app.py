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
    user1 = create_user(db, "joaquim", "joaquim@gmail.com", "123")
    user2 = create_user(db, "maria", "maria@gmail.com", "123")
    user3 = create_iser(db, "joaquim", "duplicado@gmail.com", "123")

    print(user1)
    print(user2)
    print(user3)

    #Testing READ

    print("\n Todos os usuários:")
    users = get_all_users(db)
    for u in users:
        print(u.id, u.username, u.email)

    print("\n Buscar por ID:")
    print(get_user_by_id(db, 1))

    print("\n Buscar por username:")
    print(get_user_by_username(db, "maria"))

    # Testing UPDATE

    print("\n✏️ Atualizando username:")
    updated = update_user_username(db, 1, "joaquim_novo")
    print(updated.username if updated else "Erro no update")

    print("\n✏️ Atualizando email:")
    updated = update_user_email(db, 2, "maria_nova@gmail.com")
    print(updated.email if updated else "Erro no update")

    

    