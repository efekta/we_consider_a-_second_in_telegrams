import ptbot
import os
from pytimeparse import parse
import datetime

telegram_bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
bot = ptbot.Bot(telegram_bot_token)
telegram_chat_id = os.getenv("TELEGRAM_ID_CHAT")
message_id = bot.send_message(telegram_chat_id, "На сколько запустить таймер?")


def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


def notify_progress(secs_left, message_id):
    bot.update_message(telegram_chat_id, message_id ,"Осталось {} {}".format(secs_left, "seconds"))



def notify(response):
    bot.send_message(telegram_chat_id, "Время вышло!")

def reply(text):
    bot.send_message(telegram_chat_id, "Таймер запущен на {} {}".format(text, 'seconds'))
    new_message_id = bot.send_message(telegram_chat_id, "Осталось {} {}".format(text, "seconds"))
    bot.create_countdown((int(text)), notify_progress, message_id = new_message_id)
    bot.create_timer(int(text), notify, "answer")
    

bot.wait_for_msg(reply)


############################################
import ptbot
import os
from pytimeparse import parse
import datetime

telegram_bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
bot = ptbot.Bot(telegram_bot_token)
telegram_chat_id = os.getenv("TELEGRAM_ID_CHAT")
message_id = bot.send_message(telegram_chat_id, "На сколько запустить таймер?")


def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


def notify_progress(secs_left, message_id):
    bot.update_message(telegram_chat_id, message_id ,"Осталось {} {}".format(secs_left, "seconds"))
    bot.send_message(telegram_chat_id, render_progressbar(10,2))

    


def notify(response):
    bot.send_message(telegram_chat_id, "Время вышло!")

def reply(text):
    bot.send_message(telegram_chat_id, "Таймер запущен на {} {}".format(text, 'seconds'))
    new_message_id = bot.send_message(telegram_chat_id, "Осталось {} {}".format(text, "seconds"))
    bot.create_countdown((int(text)), notify_progress, message_id = new_message_id)
    bot.create_timer(int(text), notify, "answer")
    

bot.wait_for_msg(reply)
print(render_progressbar(10,2))



#############################################
import ptbot
import os
from pytimeparse import parse
import datetime

telegram_bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
bot = ptbot.Bot(telegram_bot_token)
telegram_chat_id = os.getenv("TELEGRAM_ID_CHAT")
message_id = bot.send_message(telegram_chat_id, "На сколько запустить таймер?")


def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


def notify_progress(secs_left, message_id_text,message_id_bar,maxbar):
#Обновляем сообщение с текстом
#message_id_text - id сообщения с текстом
#telegram_chat_id - id чата
#secs_left - сколько секунд осталось
    bot.update_message(telegram_chat_id, message_id_text ,"Осталось {} {}".format(secs_left, "seconds"))
#Обновляем сообщение с графиком
#message_id_bar - id сообщения с графиком
#telegram_chat_id - id чата
#secs_left - сколько секунд осталось
#maxbar - максимальное значение графика(мксимум секунд)
#(maxbar-secs_left) - получаем сколько секунд не осталось, а прошло с момента
#запуска тамера 
    bot.update_message(telegram_chat_id, message_id_bar , render_progressbar(maxbar,(maxbar-secs_left)))
    

    


def notify(response):
    bot.send_message(telegram_chat_id, "Время вышло!")

def reply(text):

#Пишем сообщение, что таймер запущен
#Используем telegram_chat_id = id чата где принимаем сообщения        
    bot.send_message(telegram_chat_id, "Таймер запущен на {} {}".format(text, 'seconds'))
#Пишем первое сообщение  с текстом "Осталось n секунд" и его id записываем в message_id_text
#Используем входящую переменную text для задания времени таймера  
    message_id_text = bot.send_message(telegram_chat_id, "Осталось {} {}".format(text, "seconds"))
