from telebot import TeleBot
from telebot.types import Message

token = '8522205710:AAHQK-KBxRgUyO-FIZoJNKTFgNzdfCdlDMM'
bot = TeleBot(
    token=token
)


@bot.message_handler(commands=['start'])
def start_handler(
    message: Message
) -> None:
    user = message.from_user
    text = """Привет ученик Matrix, на примере меня Егор объясняет различные возможности разработки тг ботов"""
    
    bot.send_message(
        chat_id=user.id,
        text=text
    )


@bot.message_handler(commands=["sticker"])
def sticker_handler(
    message: Message
) -> None:
    user = message.from_user
    
    sticker = open(file='bots/lession 2026-01-26/sticker.webp', mode='rb')
    bot.send_sticker(
        chat_id=user.id,
        sticker=sticker
    )


@bot.message_handler(commands=["animsticker"])
def sticker_handler(
    message: Message
) -> None:
    user = message.from_user
    
    sticker = open(file='src/sources/AnimatedSticker.tgs', mode='rb')
    bot.send_sticker(
        chat_id=user.id,
        sticker=sticker
    )


@bot.message_handler(content_types=["photo"])
def photo_handler(
    message: Message
) -> None:
    user = message.from_user
    photo_id = message.photo[-1].file_id
    
    bot.send_message(
        chat_id=user.id,
        text=photo_id
    )
    bot.send_photo(
        chat_id=user.id,
        photo=photo_id
    )

if __name__ == '__main__':
    print('Бот запущен...')
    bot.infinity_polling()
    