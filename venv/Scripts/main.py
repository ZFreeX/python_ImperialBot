from telebot import types
from time import  time
import telebot
import random


global group_id
promo_check = True
promo_buff = False
smile =  u'\U0001F300'

bot = telebot.TeleBot('1001914184:AAEuTBl2XfYKdf2qj0GojneFiWDNtMxh084')
print('bot started...\n')
flex_all = 0
ad = ['Лучший руковод', 'А Анна Романовна где??', 'О великая Хмыз Анастасия Дмитриевнааа']
print('OK...')


@bot.message_handler(commands=['сукаразрешиписать'])
def start_message(message):
    bot.send_photo(message.chat.id, photo=open('cb.jpg', 'rb'), reply_to_message_id=message.message_id)
    bot.restrict_chat_member(message.chat.id, message.from_user.id, until_date=time() + 720)




@bot.message_handler(commands=['forward'])
def start_message(message):
    bot.send_message(message.chat.id, 'Секретная команда активирована. ')
    bot.register_next_step_handler(message, forward)

def forward(message):
    bot.send_message(-1001357751907, message.text)
    bot.send_message(message.chat.id, 'Переслал. ')


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Команды: \n /get - получить флекс; \n /сукаразрешиписать - для Лёни \n /join - вступить в империю; \n /grodno - без комментариев; \n /surprise - лучше б ты не вводил это; \n /leave - покинуть империю; \n /ad - Анастасия Дмитриевна, она же АД; \n /balance - проверить баланс; \n /rofl - скорей рофлить ; \n')
    print(message.chat.id)
    bot.send_message(714203526, message.from_user.username+'s id: '+str(message.chat.id))
    bot.send_message(714203526, message.from_user.username+' сказал(а): '+message.text)


