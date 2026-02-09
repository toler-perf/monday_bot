from telebot import TeleBot
from telebot.types import Message


bot = TeleBot(
    '8522205710:AAHQK-KBxRgUyO-FIZoJNKTFgNzdfCdlDMM'
)


@bot.message_handler(commands=['hi'])
def hi(message: Message):
    chat = message.chat
    
    bot.send_message(chat_id=chat.id, text="HI")
    
    
@bot.message_handler(content_types=['text'])
def text(message: Message):
    if message.text == "Дурак":
        bot.restrict_chat_member(
            chat_id=message.chat.id, 
            user_id=message.from_user.id
        )
    
    
bot.infinity_polling()
