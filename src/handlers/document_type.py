from telebot import TeleBot
from telebot.types import Message

from services.parsing_files import parsing_documents


def register_document_type(
    bot: TeleBot
) -> None:
    @bot.message_handler(content_types=["document"])
    def document_type(
        message: Message
    ) -> None:
        '''
        Docstring для document_type
        
        :param message: Описание
        :type message: Message
        '''
        user = message.from_user
        
        parsing_documents(bot, message)
        
        bot.send_message(
            chat_id=user.id,
            text="Документ был скачан!"
        )
    