encoding = 'utf-8'
import telebot
import os
from fuzzywuzzy import fuzz


mas = []
if os.path.exists('boltun.txt'):
    f = open('boltun.txt', 'r', encoding='UTF-8')
    for x in f:
        if (len(x.strip()) > 2):
            mas.append(x.strip().lower())
    f.close()


# Answer function
def answer(text):
    try:
        text = text.lower().strip()
        if os.path.exists('boltun.txt'):
            a = 0
            n = 0
            nn = 0
            for q in mas:
                if ('u: ' in q):
                    aa = (fuzz.token_sort_ratio(q.replace('u: ', ''), text))
                    if (aa > a and aa != a):
                        a = aa
                        nn = n
                n = n+1
            s = mas[nn + 1]
            return s, aa
        else:
            return None, 0
    except:
        return None, 0


# Put your Telegram token here
bot = telebot.TeleBot('yourtoken')


# First command
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'PUT STARTING MESSAGE HERE')


# Get messages, answer, and save log
@bot.message_handler(content_types=["text"])
def handle_text(message):
    f = open(str(message.chat.id)+'_log.txt', 'a', encoding='UTF-8')
    otvet, aa = answer(message.text)
    f.write('u: '+message.text + '\n' + otvet + '\n')
    f.close()
    bot.send_message(message.chat.id, otvet)


# Start bot
bot.polling(none_stop=True, interval=0)
