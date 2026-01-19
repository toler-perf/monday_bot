from telebot import TeleBot
from telebot.types import Message

token = '8522205710:AAHQK-KBxRgUyO-FIZoJNKTFgNzdfCdlDMM'
bot = TeleBot(
    token=token
)


@bot.message_handler(content_types=['text'])
def text_handler(
    message: Message
):
    user = message.from_user
    
    bot.send_message(
        chat_id=user.id,
        text=message.text[::-1]
    )


if __name__ == '__main__':
    print('Бот запущен...')
    bot.infinity_polling()
    