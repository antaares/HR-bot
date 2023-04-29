from aiogram import types

from keyboards.inline.language_keyboard import language_keyboard
from loader import dp
from messages.funcs.get_language import get_language
from messages.message_txt.message_text import *


@dp.message_handler(text=["🇺🇿 Tilni o'zgartirish","🇷🇺 Изменить язык"])
async def reg_to_bot(message: types.Message):
    language = await get_language(user_id=message.from_user.id)
    await message.answer(change_language_txt[language],
                         reply_markup= language_keyboard)




