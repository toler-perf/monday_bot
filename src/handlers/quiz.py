import random

from telebot import TeleBot
from telebot.types import Message


question = ["Сколько сейчас время?\n1."]
aswers = {"Сколько сейчас время?\n1.": "1"}

score = 0
prev_ans = 0


def register_quiz(
    bot: TeleBot
) -> None:    
    @bot.message_handler(commands=["quiz"])
    def quiz(message: Message):
        global prev_ans
        user = message.from_user
        
        if message.text != '/quiz':
            if message.text == prev_ans:
                score += 1
        
        if len(quest) == 0:
            pass    # Отправка итогового счета
        else:
            quest = random.choice(question)
            question.remove(quest)
            
            prev_ans = aswers[quest]
            
            msg = bot.send_message(
                chat_id=user.id,
                text=quest
            )
            
            bot.register_next_step_handler(msg, quiz)
            
        