def get_flex(message):
    global flex_all
    flex_all = flex_all
    bot.register_next_step_handler(message, flex_reply);
    global flex
    flex = message.text



    """
        if i == '+':
            bot.send_message(message.chat.id, 'Нормальное целое число, будьте добры. ',  reply_to_message_id=message.message_id)
            break
        elif i == '-':
            bot.send_message(message.chat.id, 'Нормальное целое число, будьте добры. ',  reply_to_message_id=message.message_id)
            break
        elif i == '*':
            bot.send_message(message.chat.id, 'Нормальное целое число, будьте добры. ',  reply_to_message_id=message.message_id)
            break
        elif i == '/':
            bot.send_message(message.chat.id, 'Нормальное целое число, будьте добры. ',  reply_to_message_id=message.message_id)
            break
     """


    if flex[0] == '1' :
        if flex[1] == '+':
            flex_all = flex_all + int(flex[0])+int(flex[2]);
            bot.send_message(message.chat.id, 'Напиши "ПОДТВЕРДИТЬ", чтобы завершить транзакцию. ')
        else:
            flex_all = flex_all + int(flex)
            bot.send_message(message.chat.id, 'Напиши "ПОДТВЕРДИТЬ", чтобы завершить транзакцию. ')
    elif flex[0] == '2':
        if flex[1] == '+':
            flex_all = flex_all + int(flex[0]) + int(flex[2]);
            bot.send_message(message.chat.id, 'Напиши "ПОДТВЕРДИТЬ", чтобы завершить транзакцию. ')
        else:
            flex_all = flex_all + int(flex)
            bot.send_message(message.chat.id, 'Напиши "ПОДТВЕРДИТЬ", чтобы завершить транзакцию. ')
    elif flex[0] == '3':
        if flex[1] == '+':
            flex_all = flex_all + int(flex[0]) + int(flex[2]);
            bot.send_message(message.chat.id, 'Напиши "ПОДТВЕРДИТЬ", чтобы завершить транзакцию. ')
        else:
            flex_all = flex_all + int(flex)
            bot.send_message(message.chat.id, 'Напиши "ПОДТВЕРДИТЬ", чтобы завершить транзакцию. ')
    elif flex[0] == '4':
        if flex[1] == '+':
            flex_all = flex_all + int(flex[0]) + int(flex[2]);
            bot.send_message(message.chat.id, 'Напиши "ПОДТВЕРДИТЬ", чтобы завершить транзакцию. ')
        else:
            flex_all = flex_all + int(flex)
            bot.send_message(message.chat.id, 'Напиши "ПОДТВЕРДИТЬ", чтобы завершить транзакцию. ')
    elif flex[0] == '5':
        if flex[1] == '+':
            flex_all = flex_all + int(flex[0]) + int(flex[2]);
            bot.send_message(message.chat.id, 'Напиши "ПОДТВЕРДИТЬ", чтобы завершить транзакцию. ')
        else:
            flex_all = flex_all + int(flex)
            bot.send_message(message.chat.id, 'Напиши "ПОДТВЕРДИТЬ", чтобы завершить транзакцию. ')
    elif flex[0] == '6':
        if flex[1] == '+':
            flex_all = flex_all + int(flex[0]) + int(flex[2]);
            bot.send_message(message.chat.id, 'Напиши "ПОДТВЕРДИТЬ", чтобы завершить транзакцию. ')
        else:
            flex_all = flex_all + int(flex)
            bot.send_message(message.chat.id, 'Напиши "ПОДТВЕРДИТЬ", чтобы завершить транзакцию. ')
    elif flex[0] == '7':
        if flex[1] == '+':
            flex_all = flex_all + int(flex[0]) + int(flex[2]);
            bot.send_message(message.chat.id, 'Напиши "ПОДТВЕРДИТЬ", чтобы завершить транзакцию. ')
        else:
            flex_all = flex_all + int(flex)
            bot.send_message(message.chat.id, 'Напиши "ПОДТВЕРДИТЬ", чтобы завершить транзакцию. ')

    elif flex[0] == '8':
        if flex[1] == '+':
            flex_all = flex_all + int(flex[0]) + int(flex[2]);
            bot.send_message(message.chat.id, 'Напиши "ПОДТВЕРДИТЬ", чтобы завершить транзакцию. ')
        else:
            flex_all = flex_all + int(flex)
            bot.send_message(message.chat.id, 'Напиши "ПОДТВЕРДИТЬ", чтобы завершить транзакцию. ')
    elif flex[0] == '9':
        if flex[1] == '+':
            flex_all = flex_all + int(flex[0]) + int(flex[2]);
            bot.send_message(message.chat.id, 'Напиши "ПОДТВЕРДИТЬ", чтобы завершить транзакцию. ')
        else:
            flex_all = flex_all + int(flex)
            bot.send_message(message.chat.id, 'Напиши "ПОДТВЕРДИТЬ", чтобы завершить транзакцию. ')
    elif flex[0] == '0':
        if flex[1] == '+':
            flex_all = flex_all + int(flex[0]) + int(flex[2]);
            bot.send_message(message.chat.id, 'Напиши "ПОДТВЕРДИТЬ", чтобы завершить транзакцию. ')
        else:
            flex_all = flex_all + int(flex)
            bot.send_message(message.chat.id, 'Напиши "ПОДТВЕРДИТЬ", чтобы завершить транзакцию. ')
    elif flex[0] == '-':
        flex_all = flex_all + int(flex)
        bot.send_message(message.chat.id, 'Напиши "ПОДТВЕРДИТЬ", чтобы завершить транзакцию. ')
    else:
        bot.send_message(message.chat.id, 'Нормальное целое число, будьте добры. ', reply_to_message_id=message.message_id)
        bot.send_message(message.chat.id, 'Напиши "ПОДТВЕРДИТЬ", чтобы завершить транзакцию. ')


@bot.message_handler(commands=['get'])
def start_message(message):
    bot.send_message(message.chat.id, 'Окей, сейчас ты получишь флекс. Сколько ты хочешь? (Введи число флексов)')
    bot.register_next_step_handler(message, get_flex);

@bot.message_handler(commands=['leave'])
def start_message(message):
    bot.send_message(message.chat.id, 'Прощай, '+ message.from_user.username + '. Иперия будет помнить тебя.')
@bot.message_handler(commands=['grodno'])
def start_message(message):
    bot.restrict_chat_member(message.chat.id, message.from_user.id, until_date=time() + 600)
    bot.send_message(message.chat.id, 'Не, ну это бан', reply_to_message_id=message.message_id)

