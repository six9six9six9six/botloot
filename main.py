import requests as rq
import json
import telebot
from operator import itemgetter
from time import sleep

token = 'TOKEN'
bot = telebot.TeleBot(token, parse_mode='html')

#отслеживаем команду /help
#отсылаем гифку


@bot.message_handler(commands=['help'])

def start(message):
    
	bot.send_animation(message.chat.id, r'https://dota2.ru/img/memes/2022/04/74262.gif')

#отслеживаем команду /start, отправляем приветствие.
@bot.message_handler(commands=['start'])

def start1(message):
    
    bot.reply_to(message, 'Привет Гуленыш!🤡')

#отслеживаем команду /percent.
#принимаем два числа, проверяем являются ли они числами, и производим вычисления профита.
@bot.message_handler(commands=['percent'])

def percent(message):
    
    split_message = message.text.split()
    
    try:
        split_message[0] == '/percent' and split_message[1].isdigit() and split_message[2].isdigit()
        buy = float(split_message[1])
        sell = float(split_message[2])
        x = (buy - sell) * 100 / -buy
        bot.reply_to(message, f'Buy price: {buy}\nSell price: {sell}\nPercent: {str(round(x, 2))} %')
#проверка возможных ошибок
    except (ValueError, IndexError, UnboundLocalError, ZeroDivisionError):
        bot.reply_to(
            message, 'Bought or sold prices \nTry like: /percent 70 100 !🤡')

#хандлер на парс раста
@bot.message_handler(commands=['rust'])
def rust(message):
    
    response = rq.get('https://loot.farm/fullpriceRUST.json')
    items = json.loads(response.text)
    sor = sorted(items, key=itemgetter('rate'), reverse=True)
    continer = ''
    counter = 0
    for item in sor:
        
        have = item['have']
        max = item['max']
        name = item['name']
        price = item['price']/100*0.95
        so = item['rate']/100*100-100
        so1 = item['rate']
        if have < max and so1 >= 115:
            
            counter += 1
            continer += f'<code>{name}</code>:\nCтоимость <b>{round(price, 2)}$</b>\nПроцент <b>{round(so, 2)} %</b>\nПредметов на ботах: <b>{have}/{max}</b>.\n\n'
            
            if counter == 10:
                bot.send_message(message.chat.id, continer)
                sleep(1)
                counter = 0
                continer = ''
#хандлер на парсинг доты
@bot.message_handler(commands=['dota'])
def dota(message):
    response = rq.get('https://loot.farm/fullpriceDOTA.json')
    items = json.loads(response.text)
    sor = sorted(items, key=itemgetter('rate'), reverse=True)
    continer = ''
    counter = 0
    
    for item in sor:
        have = item['have']
        max = item['max']
        name = item['name']
        price = item['price']/100*0.95
        so = item['rate']/100*100-100
        so1 = item['rate']
        
        if have < max and so1 >= 115:
            counter += 1
            continer += f'<code>{name}</code>:\nCтоимость <b>{round(price, 2)}$</b>\nПроцент <b>{round(so, 2)} %</b>\nПредметов на ботах: <b>{have}/{max}</b>.\n\n'
            
            if counter == 10:
                bot.send_message(message.chat.id, continer)
                sleep(1)
                counter = 0
                continer = ''

#хандлер на парсинг ксго
@bot.message_handler(commands=['csgo'])

def csgo(message):
    
    response = rq.get('https://loot.farm/fullprice.json')
    items = json.loads(response.text)
    sor = sorted(items, key=itemgetter('rate'), reverse=True)
    continer = ''
    counter = 0
    
    for item in sor:
        have = item['have']
        max = item['max']
        name = item['name']
        price = item['price']/100*0.95
        so = item['rate']/100*100-100
        so1 = item['rate']
        
        if have < max and so1 >= 120:
            counter += 1
            continer += f'<code>{name}</code>:\nCтоимость <b>{round(price, 2)}$</b>\nПроцент <b>{round(so, 2)} %</b>\nПредметов на ботах: <b>{have}/{max}</b>.\n\n'
            
            if counter == 10:
                bot.send_message(message.chat.id, continer)
                sleep(1)
                counter = 0
                continer = ''

#хандлер на парсинг тф2
@bot.message_handler(commands=['TF2'])

def tf(message):
    
    response = rq.get('https://loot.farm/fullpriceTF2.json')
    items = json.loads(response.text)
    sor = sorted(items, key=itemgetter('rate'), reverse=True)
    continer = ''
    counter = 0
    
    for item in sor:
        have = item['have']
        max = item['max']
        name = item['name']
        price = item['price']/100*0.95
        so = item['rate']/100*100-100
        so1 = item['rate']
        
        if have < max and so1 >= 115:
            counter += 1
            continer += f'<code>{name}</code>:\nCтоимость <b>{round(price, 2)}$</b>\nПроцент <b>{round(so, 2)} %</b>\nПредметов на ботах: <b>{have}/{max}</b>.\n\n'
            
            if counter == 10:
                bot.send_message(message.chat.id, continer)
                sleep(1)
                counter = 0
                continer = ''

#функция эхобота
@bot.message_handler(content_types=["text"])

def repeat_all_messages(message):
    
    bot.send_message(message.chat.id, message.text)
    bot.reply_to(message, '🤡Я, настоящий гуль, остальные фейки!🤡')
    
    
bot.polling()
