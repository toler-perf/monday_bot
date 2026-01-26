from telebot import TeleBot
from telebot.types import Message


def register_media_handler(
    bot: TeleBot
) -> None:
    '''
    Регистрация обработчика команды media
    
    :param bot: Экземпляр бота
    :type bot: TeleBot
    '''
    @bot.message_handler(commands=['media'])
    def media_handler(
        message: Message
    ) -> None:
        '''
        Обработчик команды media
        
        :param message: Сообщение пользователя
        :type message: Message
        '''
        user = message.from_user
        path = 'src/sources/'
        
        animated_sticker = open(file=path+'AnimatedSticker.tgs', mode='rb')
        audio = open(file=path+'audio.mp3', mode='rb')
        document = open(file=path+'document.txt', mode='rb')
        image = open(file=path+'image.jpg', mode='rb')
        sticker = open(file=path+'sticker.webp', mode='rb')
        video = open(file=path+'video.mp4', mode='rb')
        
        #bot.send_sticker(chat_id=user.id, sticker=animated_sticker)
        #bot.send_audio(chat_id=user.id, audio=audio)
        #bot.send_document(chat_id=user.id, document=document)
        bot.send_photo(chat_id=user.id, photo=image)
        #bot.send_sticker(chat_id=user.id, sticker=sticker)
        #bot.send_video(chat_id=user.id, video=video)
        