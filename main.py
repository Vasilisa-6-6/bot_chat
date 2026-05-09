import telebot
from bot_logik import gen_passssssss, uwiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiikeiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii






bot = telebot.TeleBot('8457062048:AAEqknrHoRNqDSXZHQjwAoIQEKzRFLnXC6o')

text_messages = {
    'welcome':
        u'Добро пожаловать в группу {name}!\n\n'
        u'Правила чата:\n'
        u'Быть вежливым\n'
        u'Не писать после 22:00\n'
        u'Не отправлять не цензурные фото\n'}




# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")

# @bot.message_handler(commands=['hello'])
# def send_hello(message):
#     bot.reply_to(message, "Привет! Как дела?")
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

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
    # Обработчик команды '/start' и '/hello'




bot.polling()