#Создаем сообщение со шкалой и его id записываем в переменную message_id_bar
#Используем входящую переменную text для задания времени таймера  
    message_id_bar = bot.send_message(telegram_chat_id, render_progressbar((int(text)),1))
#Пишем функцию отсчёта таймера notify_progress. В неё передаём 3 параметра
#message_id_text - id сообщения с текстом
#message_id_bar - id сообщения с графиком
#maxbar - максимальное значение графика(мксимум секунд)
    bot.create_countdown((int(text)), notify_progress, message_id_text = message_id_text,message_id_bar = message_id_bar,maxbar=(int(text)))
    bot.create_timer(int(text), notify, "answer")
    

bot.wait_for_msg(reply)










import ptbot
import os
from pytimeparse import parse
import datetime

telegram_bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
bot = ptbot.Bot(telegram_bot_token)
telegram_chat_id = os.getenv("TELEGRAM_ID_CHAT")
message_id = bot.send_message(telegram_chat_id, "На сколько запустить таймер?")


def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


def notify_progress(secs_left, message_id, maxbar):
#Обновляем сообщение 
#message_id - id сообщения 
#telegram_chat_id - id чата
#secs_left - сколько секунд осталось
#maxbar - максимальное значение графика(мксимум секунд)
#(maxbar-secs_left) - получаем сколько секунд не осталось, а прошло с момента
#запуска тамера 
    bot.update_message(telegram_chat_id, message_id, parse("Осталось {} {}".format(secs_left, "seconds"),'\n',render_progressbar(maxbar,(maxbar-secs_left))))
#Обновляем сообщение с графиком
   


def notify(response):
    bot.send_message(telegram_chat_id, "Время вышло!")

def reply(text):

#Пишем сообщение, что таймер запущен
#Используем telegram_chat_id = id чата где принимаем сообщения        
    bot.send_message(telegram_chat_id, "Таймер запущен на {} {}".format(text, 'seconds'))
#Пишем первое сообщение  и его id записываем в message_id
#Используем входящую переменную text для задания времени таймера  
    message_id = bot.send_message(telegram_chat_id, parse("Осталось {} {}".format(text, "seconds"),'\n',render_progressbar((int(text)),1)))

#Пишем функцию отсчёта таймера notify_progress. В неё передаём 3 параметра
#message_id - id сообщения
#maxbar - максимальное значение графика(мксимум секунд)
    bot.create_countdown((int(text)), notify_progress, message_id = message_id,maxbar=(int(text)))
    bot.create_timer(int(text), notify, "answer")
    

bot.wait_for_msg(reply)




import ptbot
import os
from pytimeparse import parse
import datetime

telegram_bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
bot = ptbot.Bot(telegram_bot_token)
telegram_chat_id = os.getenv("TELEGRAM_ID_CHAT")
message_id = bot.send_message(telegram_chat_id, "На сколько запустить таймер?")


def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


def notify_progress(secs_left, message_id_text, message_id_bar, maxbar):
#Обновляем сообщение с текстом
#message_id_text - id сообщения с текстом
#telegram_chat_id - id чата
#secs_left - сколько секунд осталось
    bot.update_message(telegram_chat_id, message_id_text ,"Осталось {} {}".format(secs_left, "seconds"))
#Обновляем сообщение с графиком
#message_id_bar - id сообщения с графиком
#telegram_chat_id - id чата
#secs_left - сколько секунд осталось
#maxbar - максимальное значение графика(мксимум секунд)
#(maxbar-secs_left) - получаем сколько секунд не осталось, а прошло с момента
#запуска тамера 
    bot.update_message(telegram_chat_id, message_id_bar , render_progressbar(maxbar,(maxbar-secs_left)))
    print(secs_left)
    print(message_id_text)
    print(message_id_bar)
    print(maxbar)
    


def notify(response):
    bot.send_message(telegram_chat_id, "Время вышло!")

def reply(text):

