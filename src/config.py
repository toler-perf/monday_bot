from dotenv import load_dotenv
from os import getenv


load_dotenv()


class Config:
    def __init__(self):
        self.BOT_TOKEN = getenv('BOT_TOKEN')


settings = Config()
