from fastapi import APIRouter, HTTPException, Depends, status, Path, Query

from sqlalchemy.ext.asyncio import AsyncSession
from src.database.db import get_db
from src.entity.models import User
from src.repository import todos as repositories_todos
from src.schemas.todo import TodoSchema, TodoUpdate, TodoResponse
from src.services.auth import auth_service

router = APIRouter(prefix='/todos', tags=['todos'])


@router.get('/', response_model=list[TodoResponse])
async def get_todos(limit: int = Query(10, ge=10, le=500), offset: int = Query(0, ge=0),
                    db: AsyncSession = Depends(get_db), user: User = Depends(auth_service.get_current_user)):
    todos = await repositories_todos.get_todos(limit, offset, db, user)
    return todos


# @router.get('/all', response_model=list[TodoResponse])
# async def get_todos(limit: int = Query(10, ge=10, le=500), offset: int = Query(0, ge=0),
#                     db: AsyncSession = Depends(get_db), user: User = Depends(auth_service.get_current_user)):
#     todos = await repositories_todos.get_all_todos(limit, offset, db)
#     return todos



@router.get('/{todo_id}', response_model=TodoResponse)
async def get_todo(todo_id: int, db: AsyncSession = Depends(get_db),
                   user: User = Depends(auth_service.get_current_user)):
    todo = await repositories_todos.get_todo(todo_id, db, user)
    if todo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Not found')
    return todo


@router.post('/', response_model=TodoResponse, status_code=status.HTTP_201_CREATED)
async def create_todo(body: TodoSchema, db: AsyncSession = Depends(get_db),
                      user: User = Depends(auth_service.get_current_user)):
    print('one')
    todo = await repositories_todos.create_todo(body, db, user)
    print('two')
    return todo



@router.put('/{todo_id}')
async def update_todo(body: TodoUpdate, todo_id: int = Path(ge=1), db: AsyncSession = Depends(get_db),
                      user: User = Depends(auth_service.get_current_user)):
    todo = await repositories_todos.update_todo(todo_id, body, db, user)
    if todo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='not found')
    return todo


@router.delete('/{todo_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(todo_id: int = Path(ge=1), db: AsyncSession = Depends(get_db),
                      user: User = Depends(auth_service.get_current_user)):
    todo = await repositories_todos.delete_todo(todo_id, db, user)
    return todo
