from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.database import get_db
from app.models.user import User
# from app.schemas.user import UserCreate, UserResponse
# from app.services.auth import authenticate_user, create_access_token, get_password_hash

auth_router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

#
# @auth_router.post("/register", response_model=UserResponse)
# async def register_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
#     # Check if the user already exists
#     result = await db.execute(select(User).filter(User.email == user.email))
#     existing_user = result.scalars().first()
#
#     if existing_user:
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
#
#     # Create new user
#     hashed_password = get_password_hash(user.password)
#     new_user = User(email=user.email, hashed_password=hashed_password)
#     db.add(new_user)
#     await db.commit()
#     await db.refresh(new_user)
#
#     return new_user
#
#
# @auth_router.post("/login")
# async def login_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
#     # Authenticate the user
#     db_user = await authenticate_user(db, user.email, user.password)
#     if not db_user:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
#
#     # Create JWT token
#     access_token = create_access_token(data={"sub": db_user.email})
#
#     return {"access_token": access_token, "token_type": "bearer"}
