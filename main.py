import telebot
from telebot import types
from function import chat_log

bot = telebot.TeleBot("token", parse_mode=None) #here you have to put your token
user = bot.get_me()
update = bot.get_updates()

main_menu_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2) #button display, row width represents the number of buttons that appears on a row
are_you_a_bot_button = types.KeyboardButton('Are you a bot?')
are_you_a_human_button = types.KeyboardButton('Are you a human?')
reply_my_message_button = types.KeyboardButton('Reply to my message please')
send_me_to_another_menu_button = types.KeyboardButton('Send me to another menu please')
main_menu_markup.add(are_you_a_bot_button, are_you_a_human_button, reply_my_message_button, send_me_to_another_menu_button)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.from_user.id, 'Hello, i am a bot', reply_markup=main_menu_markup) #reply markup gives the menu that we created
    print(chat_log(message)) #chat log prints information on the terminal

    @bot.message_handler(regexp= 'Are you a bot?')
    def are_you_a_bot_answer(message):
        bot.send_message(message.from_user.id, 'Yes i am, of course')
        print(chat_log(message))

    @bot.message_handler(regexp= 'Are you a human?')
    def are_you_a_human_button(message):
        bot.send_message(message.from_user.id, 'No i am not!')
        print(chat_log(message))

    @bot.message_handler(regexp= 'Reply to my message please')
    def reply_answer(message):
        bot.reply_to(message, 'Ok!') #replies

@bot.message_handler(regexp= 'Send me to another menu please')
def another_menu_answer(message):
    second_menu_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    thank_you_button = types.KeyboardButton('Thank you!')
    main_menu_button = types.KeyboardButton('Main Menu')
    second_menu_markup.add(thank_you_button, main_menu_button)
    bot.send_message(message.from_user.id, 'Ok!', reply_markup=second_menu_markup)

    @bot.message_handler(regexp= 'Thank you!')
    def thank_you_answer(message):
        bot.send_message(message.from_user.id, 'You are welcome :)')

    @bot.message_handler(regexp= 'Main Menu')
    def main_menu_answer(message):
        bot.send_message(message.from_user.id, 'Here you are', reply_markup=main_menu_markup)

bot.polling(none_stop=False, interval=False, timeout=20)
