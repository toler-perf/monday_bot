from telebot import TeleBot
from telebot.types import Message


def register_start_handler(
    bot: TeleBot
) -> None:
    '''
    Регистрация обработчика команды start
    
    :param bot: Экземпляр бота
    :type bot: TeleBot
    '''
    @bot.message_handler(commands=['start'])
    def start_handler(
        message: Message
    ) -> None:
        '''
        Обработчик команды start
        
        :param message: Сообщение пользователя
        :type message: Message
        '''
        user = message.from_user
        text = """Привет ученик Matrix, на примере меня Егор объясняет различные возможности разработки тг ботов"""
        
        bot.send_message(
            chat_id=user.id,
            text=text
        )
        