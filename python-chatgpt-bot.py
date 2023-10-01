import telebot
import requests

# Bot API Token
API_TOKEN = '6648308530:AAEElJzJ1_cj8Qd5uX1YPA0S98trp54ejX4'
# Safone API URL
SAFONE_API_URL = 'https://api.safone.me/v1/assistant'

bot = telebot.TeleBot(API_TOKEN)

# Generate the Response
def get_response(msg):
    data =  'message': msg,
        'api_key': 'https://api.safone.me/chatgpt'
    
    response = requests.post(SAFONE_API_URL, data=data).json()
    return response['response']

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.send_message(message.chat.id, """\
Hi there, I am an AI ChatBot.

I am here to answer your questions.

I am powered by the Safone API!

Use /ask to ask questions.\
""")

# Handle the '/ask' command
@bot.message_handler(commands=['ask'])
def first_process(message):
    bot.send_message(message.chat.id, "Send me your question")
    bot.register_next_step_handler(message, second_process)

def again_send(message):
    bot.register_next_step_handler(message, second_process)

def second_process(message):
    bot.send_message(message.chat.id, get_response(message.text))
    again_send(message)

bot.infinity_polling()
