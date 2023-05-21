import telebot
import random
from telebot import types
import token

bot = telebot.TeleBot(token.TOKEN)

d = open('data/joke.txt', 'r', encoding='UTF-8')
joke = d.read().split('\n')
d.close()


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(button1)
    bot.send_message(message.from_user.id, "👋 Привет! Я твой бот-помощник!", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '👋 Поздороваться':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('погода')
        button2 = types.KeyboardButton('курс валют')
        button3 = types.KeyboardButton('новости')
        button4 = types.KeyboardButton('шутка')
        markup.add(button1, button2, button3, button4)
        bot.send_message(message.from_user.id, 'Что вы хотите узнать?', reply_markup=markup)


    elif message.text == 'погода':
        bot.send_message(message.from_user.id,
                         'Самый точный прогноз погоды - это посмотреть в окно😂.'
                         'Конечно же это небольшая шутка😂.'
                         'Посмотреть погодн вы можете по'
                         + '[ссылке](https://pogoda.by/)',
                         parse_mode='Markdown')

    elif message.text == 'курс валют':
        bot.send_message(message.from_user.id,
                         'Самый точный курс валют'
                         'по ' + '[ссылке](https://myfin.by/bank/kursy_valjut_nbrb)',
                         parse_mode='Markdown')

    elif message.text == 'новости':
        bot.send_message(message.from_user.id,
                         'По моему мнению самые свежие новости'
                         'по' + '[ссылке](https://people.onliner.by/)',
                         parse_mode='Markdown')

    elif message.text == 'шутка':
        answer = random.choice(joke)
        bot.send_message(message.chat.id, answer)

    else:
        bot.send_message(message.chat.id,
                         "Я еще не знаю это слово,"
                         "но я буду стараться выучить больше", parse_mode='html')


bot.polling(none_stop=True, interval=0)
