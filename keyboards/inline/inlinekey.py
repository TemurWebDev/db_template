from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

til = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🇺🇿 uz',callback_data='uz'),
            InlineKeyboardButton(text='🇺🇸 eng',callback_data='en'),
            InlineKeyboardButton(text='🇷🇺 ru',callback_data='ru')
        ],
    ]
)