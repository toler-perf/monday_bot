from telebot import TeleBot
from telebot.types import Message

token = '8522205710:AAHQK-KBxRgUyO-FIZoJNKTFgNzdfCdlDMM'
bot = TeleBot(
    token=token
)


@bot.message_handler(commands=["docx"])
def docx(
    message: Message
) -> None:
    user = message.from_user
    
    file_path = "bots/lession 2026-02-02/ДЗ.txt"
    file = open(file_path, mode="r", encoding="utf-8")
    
    text = file.read()
    
    file.close()
    
    bot.send_message(
        chat_id=user.id,
        text=text
    )
    
    
if __name__ == "__main__":
    bot.infinity_polling()
    