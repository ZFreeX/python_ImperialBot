import telebot
import random

bot = telebot.TeleBot('1001914184:AAEuTBl2XfYKdf2qj0GojneFiWDNtMxh084')

flex_all = 0
ad = ['Лучший руковод', 'А Анна Романовна где??', 'О великая Хмыз Анастасия Дмитриевнааа']

@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Команды: \n /get - получить флекс; \n /join - вступить в империю; \n /ad - Анастасия Дмитриевна, она же АД; \n /balance - проверить баланс; \n /rofl - скорей рофлить ; \n')

def get_flex(message):
    global flex_all
    flex_all = 0
    bot.send_message(message.chat.id, 'Напиши "ПОДТВЕРДИТЬ", чтобы завершить транзакцию. ')
    bot.register_next_step_handler(message, flex_reply);
    global flex
    flex = message.text
    flex_all = flex_all + int(flex);

@bot.message_handler(commands=['get'])
def start_message(message):
    bot.send_message(message.chat.id, 'Окей, сейчас ты получишь флекс. Сколько ты хочешь? (Введи число флексов)')
    bot.register_next_step_handler(message, get_flex);


@bot.message_handler(commands=['join'])
def start_message(message):
    bot.send_message(message.chat.id, 'Поздравляю, теперь ты с нами :) ')


@bot.message_handler(commands=['ad'])
def start_message(message):
    bot.send_message(message.chat.id, random.choice(ad))

@bot.message_handler(commands=['rofl'])
def start_message(message):
    bot.send_message(message.chat.id, 'Дзугань уже рофлит')

@bot.message_handler(commands=['balance'])
def start_message(message):
    bot.send_message(message.chat.id, 'Твой баланс - ' + str(flex_all))


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Салам алейкум. Бот нашей Империи на связи. Введи /help для справки :) ')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай. Империя не забудет тебя.')
    else:
        bot.send_message(message.chat.id, 'Ммм, это что-то новенькое. Такой команды я пока что не знаю) ')

def flex_reply(message):
    if message.text == 'ПОДТВЕРДИТЬ':
        bot.send_message(message.chat.id, 'Можешь проверять баланс.')
    else:
        bot.send_message(message.chat.id, 'Начисление не подтверждено. ')

bot.polling(none_stop=True, interval=0)