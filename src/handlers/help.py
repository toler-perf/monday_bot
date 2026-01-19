from telebot import TeleBot
from telebot.types import Message


def register_help_handler(
    bot: TeleBot
) -> None:
    '''
    Регистрация обработчика команды help
    
    :param bot: Экзмпляр бота
    :type bot: TeleBot
    '''
    @bot.message_handler(commands=['help'])
    def help_handler(
        message: Message
    ) -> None:
        '''
        Обработчик команды help
        
        :param message: Сообщение пользователя
        :type message: Message
        '''
        user = message.from_user
        text = '''
Список всех доступных команд:

/start - запуск|перезапуск бота
/help - данное меню
        '''
        
        bot.send_message(
            chat_id=user.id,
            text=text
        )
        