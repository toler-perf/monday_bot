from telebot import TeleBot
from telebot.types import Message


bot = TeleBot("8522205710:AAHQK-KBxRgUyO-FIZoJNKTFgNzdfCdlDMM")


@bot.message_handler(commands=['start'])
def start(message: Message):
    user = message.from_user
    text = "Введите свое имя: "
    
    msg = bot.send_message(chat_id=user.id, text=text)
    bot.register_next_step_handler(msg, step2)
    

def step2(message: Message):
    user = message.from_user
    text = "Приятно познакомится"
    
    bot.send_message(chat_id=user.id, text=text)
    
bot.infinity_polling()