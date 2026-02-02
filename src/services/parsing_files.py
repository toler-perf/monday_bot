from telebot import TeleBot
from telebot.types import Message


path = "src/sources/"


def parsing_documents(
    bot: TeleBot,
    message: Message
) -> None:
    file = message.document
    file_path = path + file.file_name
    
    data = bot.get_file(file.file_id)   # Информация для скачивания
    downloaded_file = bot.download_file(data.file_path) # Информация из самого файла
    
    new_file = open(file_path, mode="wb")
    new_file.write(downloaded_file)
    new_file.close()
