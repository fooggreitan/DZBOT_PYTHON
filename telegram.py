import telebot
import random
from telebot import types
from datetime import datetime as dt

user_sweets = 0
digit = 0
sweets = 221

a = 0
b = 0
sign = 0

textMessagew = 0
time = 0

bot = telebot.TeleBot("")

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_restart1 = types.KeyboardButton('Начать игру')
    item_restart2 = types.KeyboardButton('Калькулятор')
    item_restart3 = types.KeyboardButton('Логирование')
    markup.add(item_restart1, item_restart2, item_restart3)
    bot.send_message(message.chat.id, 'Привет, {0.first_name}!'.format(message.from_user), reply_markup = markup)

def controller(message):
    global sweets
    global digit
    digit = random.randint(1, 2)
    if digit == 1:
        bot.send_message(message.chat.id, "Ходите вы")
        bot.send_message(message.chat.id, f'Введите количество не больше 28')
        bot.register_next_step_handler(message, user_input)
    else:
        bot.send_message(message.chat.id, "Ходит бот")
        user_bot(message)
def user_bot(message):
    global user_sweets
    user_sweets = random.randint(1, 28)
    get_count(message)
def user_input(message):
    global user_sweets
    user_sweets = int(message.text)
    if user_sweets > 28:
        userCount(message)
    else:
        get_count(message)
def userCount(message):
    global user_sweets
    bot.send_message(message.chat.id, "Вы взяли слишком много конфет!")
    controller(message)
def get_count(message):
    global sweets
    if sweets > 0:
        bot.send_message(message.chat.id, f'было {sweets}')
        if digit == 1:
            if sweets <= 28:
               winUser(message)
        else:
            if sweets <= 28:
                winBot(message)
            else:
                bot.send_message(message.chat.id, f'бот ввёл {user_sweets}')
        if sweets >= 28:
            sweets = sweets - user_sweets
            bot.send_message(message.chat.id, f'стало {sweets}')
            controller(message)
        else:
            sweets = 221
            start(message)
def winUser(message):
    bot.send_message(message.chat.id, "Вы победили!")
    bot.send_message(message.chat.id, f"Игра окончена")
def winBot(message):
    bot.send_message(message.chat.id, "Бот победил!")
    bot.send_message(message.chat.id, f"Игра окончена")

# =====================================================================================================

def kall(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_restart1 = types.KeyboardButton('Рациональные числа')
    item_restart2 = types.KeyboardButton('Комплексные числа')
    markup.add(item_restart1, item_restart2)
    bot.send_message(message.chat.id, 'Выберите пункт!'.format(message.from_user), reply_markup=markup)
def rationalNumbersint(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_restart1 = types.KeyboardButton('+')
    item_restart2 = types.KeyboardButton('-')
    item_restart3 = types.KeyboardButton('*')
    item_restart4 = types.KeyboardButton('/')
    item_restart5 = types.KeyboardButton('//')
    item_restart6 = types.KeyboardButton('%')
    markup.add(item_restart1, item_restart2, item_restart3, item_restart4, item_restart5, item_restart6)
    bot.send_message(message.chat.id, 'Выберите знак!'.format(message.from_user), reply_markup=markup)
def rationalNumbercomplex(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_restart1 = types.KeyboardButton('+')
    item_restart2 = types.KeyboardButton('-')
    item_restart3 = types.KeyboardButton('*')
    item_restart4 = types.KeyboardButton('/')
    markup.add(item_restart1, item_restart2, item_restart3, item_restart4)
    bot.send_message(message.chat.id, 'Выберите знак!'.format(message.from_user), reply_markup=markup)
def get_value_int1(message):
    bot.send_message(message.chat.id, f'Введите первое рациональное число')
    bot.register_next_step_handler(message, numner1_input)
def get_value_int2(message):
    bot.send_message(message.chat.id, f'Введите второе рациональное число')
    bot.register_next_step_handler(message, numner2_input)
def get_value_complex1(message):
    bot.send_message(message.chat.id, f'Введите первое комплексное число')
    bot.register_next_step_handler(message, complex1_input)
def get_value_complex2(message):
    bot.send_message(message.chat.id, f'Введите второе комплексное число')
    bot.register_next_step_handler(message, complex2_input)
def numner1_input(message):
    global a
    a = int(message.text)
    get_value_int2(message)
def numner2_input(message):
    global b
    b = int(message.text)
    rationalNumbersint(message)
def complex1_input(message):
    global a
    a = complex(message.text)
    get_value_complex2(message)
def complex2_input(message):
    global b
    b = complex(message.text)
    rationalNumbercomplex(message)
def summ(message):
    global a
    global b
    bot.send_message(message.chat.id, f'Ваш результат - > {a + b}')
    start(message)
def diff(message):
    global a
    global b
    bot.send_message(message.chat.id, f'Ваш результат - > {a - b}')
    start(message)
def multi(message):
    global a
    global b
    bot.send_message(message.chat.id, f'Ваш результат - > {a * b}')
    start(message)
def div(message):
    global a
    global b
    bot.send_message(message.chat.id, f'Ваш результат - > {a / b}')
    start(message)
def div_cel(message):
    global a
    global b
    bot.send_message(message.chat.id, f'Ваш результат - > {a // b}')
    start(message)
def div_ost(message):
    global a
    global b
    bot.send_message(message.chat.id, f'Ваш результат - > {a % b}')
    start(message)

#--------------------------------------------------------------------------

def textMessage(message):
    bot.send_message(message.chat.id, f'Введите сообщение')
    bot.register_next_step_handler(message, textMessagee)

def textMessagee(message):
    global textMessagew
    textMessagew = message.text
    record(message)

def record(message):
    global time
    time = dt.now().strftime('%H:%M:%S')
    res = ''
    res += 'Имя: {0.first_name}\n'.format(message.from_user)
    res += f'Cообщение: {textMessagew}\n'
    res += f'Время: {time}\n'
    res += ''
    with open("res.txt", 'r+', encoding="UTF-8") as file:
        file.write(f'{res}')
    bot.send_message(message.chat.id, 'Cообщение было отправлено'.format(message.from_user))
    start(message)

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.text == 'Начать игру':
        controller(message)
    elif message.text == 'Калькулятор':
        kall(message)
    elif message.text == 'Логирование':
        textMessage(message)
    elif message.text == 'Рациональные числа':
        get_value_int1(message)
    elif message.text == 'Комплексные числа':
        get_value_complex1(message)
    elif message.text == '+':
        summ(message)
    elif message.text == "-":
        diff(message)
    elif message.text == "*":
        multi(message)
    elif message.text == "/":
        div(message)
    elif message.text == "//":
        div_cel(message)
    elif message.text == "%":
        div_ost(message)

bot.polling(none_stop = True)