#Пишем сообщение, что таймер запущен
#Используем telegram_chat_id = id чата где принимаем сообщения        
    bot.send_message(telegram_chat_id, "Таймер запущен на {} {}".format(text, 'seconds'))
#Пишем первое сообщение  с текстом "Осталось n секунд" и его id записываем в message_id_text
#Используем входящую переменную text для задания времени таймера  
    message_id_text = bot.send_message(telegram_chat_id, "Осталось {} {}".format(text, "seconds"))
#Создаем сообщение со шкалой и его id записываем в переменную message_id_bar
#Используем входящую переменную text для задания времени таймера  
    message_id_bar = bot.send_message(telegram_chat_id, render_progressbar((int(text)),1))
#Пишем функцию отсчёта таймера notify_progress. В неё передаём 3 параметра
#message_id_text - id сообщения с текстом
#message_id_bar - id сообщения с графиком
#maxbar - максимальное значение графика(мксимум секунд)
    bot.create_countdown((int(text)), notify_progress, message_id_text = message_id_text, message_id_bar = message_id_bar, maxbar=(int(text)))
    bot.create_timer(int(text), notify, "answer")
    

bot.wait_for_msg(reply)




import ptbot
import os
from pytimeparse import parse
import datetime

telegram_bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
bot = ptbot.Bot(telegram_bot_token)
telegram_chat_id = os.getenv("TELEGRAM_ID_CHAT")
message_id = bot.send_message(telegram_chat_id, "На сколько запустить таймер?")


def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)

    

def notify_progress(secs_left, message_id):
    bot.update_message(telegram_chat_id, message_id, "Осталось {} {}".format(secs_left, 'seconds'))

def notify_end(answer):
    bot.send_message(telegram_chat_id, "Время вышло")


def reply(user_input_in_seconds):
    user_input_in_seconds = parse(user_input_in_seconds)

    # bot.send_message(telegram_chat_id, "Таймер запущен на {} {}".format(user_input_in_seconds, 'seconds'))
    message_id_progress = bot.send_message(telegram_chat_id, "Осталось {} {}".format(user_input_in_seconds, 'seconds'))

    bot.create_countdown(int(user_input_in_seconds), notify_progress, message_id = message_id_progress)
    bot.create_timer(int(user_input_in_seconds), notify_end, user_input_in_seconds)

bot.wait_for_msg(reply)
import ptbot
import os
from pytimeparse import parse
import datetime

telegram_bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
bot = ptbot.Bot(telegram_bot_token)
telegram_chat_id = os.getenv("TELEGRAM_ID_CHAT")
message_id = bot.send_message(telegram_chat_id, "На сколько запустить таймер? Формат: 10s, 2m, 3h")


def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


def notify_progress(secs_left, message_id, message_id_bar, maxbar):
    minbar = maxbar - secs_left
    bot.update_message(
        telegram_chat_id, 
        message_id, 
        ("Осталось {} {}".format(secs_left, "seconds"),
        "\n",
        render_progressbar(maxbar, minbar)
        )
    
    )
    # bot.update_message(telegram_chat_id, message_id_bar, render_progressbar(maxbar, minbar))


def notify_end(answer):
    bot.send_message(telegram_chat_id, "Время вышло")


def reply(user_input_in_seconds):
    user_input_in_seconds = parse(user_input_in_seconds)
    user_input_in_seconds = int(user_input_in_seconds)

    message_id_progress = bot.send_message(
        telegram_chat_id,
        ("Осталось {} {} ".format(user_input_in_seconds, "seconds"),
        "\n",
        render_progressbar(int(user_input_in_seconds), 1)
        )
    )

    # message_id_bar = bot.send_message(telegram_chat_id, render_progressbar(user_input_in_seconds, 1))

    bot.create_countdown(
        user_input_in_seconds,
        notify_progress,
        message_id = message_id_progress,
        message_id_bar = user_input_in_seconds,
        maxbar = int(user_input_in_seconds)
    )
    bot.create_timer(user_input_in_seconds, notify_end, user_input_in_seconds)


