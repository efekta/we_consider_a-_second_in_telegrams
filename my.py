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
    message_bar = render_progressbar(maxbar, maxbar-secs_left)
    message_result = "Осталось {} seconds \n {}".format(secs_left, message_bar)
    bot.update_message(
        telegram_chat_id, 
        message_id,
        message_result
    )

def notify_end(answer):
    bot.send_message(telegram_chat_id, "Время вышло")

def reply(user_input_in_seconds):
    user_input_in_seconds = parse(user_input_in_seconds)
    bot.send_message(telegram_chat_id, "Таймер запущен на {} seconds".format(user_input_in_seconds))
    maxbar = int(user_input_in_seconds)
    message_bar = render_progressbar(maxbar,1)
    message_result = "Осталось {} seconds \n {}".format(user_input_in_seconds, message_bar)
    message_id = bot.send_message(
        telegram_chat_id,
        message_result
    )
    bot.create_countdown(
        maxbar, 
        notify_progress, 
        message_id = message_id,
        maxbar = int(user_input_in_seconds)
    )

    bot.create_timer(maxbar, notify_end, user_input_in_seconds)

bot.wait_for_msg(reply)

