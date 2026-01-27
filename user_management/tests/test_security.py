from security import hash_password, verify_password


def test_hash_and_verify_password():
    password = "123456"

    hashed = hash_password(password)

    assert hashed != password
    assert verify_password(password, hashed) is True
    assert verify_password("wrong_password", hashed) is False