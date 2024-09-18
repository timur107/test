import telebot
import config
import random

bot = telebot.TeleBot(config.token)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hello, I am BotusBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")
    
@bot.message_handler(commands=['random', 'rnd'])
def send_welcome(message):
    number = random.randint(0, 100)
    bot.reply_to(message, "Случайное число от 0 до 100: " + str(number))

@bot.message_handler(content_types=['new_chat_members'])
def make_some(message):
    bot.send_message(message.chat.id, 'I accepted a new user!')
    bot.approve_chat_join_request(message.chat.id, message.from_user.id)
    
# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, "Ты написал: " + message.text)


bot.infinity_polling()