import telebot;
#token = 5146293499:AAGkPTPbwpECUaM00lPonkimKYsIbgoN9UU
#bot = telebot.TeleBot('your token');

p = [""]
def CreateNote(last_message, id):
    """
    Realization
    :param last_message:
    :return: bot.send_message()
    """
    bot.send_message(id, "The last message is: " + last_message)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/help":
        bot.send_message(message.from_user.id, "Available features:\n"
                                               "/Note"
                                               " - Creates a new note after call")
    if message.text == "/Note":
        CreateNote(p[-1], message.from_user.id)
        #Clean Realization wasn't done yet - clean(p)
    else:
        last_message = message.text
        p.append(last_message) #bad idea

bot.polling(none_stop=True, interval=0)
