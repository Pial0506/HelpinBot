from aiogram import Router, F
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from app.database.requests import set_user, update_user
import app.keyboards as kb

router = Router()


class Reg(StatesGroup):
    name = State()
    contact = State()


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    user = await set_user(message.from_user.id)
    if user:
        await message.answer(f'Доброго времени суток, {user.name}', reply_markup=kb.main)
        await state.clear()
    else:
        await message.answer('Добро пожаловать! Пожалуйста пройдите регистрацию.\n\nВведите Вашу фамилию')
        await state.set_state(Reg.name)


@router.message(Reg.name)
async def reg_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Reg.contact)
    await message.answer('Отправьте номер  телефона', reply_markup=kb.contact)


@router.message(Reg.contact, F.contact)
async def reg_contact(message: Message, state: FSMContext):
    data = await state.get_data()
    await update_user(message.from_user.id, data['name'], message.contact.phone_number)
    await state.clear()
    await message.answer(f'Опишите свою проблему.', reply_markup=kb.main)


