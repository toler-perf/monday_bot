from telebot import TeleBot

from config import settings
from handlers.start import register_start_handler
from handlers.help import register_help_handler

def main() -> None:
    '''
    Функция запуска бота и регистрации обработчиков
    '''
    bot = TeleBot(
        token=settings.BOT_TOKEN
    )
    
    # Регистрация всех обработчиков
    register_start_handler(bot)
    register_help_handler(bot)
    
    print('Бот запущен...')
    bot.infinity_polling()
    
    
if __name__ == '__main__':
    main()
    