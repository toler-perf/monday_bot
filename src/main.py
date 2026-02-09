from telebot import TeleBot

from config import settings
from handlers.check_age import register_check_age_handler
from handlers.document_type import register_document_type
from handlers.media import register_media_handler
from handlers.start import register_start_handler
from handlers.help import register_help_handler
from handlers.text_type import register_text_type

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
    register_media_handler(bot)
    register_check_age_handler(bot)
    register_document_type(bot)
    register_text_type(bot)
    
    print('Бот запущен...')
    bot.infinity_polling()
    
    
if __name__ == '__main__':
    main()
    