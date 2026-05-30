import telebot
import random
import os
from bot_logik import gen_passssssss, uwiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiikeiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton





bot = telebot.TeleBot('8457062048:AAEqknrHoRNqDSXZHQjwAoIQEKzRFLnXC6o')

text_messages = {
    'welcome':
        u'Добро пожаловать в группу {name}!\n\n'
        u'Правила чата:\n'
        u'Быть вежливым\n'
        u'Не писать после 22:00\n'
        u'Не отправлять не цензурные фото\n'}


kommands = ['/bye','/password','/keyboard','/start','/hello','/heh','/help','/mem','/cheremsha','/game']

# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")

# @bot.message_handler(commands=['hello'])
# def send_hello(message):
#     bot.reply_to(message, "Привет! Как дела?")


otxo = ['Макулатура', 'Железная палка', 'Бутылка для воды', 'Стеклянная банка', 'Огрызок яблока']

game_otvet = ''
count = 0
num = 0


def game_help():
    game_helper = InlineKeyboardMarkup()
    game_helper.row_width = 5
    game_helper.add(InlineKeyboardButton('Несортируемые', callback_data='cb_sor'),
                    InlineKeyboardButton('Бумага', callback_data='cb_pap'),
                    InlineKeyboardButton('Пластик', callback_data='cb_pla'),
                    InlineKeyboardButton('Стекло', callback_data='cb_ste'),
                    InlineKeyboardButton('Металл', callback_data='cb_met'))
    return game_helper


@bot.message_handler(func=lambda m: True, content_types=['new_chat_members'])
def on_user_joins(message):

    for user in message.new_chat_members:
        name = user.first_name
        if hasattr(user, 'last_name') and user.last_name is not None:
            name += u" {}".format(user.last_name)

        if hasattr(user, 'username') and user.username is not None:
            name += u" (@{})".format(user.username)

        bot.send_message(message.chat.id, text_messages['welcome'].format(name=name))

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['help'])
def send_bye(message):
    bot.reply_to(message, 'Вот мои команды:')
    for po in range(len(kommands)):
        bot.reply_to(message, kommands[po])

@bot.message_handler(commands=['mem'])
def send_mem(message):
    lelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelele = os.listdir('images')
    with open(f'images/{random.choice(lelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelele)}', 'rb') as upi:
        bot.send_photo(message.chat.id, upi)

@bot.message_handler(commands=['game'])
def sennd_game(message):
    global count, game_otvet, num
    bot.reply_to(message, 'Приветствую в игре про сортировку мусора!\nПравила игры: \nЯ называю отход \nВы отвечаете какой это отход из предложенных вариантов \nЯ говорю правильно или нет \nТы можешь несколько раз написать команду и несколько раз поиграть! \nВ 1-ой игре 1 отход')
    count = 0
    num = 0
    otxod = random.choice(otxo)
    if otxod == otxo[0]:
        game_otvet = 'cb_pap'
    elif otxod == otxo[1]:
        game_otvet = 'cb_met'
    elif otxod == otxo[2]:
        game_otvet = 'cb_pla'
    elif otxod == otxo[3]:
        game_otvet = 'cb_ste'
    elif otxod == otxo[4]:
        game_otvet = 'cb_sor'
    
    bot.send_message(message.chat.id, otxod, reply_markup=game_help())  


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    global count, game_otvet, num
    if call.data == game_otvet:
        bot.answer_callback_query(call.id, "Правильно")
        count += 1
        num += 1
    else:
        bot.answer_callback_query(call.id, "Неправильно")



@bot.message_handler(commands=['cheremsha'])
def sennd_cheremsha(message):
    bot.reply_to(message, 'Для здоровья малыша')
    with open('images/черемша.jpg', 'rb') as cherem:
        bot.send_photo(message.chat.id,  cherem)

@bot.message_handler(commands=['password'])
def sennd_pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaassssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss(message):
    bot.reply_to(message, gen_passssssss(10))

@bot.message_handler(commands=['keyboard'])
def send_uwiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii(message):
    bot.reply_to(message, uwiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiikeiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii())
    
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!')

# Обработчик команды '/heh'
@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)

@bot.message_handler(func=lambda message: True) # отвечает на просто сообщения можно поставить услоаие на конкретное сообщение
def echo_all(message):
    bot.reply_to(message, message.text)
    # Обработчик команды '/start' и '/hello'




bot.polling()