from aiogram import Bot, types
from aiogram.types import Message
from core.keyboards.reply import reply_keyboard
from aiogram.types import WebAppInfo

async def get_start(message: Message, bot: Bot):
    await message.answer(f'Приветствую Вас, <b>{message.from_user.first_name}</b>.\n\nБлагодаря этому боту вы можете создавать посты на своем сайте.\n\nНажмите на кнопку <b>меню</b>, чтобы увидеть список команд.')


async def descr_command(message: Message, bot: Bot):
    await message.answer('Благодаря этому боту вы можете размещать на сайте посты, фотографии, менять темы и оформление.') 


async def your_site_command(message: Message, bot: Bot):
    text = 'web-app'
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Launch web-app', web_app=WebAppInfo(url='https://c0d0-109-111-146-53.ngrok-free.app/')))
    await bot.send_message(message.chat.id, text, reply_markup=keyboard)

   