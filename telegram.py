#~ USAGE
# cd c:\python_developer
# cd d:\python_developer
# .\pydev\Scripts\activate
# cd c:\python_developer\python_developer_lesson15
# cd d:\python_developer\python_developer_lesson15
#~~~~~~~~~~~~~~~~~~~~~~~~
# python telegram.py
#~~~~~~~~~~~~~~~~~~~~~~~~


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from os import getenv
from os.path import exists

#~ библиотека для загрузки данных из env
# from dotenv import load_dotenv
import dotenv
import telebot

# файл для парсинга данных
from digital import parce

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ метод ищет файл env и переменные из него
# load_dotenv()

#~ достает из файла переменную token
# token = getenv('token')
token = dotenv.get_variable('.env','token')
# print(f'token: `{token}`')
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
  text = message.text.split()[1]
  bot.reply_to(message, text[::-1])


@bot.message_handler(commands=['parse'])
def parse_site(message):
  text = message.text.split()[1]
  chat_id = message.chat.id
  q = parce(text)
  for it in q[:20]:
    bot.send_message(chat_id, f'{it[0]} - {it[1]}')


@bot.message_handler(commands=['file'])
def send_file(message):
  chat_id = message.chat.id
  print(f'chat_id: `{chat_id}`')
  if exists('base.csv'):
    print('base.csv сформирован, отправляю в бот')
    with open('base.csv', encoding='utf-8') as f:
      bot.send_document(chat_id, f)
  else:
    bot.send_message(chat_id, 'Файл не сформирован. Используйте команду /parce для его формирования')


@bot.message_handler(func=lambda m: True)
def echo(message):
  print(message)
  bot.reply_to(message, message.text.upper())


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
bot.infinity_polling()
