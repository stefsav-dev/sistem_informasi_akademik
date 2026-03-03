from pydantic import BaseModel
from typing import Optional, Literal

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str

class UserCreate(BaseModel):
    email: str
    password: str
    role: Optional[Literal["mahasiswa", "dosen", "admin"]] = "mahasiswa"

class LoginSchema(BaseModel):
    email: str
    password: str

class LogoutSchema(BaseModel):
    refresh_token: str