import telepot
from telepot.loop import MessageLoop

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print 'Got command: %s' % command

    if command == '/hi':
        bot.sendMessage(chat_id, 'hello world motherfucker')
    else:
        bot.sendMessage(chat_id, 'say what nigga')

bot = telepot.Bot('*')

MessageLoop(bot, handle).run_as_thread()
print 'I am listening ...'

while 1:
    time.sleep(10)
