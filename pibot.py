from env import botToken, myChatId
import telepot
from telepot.loop import MessageLoop
import time

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    # print 'id put this value on myChatId at the env.py file: %s' % chat_id
    if chat_id != myChatId:
	bot.sendMessage(chat_id, 'get out!! this bot is not for you!!')
    elif command == '/hi':
        bot.sendMessage(chat_id, 'hello world')
    else:
        bot.sendMessage(chat_id, 'say what?')

bot = telepot.Bot(botToken)

MessageLoop(bot, handle).run_as_thread()

while 1:
    time.sleep(10)
