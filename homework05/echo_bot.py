# -*- coding: utf-8 -*-
import config
import telebot

# Создание бота с указанным токеном доступа
bot = telebot.TeleBot(config.access_token)

# Бот будет отвечать только на текстовые сообщения
@bot.message_handler(content_types=['text'])
def echo(message: str) -> None:
    bot.send_message(message.chat.id, message.text)

@bot.message_handler(content_types=['photo'])
def text_handler(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Красиво.')


if __name__ == '__main__':
    bot.polling(none_stop=True)