bot.wait_for_msg(reply)




# Финал
import ptbot
import os
from pytimeparse import parse
import datetime

telegram_bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
bot = ptbot.Bot(telegram_bot_token)
telegram_chat_id = os.getenv("TELEGRAM_ID_CHAT")
message_id = bot.send_message(telegram_chat_id, "На сколько запустить таймер? Формат: 10s, 2m, 3h")


def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)

    
def notify_progress(secs_left, message_id, message_id_bar, maxbar):
    bot.update_message(telegram_chat_id, message_id, "Осталось {} {}".format(secs_left, "seconds"))
    bot.update_message(telegram_chat_id, message_id_bar, render_progressbar(maxbar,(maxbar-secs_left)))

def notify_end(answer):
    bot.send_message(telegram_chat_id, "Время вышло")

def reply(user_input_in_seconds):
    user_input_in_seconds = parse(user_input_in_seconds)
    message_id_progress = bot.send_message(telegram_chat_id, "Осталось {} {}".format(user_input_in_seconds, "seconds"))
    message_id_bar = bot.send_message(telegram_chat_id, render_progressbar((int(user_input_in_seconds)),1))
    bot.create_countdown(int(user_input_in_seconds), notify_progress, message_id = message_id_progress, message_id_bar = message_id_bar, maxbar=(int(user_input_in_seconds)))
    bot.create_timer(int(user_input_in_seconds), notify_end, user_input_in_seconds)

bot.wait_for_msg(reply)























import ptbot
import os
from pytimeparse import parse
import datetime

telegram_bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
bot = ptbot.Bot(telegram_bot_token)
telegram_chat_id = os.getenv("TELEGRAM_ID_CHAT")
message_id = bot.send_message(telegram_chat_id, "На сколько запустить таймер? Формат: 10s, 2m, 3h")


def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)

    
def notify_progress(secs_left, message_id, message_id_bar, maxbar):
    minbar = maxbar - secs_left
    bot.update_message(telegram_chat_id, message_id, "Осталось {} {}".format(secs_left, "seconds"))
    bot.update_message(telegram_chat_id, message_id_bar, render_progressbar(maxbar, minbar))

def notify_end(answer):
    bot.send_message(telegram_chat_id, "Время вышло")

def reply(user_input_in_seconds):
    user_input_in_seconds = parse(user_input_in_seconds)
    maxbar = int(user_input_in_seconds)

    message_id_progress = bot.send_message(
        telegram_chat_id, 
        ("Осталось {} {}".format(user_input_in_seconds, "seconds"),
        "\n",
        render_progressbar(maxbar, 1)
        )
    )
    
    bot.create_countdown(
        maxbar, 
        notify_progress, 
        message_id = message_id_progress, 
        message_id_bar = message_id,
        maxbar = int(user_input_in_seconds)        
    )
    bot.create_timer(
        maxbar, 
        notify_end, 
        user_input_in_seconds
    )

bot.wait_for_msg(reply)




import ptbot
import os
from pytimeparse import parse
import datetime

telegram_bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
bot = ptbot.Bot(telegram_bot_token)
telegram_chat_id = os.getenv("TELEGRAM_ID_CHAT")
message_id = bot.send_message(telegram_chat_id, "На сколько запустить таймер? Формат: 10s, 2m, 3h")

def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)
    
def notify_progress(secs_left, message_id,  maxbar):
    # bot.update_message(telegram_chat_id, message_id, "Осталось {} {}".format(secs_left, "seconds"))
    # bot.update_message(telegram_chat_id, message_id_bar, render_progressbar(maxbar, maxbar-secs_left))
    s = ("Осталось {} {}".format(secs_left, "seconds"), "\n", render_progressbar(maxbar, maxbar-secs_left)).join
    bot.update_message(
        telegram_chat_id, 
        message_id,
        s
        # (
        #     "Осталось {} {}".format(secs_left, "seconds"),
        #     "\n",
        #     render_progressbar(maxbar, maxbar-secs_left)
        # )
    )

