import time, datetime
import telepot
from telepot.loop import MessageLoop

now = datetime.datetime.now()


def action(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print('Received: %s' % command)

    if command == '/hi':
        telegram_bot.sendMessage(chat_id, str('Hi! I AM MPR PROJECT'))
        telegram_bot.sendMessage(chat_id, str('Use /time to aske me the current time '))
        telegram_bot.sendMessage(chat_id, str('Use /logo for the college logo to be sent '))
        telegram_bot.sendMessage(chat_id, str('LIST OF NOTES AND BOOKS YOU CAN ASK FROME ME'))
        telegram_bot.sendMessage(chat_id, str('1 Python101 book --(/py101)'))  # (/py101 command to acess the file)
        telegram_bot.sendMessage(chat_id, str('2 Python202 book --(/py202)'))  # (/py202 command to acess the file)
        telegram_bot.sendMessage(chat_id, str('3 Basic Networking notes --(/netw)'))
        telegram_bot.sendMessage(chat_id, str('4 MPR FILE --(/c1)'))
    elif command == '/time':
        telegram_bot.sendMessage(chat_id, str(now.hour) + str(":") + str(now.minute))
    elif command == '/logo':
        telegram_bot.sendPhoto(chat_id, photo=" https://photos.app.goo.gl/8Z7ivRDSA4bJpCmc7")
    elif command == '/py101':
        telegram_bot.sendDocument(chat_id, document=open('/home/pi/Documents/py101.pdf'))
    elif command == '/py202':
        telegram_bot.sendDocument(chat_id, document=open('/home/pi/Documents/py202.pdf'))
    elif command == '/netw':
        telegram_bot.sendDocument(chat_id, document=open('/home/pi/Documents/netw.pdf'))
    elif command == '/c1':
        telegram_bot.sendDocument(chat_id, document=open('/home/pi/Documents/c1.pdf'))


telegram_bot = telepot.Bot('1817933623:AAHA2ZXYkdotuxPtHLBYhCfepxKELRPOhzw')
print(telegram_bot.getMe())

MessageLoop(telegram_bot, action).run_as_thread()
print('Up and Running....')

while 1:
    time.sleep(10)
