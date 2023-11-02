import telebot
from telebot import types
import wikipedia as wiki
from googletrans import Translator

tarjimon = Translator()
wiki.set_lang("en")
# pip install googletrans==3.1.0a0

def getTarjimon(word_id):
  lang = tarjimon.detect(word_id).lang
  dest = "en" if lang == "uz" else "uz"
  tarjima = tarjimon.translate(word_id, dest)
  return tarjima


API_TOKEN = '5698911193:AAGikBbzy1ZPYyJg6yEawhIg3DTOF6ym7fo'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message,text = "Hi there, I am EchoBot.\nI am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!")

@bot.message_handler()
def echo_message(message):
  try:
    res = getTarjimon(message.text)
    w = wiki.summary(res.text)
    wo = getTarjimon(w)
    bot.reply_to(message, wo.text)
  except:
    bot.reply_to(message, f"{message.text} Bu mavzudagi maqola topilmadi")


@bot.message_handler(regexp="idss")
def echooo(messages):
  ids = messages.chat.id
  bot.send_message(messages.chat.id,text = f"[salom](tg://user?id{ids}) salom")

print("Bot Runing....")
bot.infinity_polling()