def notify_end(answer):
    bot.send_message(telegram_chat_id, "Время вышло")

def reply(user_input_in_seconds):
    user_input_in_seconds = parse(user_input_in_seconds)
    bot.send_message(telegram_chat_id, "Таймер запущен на {} {}".format(user_input_in_seconds, 'seconds'))
    # user_input_in_seconds = parse(user_input_in_seconds)
    maxbar = int(user_input_in_seconds)

    # message_id_progress = bot.send_message(telegram_chat_id, "Осталось {} {}".format(user_input_in_seconds, "seconds"))
    # message_id_bar = bot.send_message(telegram_chat_id, render_progressbar(maxbar,1))
    s = ("Осталось {} {}".format(user_input_in_seconds, "seconds"), "\n", render_progressbar(maxbar,1)).join
    message_id = bot.send_message(
        telegram_chat_id,
        s
        # (
        #     "Осталось {} {}".format(user_input_in_seconds, "seconds"),
        #     "\n",
        #     render_progressbar(maxbar,1)
        # )
    )

    bot.create_countdown(
        maxbar, 
        notify_progress, 
        message_id = message_id,
        maxbar = int(user_input_in_seconds)
    )

    bot.create_timer(maxbar, notify_end, user_input_in_seconds)

bot.wait_for_msg(reply)













import ptbot
import os
from pytimeparse import parse
import datetime

telegram_bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
bot = ptbot.Bot(telegram_bot_token)
telegram_chat_id = os.getenv("TELEGRAM_ID_CHAT")
message_id = bot.send_message(telegram_chat_id, "На сколько запустить таймер? Формат: 10s, 2m, 3h")

def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)
    
def notify_progress(secs_left, message_id,  maxbar):
    # bot.update_message(telegram_chat_id, message_id, "Осталось {} {}".format(secs_left, "seconds"))
    # bot.update_message(telegram_chat_id, message_id_bar, render_progressbar(maxbar, maxbar-secs_left))
    sep = "\n"
    seq = "Осталось {} {}".format(secs_left, "seconds"), render_progressbar(maxbar, maxbar-secs_left)
    bot.update_message(
        telegram_chat_id, 
        message_id,
        sep.join(seq)
        # (
        #     "Осталось {} {}".format(secs_left, "seconds"),
        #     "\n",
        #     render_progressbar(maxbar, maxbar-secs_left)
        # )
    )

def notify_end(answer):
    bot.send_message(telegram_chat_id, "Время вышло")

def reply(user_input_in_seconds):
    user_input_in_seconds = parse(user_input_in_seconds)
    bot.send_message(telegram_chat_id, "Таймер запущен на {} {}".format(user_input_in_seconds, 'seconds'))
    # user_input_in_seconds = parse(user_input_in_seconds)
    maxbar = int(user_input_in_seconds)

    # message_id_progress = bot.send_message(telegram_chat_id, "Осталось {} {}".format(user_input_in_seconds, "seconds"))
    # message_id_bar = bot.send_message(telegram_chat_id, render_progressbar(maxbar,1))
    sep = "\n"
    seq = "Осталось {} {}".format(user_input_in_seconds, "seconds"), render_progressbar(maxbar,1)
    message_id = bot.send_message(
        telegram_chat_id,
        sep.join(seq)
        # (
        #     "Осталось {} {}".format(user_input_in_seconds, "seconds"),
        #     "\n",
        #     render_progressbar(maxbar,1)
        # )
    )

    bot.create_countdown(
        maxbar, 
        notify_progress, 
        message_id = message_id,
        maxbar = int(user_input_in_seconds)
    )

    bot.create_timer(maxbar, notify_end, user_input_in_seconds)

bot.wait_for_msg(reply)
