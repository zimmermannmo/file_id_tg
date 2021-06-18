import telebot
import time
import os
token = '1899004769:AAFmPSxnCdtKQm0mXrVugr5DoGYfdYvefSw'  
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['test'])
def find_file_ids(message):
    for file in os.listdir('photo/'):     # папка в которой файлы айди которых вам нудны
        if file.split('.')[-1] == 'jpg':            # расширение файла 
            f = open('photo/'+file, 'rb')
            msg = bot.send_photo(message.chat.id, f, None)
            # А теперь отправим вслед за файлом его file_id
            bot.send_message(message.chat.id, msg.photo, reply_to_message_id=msg.message_id)
        time.sleep(3)


if __name__ == '__main__':
    bot.infinity_polling()