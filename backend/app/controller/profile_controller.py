from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database.database import get_db
from app.models.models import User, Profile
from app.schemas import ProfileCreate, ProfileUpdate, ProfileResponse, UserWithProfileResponse
from app.auth.auth import get_current_user
from app.controller.dependencies import require_role

router = APIRouter(prefix="/profile", tags=["Profile"])

# Endpoint untuk membuat profile (hanya untuk user yang sudah login)
@router.post("/create", response_model=ProfileResponse, status_code=status.HTTP_201_CREATED)
def create_profile(
    profile: ProfileCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Cek apakah user sudah punya profile
    existing_profile = db.query(Profile).filter(Profile.user_id == current_user.id).first()
    if existing_profile:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already has a profile"
        )
    
    # Validasi berdasarkan role
    if current_user.role == "mahasiswa" and not profile.nim:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="NIM is required for mahasiswa"
        )
    elif current_user.role == "dosen" and not profile.nip:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="NIP is required for dosen"
        )
    
    # Buat profile baru
    new_profile = Profile(
        **profile.dict(),
        user_id=current_user.id
    )
    
    db.add(new_profile)
    db.commit()
    db.refresh(new_profile)
    
    return new_profile

# Endpoint untuk get profile mahasiswa yang sedang login
@router.get("/mahasiswa/me", response_model=UserWithProfileResponse)
def get_my_mahasiswa_profile(
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(["mahasiswa"]))
):
    # Load profile dengan join
    user_with_profile = db.query(User).filter(User.id == current_user.id).first()
    
    if not user_with_profile.profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profile not found for this mahasiswa"
        )
    
    return user_with_profile

# Endpoint untuk get profile mahasiswa by ID (untuk admin/dosen)
@router.get("/mahasiswa/{user_id}", response_model=UserWithProfileResponse)
def get_mahasiswa_profile_by_id(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(["admin", "dosen"]))
):
    user = db.query(User).filter(
        User.id == user_id,
        User.role == "mahasiswa"
    ).first()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Mahasiswa not found"
        )
    
    if not user.profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profile not found for this mahasiswa"
        )
    
    return user

# Endpoint untuk get all mahasiswa dengan profile (untuk admin/dosen)
@router.get("/mahasiswa", response_model=List[UserWithProfileResponse])
def get_all_mahasiswa_profiles(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(["admin", "dosen"]))
):
    mahasiswa = db.query(User).filter(
        User.role == "mahasiswa"
    ).offset(skip).limit(limit).all()
    
    return mahasiswa

# Endpoint untuk update profile
@router.put("/update", response_model=ProfileResponse)
def update_profile(
    profile_update: ProfileUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    profile = db.query(Profile).filter(Profile.user_id == current_user.id).first()
    
    if not profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profile not found"
        )
    
    # Update profile
    for key, value in profile_update.dict(exclude_unset=True).items():
        setattr(profile, key, value)
    
    db.commit()
    db.refresh(profile)
    
    return profile

# Endpoint untuk delete profile
@router.delete("/delete", status_code=status.HTTP_204_NO_CONTENT)
def delete_profile(
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(["admin"]))
):
    profile = db.query(Profile).filter(Profile.user_id == current_user.id).first()
    
    if not profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profile not found"
        )
    
    db.delete(profile)
    db.commit()
    
    return None