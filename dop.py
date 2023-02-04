#--------------------------------------------------------------------------------------------------------

# global user_sweets
#     global swtt
#     swtt = int(message.text)

#     while user_sweets > 0:
#         digit = random.randint(1, 10)
#         if digit == 1:
#             if user_sweets < 28:
#                 bot.send_message(message.chat.id, 'Вы победили!')
#                 break
#             else:
#                 bot.send_message(message.chat.id, 'Введите число от 0 до 28: ')
#                 g = int(message.text)
#             if g > 28:
#                 bot.send_message(message.chat.id, 'Вы взяли cлишком много')
#                 g = 0
#             m = random.randint(0, 28)
#             bot.send_message(message.chat.id, f'Бот взял: {m}')
#         else:
#             if user_sweets < 28:
#                 bot.send_message(message.chat.id, 'бот победили!')
#                 break
#             else:
#                 m = random.randint(0, 28)
#                 bot.send_message(message.chat.id, f'Бот взял: {m}')
#                 g = int(message.text)

#             if g > 28:
#                 bot.send_message(message.chat.id, 'Вы взяли cлишком много')
#                 g = 0

#         bot.send_message(message.chat.id, '---------------------')
#         user_sweets = user_sweets - g - m
#         print(user_sweets)

#----------------------------------------------------------------------------------------------------

# #на столе лежит...
# import telebot
# import random
#
# bot = telebot.TeleBot("6185618554:AAGS8T5BvicTGRTkGKp3HGAq0HPYLnln8UM")
#
# flag = None
# sweets = 60
# max_sweet = 28
#
# @bot.message_handler(commands=["start"])
# def start(message):
#     global flag
#     bot.send_message(message.chat.id, f"Приветствую вас в игре!")
#     flag = random.choice(["user", "bot"])
#     bot.send_message(message.chat.id, f"Всего в игре {sweets} конфет")
#     if flag == "user":
#         bot.send_message(message.chat.id,f"Первым ходите вы")  # отправка сообщения (кому отправляем, что отправляем(str))
#     else:
#         bot.send_message(message.chat.id,f"Первым ходит бот")# отправка сообщения (кому отправляем, что отправляем(str))
#     controller(message)
#
# def controller(message):
#     global flag
#     if sweets > 0 :
#         if flag == "user":
#             bot.send_message(message.chat.id, f"Ваш ход введите кол-во конфет от 0 до {max_sweet}")
#             bot.register_next_step_handler(message,user_input)
#         else:
#             bot_input(message)
#     else:
#         flag = "user" if flag == "bot" else "bot"
#         bot.send_message(message.chat.id, f"Победил {flag}!")

# def bot_input(message):
#     global sweets, flag
#     if sweets <= max_sweet:
#         bot_turn = sweets
#     elif sweets % max_sweet == 0:
#         bot_turn = max_sweet - 1
#     else:
#         bot_turn = sweets % max_sweet - 1
#     sweets -= bot_turn
#     bot.send_message(message.chat.id, f"бот взял {bot_turn} конфет")
#     bot.send_message(message.chat.id, f"осталось {sweets}")
#     flag = "user" if flag == "bot" else "bot"
#     controller(message)

# def user_input(message):
#     global sweets,flag
#     user_turn = int(message.text)
#     sweets -= user_turn
#     bot.send_message(message.chat.id, f"осталось {sweets}")
#     flag = "user" if flag == "bot" else "bot"
#     controller(message)
#

# bot.infinity_polling()

#----------------------------------------------------------------------------------------------------

#на столе лежит c кнопками
# import telebot
# import random

# bot = telebot.TeleBot("6185618554:AAGS8T5BvicTGRTkGKp3HGAq0HPYLnln8UM")

# flag = None
# sweets = 20
# max_sweet = 28

# def restart():
#     global sweets
#     sweets = 60

# @bot.message_handler(commands=["start"])
# def start(message):
#     global flag
#     bot.send_message(message.chat.id, f"Приветствую вас в игре!")
#     # flag = random.choice(["user", "bot"])
#     bot.send_message(message.chat.id, f"Всего в игре {sweets} конфет")
#     mrk = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
#     key1 = telebot.types.KeyboardButton("хожу я")
#     key2= telebot.types.KeyboardButton("ходит бот")
#     mrk.add(key1)
#     mrk.add(key2)
#     bot.send_message(message.chat.id,"выбери ниже", reply_markup=mrk)
#     bot.register_next_step_handler(message,first_turn)
    # if flag == "user":
    #     bot.send_message(message.chat.id,f"Первым ходите вы")  # отправка сообщения (кому отправляем, что отправляем(str))
    # else:
    #     bot.send_message(message.chat.id,f"Первым ходит бот")# отправка сообщения (кому отправляем, что отправляем(str))
    # controller(message)

# @bot.message_handler(content_types=["text"])
# def first_turn(message):
#     global flag
#     if message.text == "хожу я":
#         flag = "user"
#     else:
#         flag = "bot"
#     controller(message)

