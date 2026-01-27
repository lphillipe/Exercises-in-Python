from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from database import engine, Base, get_db
import crud
import schemas
import security


#Create tables

Base.metadata.create_all(bind=engine)

app = FastAPI(title="User Management API")

# Endpoint POST Create USERS
@app.post("/users", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    created_user = crud.create_user(
        db,
        username=user.username,
        email=user.email,
        password=user.password
    )

    if not created_user:
        raise HTTPException(status_code=400, detail="Username or email already exists")
    
    return created_user

# Endpoint GET List users
@app.get("/users", response_model=list[schemas.UserResponse])
def list_users(db: Session = Depends(get_db)):
    return crud.get_all_users(db)

# Endpoint GET Search by ID
@app.get("/users/{user_id}", response_model=schemas.UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user_by_id(db, user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
        
    return user

@app.put("/users/{user_id}/username", response_model=schemas.UserResponse)
def update_username(user_ind: int, username: str, db: Session = Depends(get_db)):
    user = crud.update_user_username(db, user_id, username)

    if not user:
        raise HTTPException(status_code=400, detail="Not possible to update")

    return user

@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_user_by_id(db, user_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")

    return {"message": "User found successfully"}

@app.post("/login")
def login(data: schemas.LoginData, db: Session = Depends(get_db)):
    user = crud.authenticate_user(db, data.email, data.password)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid Credentials")

    token = security.create_access_token(
        data={"sub": str(user.id)}
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }