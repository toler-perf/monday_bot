# Reply клавиатуры
from telebot import TeleBot
from telebot.types import Message, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


bot = TeleBot("8522205710:AAHQK-KBxRgUyO-FIZoJNKTFgNzdfCdlDMM")


@bot.message_handler(commands=['start'])
def start(message: Message):
    user = message.from_user
    
    markup = ReplyKeyboardMarkup(
        row_width=1,    # Данный аргумент указывает на то, сколько будет кнопок в одном ряду
        one_time_keyboard=True,  # Будет ли закрываться клавиатура после использования
        resize_keyboard=True    # Указывает на нормальные разимеры для кнопок
    ) # Создание клавиатуры
    
    btn1 = KeyboardButton("Кнопка 1")
    btn2 = KeyboardButton("Кнопка 2")
    markup.add(btn1, btn2)
    
    text = "Привет"
    
    msg = bot.send_message(
        chat_id=user.id,
        text=text,
        reply_markup=markup
    )
    
    bot.register_next_step_handler(msg, answer)
    
def answer(message: Message):
    user = message.from_user
    text = "Привет"
    
    bot.send_message(
        chat_id=user.id,
        text=text,
        reply_markup=ReplyKeyboardRemove()
    )


bot.infinity_polling()