from telebot import TeleBot
from telebot.types import Message

token = '8522205710:AAHQK-KBxRgUyO-FIZoJNKTFgNzdfCdlDMM'
bot = TeleBot(
    token=token,
    parse_mode="MarkdownV2"
)

@bot.message_handler(content_types=["text"])
def text(msg: Message):
    user = msg.from_user
    text = msg.text
    
    bot.send_message(user.id, f"{text}")        # обычный
    bot.send_message(user.id, f"*{text}*")      # жирный
    bot.send_message(user.id, f"_{text}_")      # курсив
    bot.send_message(user.id, f"`{text}`")      # моноширный
    bot.send_message(user.id, f"~~~{text}~~~")  # зачеркнутый
    bot.send_message(user.id, f"__{text}__")    # подчеркнутый
    
    
bot.infinity_polling()
    
    
