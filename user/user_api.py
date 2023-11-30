from fastapi import APIRouter
from datetime import datetime
from database.userservice import (check_user_email_db, register_user_db, delete_user_db,
                                  get_all_user_db, get_exact_user_db)

from user import UserRegisterValidator

user_router = APIRouter(prefix='/user', tags=['Работа с юзерами'])


@user_router.post('/register')
async def register_user(data: UserRegisterValidator):
    new_user_data = data.model_dump()

    checker = check_user_email_db(data.email)
    # prevroshaem v sliver
    if checker:
        result = register_user_db(reg_date=datetime.now(), **new_user_data)
        return {'message': result}
    else:
        return {'message': 'Пользователь уже есть'}


@user_router.get('/info')
async def get_user(user_id: int):
    result = get_exact_user_db(user_id)

    if result:
        return {'message': result}
    else:
        return {'message': 'Такого пользователя нету. Иди зарегайся'}


@user_router.delete('/delete-user')
async def delete_user(user_id: int):
    result = delete_user_db(user_id)

    if result:
        return {'message': result}

    else:
        return {'message': 'Пользователь не найден'}


@user_router.get('/get-all-user')
async def get_all_user():
    test = get_all_user_db()

    return test
