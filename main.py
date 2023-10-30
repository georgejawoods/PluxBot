import requests
import random
from bs4 import BeautifulSoup as bs
from aiogram import Bot, Dispatcher, executor, types
import os

API_TOKEN = os.environ.get("API_TOKEN", "")

URL = 'https://www.anekdot.ru/last/'
def parser(url):
    r = requests.get(url)
    soup = bs(r.text, 'html.parser')
    anekdots = soup.find_all('div', class_='text')
    return [c.text for c in anekdots]

list_of_jokes = parser(URL)
random.shuffle(list_of_jokes)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    #This handler will be called when user sends `/start` or `/help` command
    
    await message.reply("Клоун на месте!")

@dp.message_handler(lambda message: message.text == 'Анекдот')
async def anekdot(message: types.Message):
    await message.reply(list_of_jokes[0])
    del list_of_jokes[0]

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)