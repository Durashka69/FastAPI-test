from typing import List

from fastapi import (
    APIRouter, Depends, status
)

from sqlalchemy.orm import Session

from blog.schemas import (
    ShowBlog, Blog, User
)
from blog.database import get_db
from blog.repository import blog
from blog.oauth2 import get_current_user


router = APIRouter(
    prefix='/blog',
    tags=['blogs']
)


@router.get('/', response_model=List[ShowBlog])
async def get_blogs(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
    ):
    return blog.get_all_blogs(db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=ShowBlog)
async def show_blog(
    id: int, 
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
    ):
    return blog.get_blog(id, db)


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_blog(
    request: Blog, 
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
    ):
    return blog.create_blog(request, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
async def update_blog(
    id: int, 
    request: Blog, 
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
    ):
    return blog.update_blog(id, request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy_blog(
    id: int, 
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
    ):
    return blog.delete_blog(id, db)
