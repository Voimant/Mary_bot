from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from source.func_pandas import dela

main_menu_button = [
    [InlineKeyboardButton(text='👩🏽‍💻 Запись на консультация', callback_data='button_1')],
    [InlineKeyboardButton(text='⚖️ Моя специализация и опыт', callback_data='button_2')],
    [InlineKeyboardButton(text='🎖 Отзывы клиентов', callback_data='button_3')],
    [InlineKeyboardButton(text='💁🏽‍♀️ Советы от юриста', callback_data='mary_sovets')],
    [InlineKeyboardButton(text='⁉️ Задать открытый вопрос юристу', url='https://t.me/mara_mary_lawyer')],
    [InlineKeyboardButton(text='📲 Контакты', callback_data='contacts')],
    [InlineKeyboardButton(text='📲 Проверить организацию', callback_data='go_ddata')]
]

main_markup = InlineKeyboardMarkup(inline_keyboard=main_menu_button)


specialization_button = [
    [InlineKeyboardButton(text='Семейное право', callback_data='family'),
    InlineKeyboardButton(text='Арбитражные споры', callback_data='dispute')],
    [InlineKeyboardButton(text='Банкротство', callback_data='bankrupt'),
    InlineKeyboardButton(text='Интелектуальное право', callback_data='intel')],
    [InlineKeyboardButton(text='Корпоративное право', callback_data='corp'),
    InlineKeyboardButton(text='Ликвидация бизнеса', callback_data='licvid')],
    [InlineKeyboardButton(text='Назад', callback_data='cancel')]

]
spec_markup = InlineKeyboardMarkup(inline_keyboard=specialization_button)

cancel_button = [[InlineKeyboardButton(text="Главное меню", callback_data='cancel')]]
cancel_markup = InlineKeyboardMarkup(inline_keyboard=cancel_button)

contacts_button = [
    [InlineKeyboardButton(text='🌐VK', url='https://vk.com/platunova_lawyer')],
    [InlineKeyboardButton(text='📷instagram', url='https://instagram.com/platunova.mara?igshid=OGQ5ZDc2ODk2ZA==')],
    [InlineKeyboardButton(text='Назад', callback_data='cancel')]
]
contacts_markup = InlineKeyboardMarkup(inline_keyboard=contacts_button)

def dela_mark():

    builder = InlineKeyboardBuilder()
    for key, v in dela().items():
        builder.row(InlineKeyboardButton(text=str(key), url=str(v)))
    builder.row(InlineKeyboardButton(text=str('Назад'), callback_data='cancel'))
    builder.adjust(1)
    return builder


for k,v in dela().items():
    print(k + " ", v)