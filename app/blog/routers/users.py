from fastapi import (
    APIRouter, Depends, status
)

from typing import List

from sqlalchemy.orm import Session

from blog.schemas import ShowUser, User
from blog.database import get_db
from blog.repository import user


router = APIRouter(
    prefix='/users',
    tags=['users']
)


@router.get('/', response_model=List[ShowUser])
async def get_users(db: Session = Depends(get_db)):
    return user.get_all_users(db)


@router.get('/{id}',status_code=status.HTTP_200_OK,response_model=ShowUser,)
async def get_user(id: int, db: Session = Depends(get_db)):
    return user.get_user(id, db)


@router.post('/', response_model=ShowUser)
async def create_user(request: User,db: Session = Depends(get_db)):
    return user.create_user(request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy_user(id, db: Session = Depends(get_db)):
    return user.delete_user(id, db)
