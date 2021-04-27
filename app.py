import telebot
from config import keys, TOKEN
from utils import APIException, Converter

bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text= '''To start working with bot please enter command in the following format:
          <name of the currency>,
          <in which currency you want to transfer>
          <the amount of transferred money>       
          You can see all available currencies with: /values
          '''
    bot.reply_to(message,text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text= "Available currencies:"
    for key in keys.keys():
        text='\n'.join((text, key, ))
    bot.reply_to(message,text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')
        if len(values) != 3:
            raise APIException('False amount of parameters')
        quote, base, amount = [each_value.lower() for each_value in values]
        total_base = Converter.convert(quote, base, amount)
    except APIException as e:
        bot.reply_to(message, f"User's error: {e}")
    except Exception as e:
        bot.reply_to(message, f"Processing your request was not possible because of {e}")
    else:
        text = f'Price of {amount} {quote} in {base} - {total_base}'
        bot.send_message(message.chat.id, text)


bot.polling()