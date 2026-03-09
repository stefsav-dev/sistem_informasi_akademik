# app/main.py

from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.database.database import Base, engine
from app.controller.dependencies import get_db, require_role
from app.models.models import User
from app.schemas import UserCreate
from app.auth.auth import *
from app.schemas import LoginSchema
from app.schemas import LogoutSchema
from app.controller import profile_controller


app = FastAPI()

app.include_router(profile_controller.router)

@app.get("/")
def index():
    return {"message": "Hello World"}

Base.metadata.create_all(bind=engine)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

@app.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    hashed_password = hash_password(user.password)
    

    new_user = User(
        email=user.email,
        password=hashed_password,
        role=user.role
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User created"}


@app.post("/login")
def login(data: LoginSchema, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.email == data.email).first()

    if not user or not verify_password(data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token({
        "sub": user.email,
        "role": user.role
    })

    refresh_token = create_refresh_token({
        "sub": user.email,
        "role": user.role
    })

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }


@app.post("/refresh")
def refresh(token: str):
    payload = verify_token(token, "refresh")
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid refresh token")

    new_access_token = create_access_token({
        "sub": payload["sub"],
        "role": payload["role"]
    })

    return {"access_token": new_access_token}

@app.get("/admin")
def admin_route(user=Depends(require_role(["admin"]))):
    return {"message": "Welcome Admin"}

@app.get("/dosen")
def dosen_route(user=Depends(require_role(["dosen", "admin"]))):
    return {"message": "Welcome Dosen"}

@app.get("/mahasiswa")
def mahasiswa_route(user=Depends(require_role(["mahasiswa"]))):
    return {"message": "Welcome Mahasiswa"}

@app.post("/logout")
def logout(
    data: LogoutSchema,
    access_token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    refresh_token = data.refresh_token

    refresh_payload = verify_token(refresh_token, "refresh")
    if not refresh_payload:
        raise HTTPException(status_code=401, detail="Invalid refresh token")

    access_payload = verify_token(access_token, "access")
    if not access_payload:
        raise HTTPException(status_code=401, detail="Invalid access token")

    db.add(TokenBlacklist(token=refresh_token))
    db.add(TokenBlacklist(token=access_token))
    db.commit()

    return {"message": "Logout successful"}

