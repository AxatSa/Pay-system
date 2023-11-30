from fastapi import APIRouter
from datetime import datetime
from database.cardservice import (add_card_db, delete_card, get_exact_card_db,
                                  get_exact_user_cards_db, get_check_card_info_db)

from cart import CardAddValidator, CardDeleteValidator

card_router = APIRouter(prefix='/card', tags=['Работа с картами'])


@card_router.post('/register-card')
async def register_card(data: CardAddValidator):
    new_card_data = data.model_dump()

    checker = add_card_db(data.user_id)

    if checker:
        add_card_db(reg_date=datetime.now(), **new_card_data)
    else:
        return {'message': 'Карта уже есть'}


@card_router.delete('/delete-card')
async def delete_card(card: int):
    result = delete_card_db(card_id)

    if result:
        return {'message': result}
    else:
        return {'message': 'Карта не найдена'}


@card_router.get('/info-user-card')
async def get_exact_user_cards(card_id: int):
    result = get_exact_user_cards_db(card_id)

    if result:
        return {'message': result}
    else:
        return {'message': 'Такой карты нету'}


@card_router.get('/info-card')
async def get_card(card_id: int):
    result = get_exact_card_db(user_id)

    if result:
        return {'message': result}
    else:
        return {'message': 'Такой карты нету'}
