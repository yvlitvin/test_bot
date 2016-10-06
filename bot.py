#!/usr/bin/env python

import config
import telebot

from telebot import types




bot = telebot.TeleBot(config.token)

bot = telebot.TeleBot(config.token)
@bot.message_handler(commands=['help','start'])
def send_welcome(message):
    bot.reply_to(message, "Hello, you can use following commands \n /start \n /help \n /links")
    
    
@bot.message_handler(commands=['links'])
def command_help(message):
    markup = types.InlineKeyboardMarkup()
    itembtna = types.InlineKeyboardButton('open our site', url='www.credit-agricole.ua')
    itembtnv = types.InlineKeyboardButton('show contacts', url= 'www.umc.ua')
    itembtnc = types.InlineKeyboardButton('c', switch_inline_query="")
    markup.row(itembtna)
    markup.row(itembtnv, itembtnc)
    bot.send_message(message.chat.id, "Choose one letter:", reply_markup=markup)

    

@bot.message_handler(commands=["geophone"])
def geophone(message):
    # Эти параметры для клавиатуры необязательны, просто для удобства
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_phone = types.KeyboardButton(text="Отправить номер телефона", request_contact=True)
    button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
    keyboard.add(button_phone, button_geo)
    bot.send_message(message.chat.id, "---", reply_markup=keyboard)

bot.polling()
