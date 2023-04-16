""" import datetime
b1=int(input("Введите сумму Белладжио в чеке: "))
a1=int(input("Введите сумму Авалон в чеке: "))

b2=int(input("Введите фактически снятую сумму с терминала Белладжио: "))
a2=int(input("Введите фактически снятую сумму с терминала Авалон: "))
def v (i, j):
    v = i-j
    return (v)

if (v(b1, b2))<0:
    print ("Снять с Авалон: ", abs(v(b1, b2)))
elif (v(b1, b2))==0:
    print ("Все норм, работаем дальше")
else:
    print ("Снять с Биладжио: ", abs(v(b1, b2)))



dt_now = datetime.datetime.now()
print(dt_now)


 """

""" pip3 install --user pyTelegramBotAPI
 """

""" import telebot
bot = telebot.TeleBot("6278611193:AAEdTALucmAoDSkOV2cQbOZEXoWwFgOkBVs")
@bot.message.handlers(commands=["start"])
def start (message):
    bot.send_message(message.chat.id, "<b>Привет</b>", parse_mode="html")
bot.pollyng(none_stop=True) """

import datetime

print (datetime.datetime.now())
