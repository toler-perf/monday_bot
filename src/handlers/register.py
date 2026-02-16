from telebot import TeleBot
from telebot.types import Message

NAME = ''
AGE = ''
GEN = ''


def register_date(bot: TeleBot) -> None:
    @bot.message_handler(commands=['register'])
    def date(message: Message):
        user = message.from_user
        text = 'Имя: '
        
        message = bot.send_message(user.id, text)        #type: ignore
        
        bot.register_next_step_handler(message, second_step)
        
    def second_step(message: Message):
        global NAME
        NAME = message.text
        
        user = message.from_user
        text = 'Возраст: '
        
        message = bot.send_message(user.id, text)      #type: ignore  
        
        bot.register_next_step_handler(message, third_step)

        
    def third_step(message: Message):
        global AGE
        AGE = message.text
        
        user = message.from_user
        text = 'Пол: '
        
        message = bot.send_message(user.id, text)      #type: ignore
        
        bot.register_next_step_handler(message, fourth_step)

        
    def fourth_step(message: Message):
        global GEN
        GEN = message.text
        
        user = message.from_user
        text = f'Вы зарегестрированы\nИнформация:\nИмя: {NAME}\nВозраст: {AGE}\nПол: {GEN}'
        
        bot.send_message(user.id, text)  #type: ignore