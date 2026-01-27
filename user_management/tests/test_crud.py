from app.crud import create_user, authenticate_user

def test_create_user_success(db):
    user = create_user(
        db,
        username="joao",
        email="joao@gmail.com",
        password="123"
    )

    assert user is not None
    assert user.id is not None
    assert user.username == "joao"

def test_create_user_duplicate_email(db):
    create_user(db, "joao", "joao@gmail.com", "123")
    user = create_user(db, "maria", "joao@gmail.com", "123")
    
    assert user is None

def test_authenticate_user_success(db):
    create_user(db, "joao", "joao@gmail.com", "123")
    user = authenticate_user(db, "joao@gmail.com", "123")

    assert user is not None

def test_authenticate_user_wrong_password(db):
    create_user(db, "joao", "joao@gmail.com", "123")

    user = authenticate_user(db, "joao@gmail.com", "wrong")

    assert user is None