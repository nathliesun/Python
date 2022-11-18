import telebot
import random

bot = telebot.TeleBot("5386855733:AAFJNpLKEHIQQj3jQ-2HqOdXVQmbfDEfNOs")

candies = 0
candies_player = 0
candies_bot = 0
playing = False

@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.reply_to(message, "Набери /play чтобы начать игру")

@bot.message_handler(commands=['play'])
def start_game(message):
    global playing, candies, candies_bot, candies_player
    bot.reply_to(message, "Играем в конфетки, бери от 1 до 28. Кто заберет последние, тот и победил")
    playing = True
    candies = 100
    candies_player = 0
    candies_bot = 0

@bot.message_handler(func=lambda message: message.text == 'привет')
def q(message):
    bot.reply_to(message, "привет")

@bot.message_handler(func=lambda message: True)
def a(message):
    global playing, candies, candies_player, candies_bot
    if (int(message.text) in range(1,29)) and playing:
        player_takes = int(message.text)
        if(player_takes > candies):
            bot.send_message(text="введи число от 1 до " + str(candies),chat_id=message.chat.id)
            return
        candies -= player_takes
        candies_player += player_takes
        bot.send_message(text='У тебя ' + str(candies_player) + ' конфет, осталось ' + str(candies),chat_id=message.chat.id)
        if(candies==0):
            bot.send_message(text='Ты победил!' ,chat_id=message.chat.id)
            playing = False
            return
        bot_takes = random.randint(0, 28)
        if(bot_takes > candies):
            bot_takes = candies
        candies -= bot_takes
        candies_bot += bot_takes
        bot.send_message(text='Я беру ' + str(bot_takes) + ', у меня ' + str(candies_bot) + ', осталось ' + str(candies) + ' конфет',chat_id=message.chat.id)
        if(candies==0):
            bot.send_message(text='Я победил!' ,chat_id=message.chat.id)
            playing = False
            return
    elif playing:
        bot.send_message(text="введи число от 1 до 28",chat_id=message.chat.id)

bot.infinity_polling()