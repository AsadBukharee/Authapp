from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.database import get_db
from app.models.user import User
# from app.schemas.user import UserResponse
# from app.services.auth import get_current_user

users_router = APIRouter(
    prefix="/users",
    tags=["users"]
)


# @users_router.get("/me", response_model=UserResponse)
# async def get_me(current_user: User = Depends(get_current_user)):
#     return current_user
#
#
# @users_router.get("/{user_id}", response_model=UserResponse)
# async def get_user(user_id: int, db: AsyncSession = Depends(get_db)):
#     result = await db.execute(select(User).filter(User.id == user_id))
#     user = result.scalars().first()
#
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
#
#     return user
