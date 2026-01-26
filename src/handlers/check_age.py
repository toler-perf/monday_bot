from telebot import TeleBot
from telebot.types import Message


def register_check_age_handler(
    bot: TeleBot
) -> None:
    '''
    Регистрация обработчика команды check_age
    
    :param bot: Экзмпляр бота
    :type bot: TeleBot
    '''
    @bot.message_handler(commands=['check_age'])
    def check_age_handler(
        message: Message
    ) -> None:
        '''
        Обработчик команды check_age
        
        :param message: Сообщение пользователя
        :type message: Message
        '''
        user = message.from_user
        
        text = 'Ввведите свой возраст'
        
        msg = bot.send_message(
            chat_id=user.id,
            text=text
        )
        bot.register_next_step_handler(
            message=msg,
            callback=second_step
        )
        
    def second_step(
        message: Message
    ) -> None:
        user = message.from_user
        age = int(message.text)
        
        if age >= 18:
            text = 'Взорслый'
        else:
            text = 'Маленький'
            
        bot.send_message(
            chat_id=user.id,
            text=text
        )
        