@bot.message_handler(commands=['join'])
def start_message(message):
    bot.send_message(message.chat.id, 'Поздравляю, теперь ты с нами :) ')


@bot.message_handler(commands=['ad'])
def start_message(message):
    bot.send_message(message.chat.id, random.choice(ad))

@bot.message_handler(commands=['surprise'])
def start_message(message):
    bot.send_audio(message.chat.id, audio=open('sukanezabudka.mp3', 'rb'))

@bot.message_handler(content_types=['photo'])
def start_message(message):
    bot.send_message(message.chat.id, 'Фото? У меня тоже есть фото', reply_to_message_id=message.message_id)
    bot.send_photo(message.chat.id, photo=open('dzugan.jpg', 'rb'))


@bot.message_handler(commands=['promo'])
def start_message(message):
    global promo_check
    promo_check = promo_check
    if promo_check == True:
        bot.send_message(message.chat.id, 'Введи промокод: ')
        bot.register_next_step_handler(message, get_promo);
        promo_check = False
    else:
         bot.send_message(message.chat.id, 'Ты уже использовал(а) этот промокод. ', reply_to_message_id=message.message_id)


def get_promo(message):
    global flex_all
    flex_all = flex_all
    promo_check = promo_buff
    if message.text == 'FLEX100':
        bot.send_message(message.chat.id, 'Получено 100 флекса.')
        flex_all = flex_all + 100
    else:
        bot.send_message(message.chat.id, 'Неверный промокод. ', reply_to_message_id=message.message_id)
        bot.send_message(message.chat.id, 'Введи промокод: ')
        bot.register_next_step_handler(message, get_promo);







@bot.message_handler(commands=['rofl'])
def start_message(message):
    #bot.send_message(message.chat.id, 'Дзугань уже рофлит. Подкинуть его номерок?')
    keyboard = types.InlineKeyboardMarkup();  # наша клавиатура
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes');  # кнопка «Да»
    keyboard.add(key_yes);  # добавляем кнопку в клавиатуру
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='no');
    keyboard.add(key_no);
    bot.send_message(message.chat.id, text='Дзугань уже рофлит. Подкинуть его номерок?', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes": #call.data это callback_data, которую мы указали при объявлении кнопки
        bot.send_message(call.message.chat.id, '*тут должен быть номер Ванечки*');
    elif call.data == "no":
        bot.send_message(call.message.chat.id, 'Ладно, пока он рофлит без тебя')

@bot.message_handler(content_types=['sticker'])
def start_message(message):
    bot.send_sticker(message.chat.id, 'https://github.com/TelegramBots/book/raw/master/src/docs/sticker-fred.webp')

@bot.message_handler(commands=['balance'])
def start_message(message):
    bot.send_message(message.chat.id, str(message.from_user.username) +', твой баланс: ' + str(flex_all) + ' флекса', reply_to_message_id=message.message_id)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        #bot.send_message(message.chat.id,
                 #       'КИРИЛЛ, ЕСЛИ ТЫ ЭТО ЧИТАЕШЬ, ТО ТЕБЕ ПОЛАГАЕТСЯ БАН, ТЫ МЕНЯ ДОСТАЛ СВОИМ ТЕКСТОМ. Ой, я же дружелюбный бот...')
       # bot.send_message(message.chat.id, 'Простите)))')
        bot.send_message(message.chat.id, 'Салам алейкум, '+str(message.from_user.username)+'. Бот нашей Империи на связи. Введи /help для справки :) ')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, товарищ. Империя не забудет тебя.')
    else:
        bot.send_message(714203526, message.from_user.username+' сказал(а): '+message.text)
  #bot.send_message(message.from_user.id, 'Ммм, это что-то новенькое. Такой команды я пока что не знаю' + smile +' (Возможно ты что-то написал(а) в группе) ')

def flex_reply(message):
    if message.text == 'ПОДТВЕРДИТЬ':
        bot.send_message(message.chat.id, 'Можешь проверять баланс.')
    else:
        bot.send_message(message.chat.id, 'Начисление не подтверждено. ')

bot.polling(none_stop=True, interval=0)
