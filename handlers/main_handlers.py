from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from source.main_text import main_texts
from keyboards.main_menu import main_markup
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import State, StatesGroup

from source.test_api import test_api

router = Router()

@router.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer(main_texts, reply_markup=main_markup)

@router.callback_query(F.data == 'cancel')
async def cancel(call: CallbackQuery):
    await call.message.edit_text('Вы вернулись в главное меню', inline_message_id=call.inline_message_id,
                                 reply_markup=main_markup)


class Fsdata(StatesGroup):
    inn = State()

@router.callback_query(F.data == 'go_ddata')
async def get_data(call: CallbackQuery, state: FSMContext):
    await call.message.answer('Введите ИНН организации')
    await state.set_state(Fsdata.inn)

@router.message(Fsdata.inn)
async def final_data(mess: Message, state: FSMContext):
    try:
        await state.update_data(inn=mess.text)
        data = await state.get_data()
        x = test_api(data['inn'])
        await mess.answer(x)
    except Exception as e:
        await mess.answer('Что то пошло не так, нужно проверить правильность ввода ИНН', reply_markup=main_markup)