# def controller(message):
#     global flag
#     if sweets > 0 :
#         if flag == "user":
#             bot.send_message(message.chat.id, f"Ваш ход введите кол-во конфет от 0 до {max_sweet}")
#             bot.register_next_step_handler(message,user_input)
#         else:
#             bot_input(message)
#     else:
#         flag = "user" if flag == "bot" else "bot"
#         bot.send_message(message.chat.id, f"Победил {flag}!")
#         mrk = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
#         key1 = telebot.types.KeyboardButton("рестар")
#         key2 = telebot.types.KeyboardButton("выход")
#         mrk.add(key1)
#         mrk.add(key2)
#         bot.send_message(message.chat.id,"если хочешь перезапусти", reply_markup=mrk)
#         bot.register_next_step_handler(message,choose_op)

# @bot.message_handler(content_types=["text"])
# def choose_op(message):
#     if message.text == "рестар":
#         print("111")
#         restart()
#         start(message)
#     else:
#         exit()

# def bot_input(message):
#     global sweets, flag
#
#     if sweets <= max_sweet:
#         bot_turn = sweets
#     elif sweets % max_sweet == 0:
#         bot_turn = max_sweet + 1
#     else:
#         bot_turn = sweets % max_sweet - 1
#
#     if bot_turn == 0:
#         bot_turn = 1
#     sweets -= bot_turn
#     bot.send_message(message.chat.id, f"бот взял {bot_turn} конфет")
#     bot.send_message(message.chat.id, f"осталось {sweets}")
#     flag = "user" if flag == "bot" else "bot"
#     controller(message)

# def user_input(message):
#     global sweets,flag
#     user_turn = int(message.text)
#     if user_turn == 0:
#         bot.send_message(message.chat.id,"введен ноль, повторите")
#         bot.register_next_step_handler(message,user_input)
#     else:
#         sweets -= user_turn
#         bot.send_message(message.chat.id, f"осталось {sweets}")
#         flag = "user" if flag == "bot" else "bot"
#         controller(message)
#

# bot.infinity_polling()

#--------------------------------------------------------------------

# import telebot
# import random

# user_sweets = 0
# sweets = 221
# bot = telebot.TeleBot("5537547955:AAHTXgYunAWpv29f8G4YoTWP_4c9W3glIzA")

# @bot.message_handler(commands=['start'])  # вызов функции по команде в списке
# def controller(message):
#     bot.send_message(message.chat.id, f"Введите количество не больше 28")  # отправка сообщения (кому отправляем, что отправляем(str))
#     bot.register_next_step_handler(message, user_input)
#     user_input(message)

# def user_input(message):
#     global user_sweets
#     user_sweets = int(message.text)
#     get_count(message)

# def get_count(message):
#     global sweets
#     digit = random.randint(1, 2)
#     if sweets > 0:
#         if digit == 1:
#             bot.send_message(message.chat.id, 'Первый игрок ходит')
#             if sweets < 29:
#                 bot.send_message(message.chat.id, 'Вы победили!')
#             elif user_sweets > 28:
#                 bot.send_message(message.chat.id, 'Вы взяли слишком много конфет!')
#         else:
#             bot.send_message(message.chat.id, 'Второй игрок ходит')
#             if sweets < 29:
#                 bot.send_message(message.chat.id, 'бот победили!')
#             elif user_sweets > 28:
#                 bot.send_message(message.chat.id, 'бот взял слишком много конфет!')
#         sweets = sweets - user_sweets
#         bot.send_message(message.chat.id, f"осталось {sweets}")
#         get_count(message)

#     else:
#         bot.send_message(message.chat.id, f"Игра окончена")

# bot.infinity_polling()

# ------------------------------------------------------------------------------------------------


# import random

# user_sweets = 0
# sweets = 221
# bot = telebot.TeleBot("5537547955:AAHTXgYunAWpv29f8G4YoTWP_4c9W3glIzA")

# @bot.message_handler(commands=['start'])  # вызов функции по команде в списке
# def controller(message):
#     global sweets
#     bot.send_message(message.chat.id, f"Введите количество не больше 28")  # отправка сообщения (кому отправляем, что отправляем(str))
#     bot.register_next_step_handler(message, user_input)

# def user_input(message):
#     global user_sweets
#     user_sweets = int(message.text)
#     get_count(message)

# def get_count(message):
#     global sweets
#     digit = random.randint(1, 2)
#     if sweets > 0:

#         if digit == 1:
#             bot.send_message(message.chat.id, 'Первый игрок ходит')
#             if sweets < 29:
#                 bot.send_message(message.chat.id, 'Вы победили!')
#             elif user_sweets > 28:
#                 bot.send_message(message.chat.id, 'Вы взяли слишком много конфет!')
#         else:
#             bot.send_message(message.chat.id, 'Второй игрок ходит')
#             if sweets < 29:
#                 bot.send_message(message.chat.id, 'бот победили!')
#             elif user_sweets > 28:
#                 bot.send_message(message.chat.id, 'бот взял слишком много конфет!')

#         sweets = sweets - user_sweets
#         bot.send_message(message.chat.id, f"осталось {sweets}")
#         controller(message)

#     else:
#         bot.send_message(message.chat.id, f"Игра окончена")

# bot.infinity_polling()