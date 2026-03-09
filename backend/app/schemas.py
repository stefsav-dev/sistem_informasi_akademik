from pydantic import BaseModel, EmailStr
from typing import Optional, Literal
from datetime import datetime

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str

#auth schema
class UserCreate(BaseModel):
    email: str
    password: str
    role: Optional[Literal["mahasiswa", "dosen", "admin"]] = "mahasiswa"

class LoginSchema(BaseModel):
    email: str
    password: str

class LogoutSchema(BaseModel):
    refresh_token: str


#profile schema
class ProfileBase(BaseModel):
    full_name: str
    nim: Optional[str] = None
    nip: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    tanggal_lahir: Optional[datetime] = None


class ProfileCreate(ProfileBase):
    user_id: int

class ProfileUpdate(ProfileBase):
    pass

class ProfileResponse(ProfileBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class UserWithProfileResponse(BaseModel):
    id: int
    email: EmailStr
    role: str
    profile: Optional[ProfileResponse] = None

    class Config:
        from_attributes = True