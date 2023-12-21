from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.types import Message
from keyboards.main_menu import spec_markup, cancel_markup, contacts_markup, dela_mark
import bot
from source.func_pandas import dela
from source.main_text import t_contacts
router = Router()


# @router.callback_query(F.data == 'button_2')
# async def get_specialization(call: types.CallbackQuery):
#     await call.message.answer('Мои специализации и опыт', reply_markup=spec_markup)

@router.callback_query(F.data =='button_2')
async def get_spec(call: types.CallbackQuery):
    await call.message.edit_text(text='Мои Специализации и опыт', inline_message_id=call.inline_message_id,
                                 reply_markup=spec_markup)


@router.callback_query(F.data=='button_3')
async  def get_otziv(call: types.CallbackQuery):
    await call.message.edit_text(text='Здесь будут жить отзывы клиентов', inline_message_id=call.inline_message_id,
                                 reply_markup=cancel_markup)

@router.callback_query(F.data=='contacts')
async def contacts(call: types.CallbackQuery):
    await call.message.edit_text(text=t_contacts, inline_message_id=call.inline_message_id,
                                 reply_markup=contacts_markup)


@router.callback_query(F.data == 'dispute')
async def dispute(call: types.CallbackQuery):
    await call.message.answer(text='Вы можете ознакомиться с делами', reply_markup=dela_mark().as_markup())

# @router.callback_query(F.data == 'dispute')
# async def dispute(call: types.CallbackQuery):
#     text = ''
#     for key, val in dela().items():
#         text += f'{key}\n {val}\n '
#     await call.message.answer(text='Вы можете ознакомиться с делами',)
#     await call.message.answer(text=text)