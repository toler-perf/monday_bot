from telebot import TeleBot
from telebot.types import Message


blacklist_words = ['дурак', 'черт', 'c++', 'qwerty']


def register_text_type(
    bot: TeleBot
) -> None:
    @bot.message_handler(content_types=["text"])
    def text_type(
        message: Message
    ) -> None:
        chat = message.chat
        user = message.from_user
        
        text_msg = message.text.lower()
        
        for word in blacklist_words:
            if word in text_msg:
                bot.restrict_chat_member(
                    chat_id=chat.id,
                    user_id=user.id
                )
                text = f'Пользователь: {user.username} отправил одно из запрещенных слов'
                bot.send_message(
                    chat_id=chat.id, 
                    text=text
                )
                break
        