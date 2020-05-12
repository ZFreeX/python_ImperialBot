from telebot import types
import requests
import telebot
import random
import sqlite3 as sql
import time


bot = telebot.TeleBot('722134226:AAGesDfeltaU7img9SoOn_Q0Oo4fN9NPhUQ')

print("BOT STARTED...")


last_review = 'https://youtu.be/3cUS75xEY80'



users =107


taban = 1


@bot.message_handler(content_types=['document'])
def start_message(message):
    bot.send_message(message.chat.id, 'Напоминаем, что в чате запрещено распространение платных аранжировок. ',
                     reply_to_message_id=message.message_id)
    time.sleep(10)
    bot.delete_message(message.chat.id, message.message_id)


try:
    @bot.message_handler(commands=['tab'])
    def start_message(message):
        print(message.chat.id)
        global taban
        if message.chat.id == -1001292652798:
            bot.send_sticker(message.chat.id,
                             'https://raw.githubusercontent.com/ZFreeX/ugglite_ota/master/Sticker.webp')
            taban = taban + 1
        # bot.send_message(message.chat.id, 'Хмм, кажется '+str(message.from_user.first_name)+' не прочитал правила группы. Что ж, читай ЗАКРЕПЛЕННОЕ СООБЩЕНИЕ или /rules в помощь.', reply_to_message_id=message.message_id)
        else:
            kb = types.InlineKeyboardMarkup()
            key_GD = types.InlineKeyboardButton(text='Грустный дэнс', callback_data='GD')
            key_Comet = types.InlineKeyboardButton(text='JONY - Комета', callback_data='Comet')
            key_JB = types.InlineKeyboardButton(text='Jingle Bells Rock', callback_data='JB')
            key_MM = types.InlineKeyboardButton(text='Magic Moments', callback_data='MM')
            key_ODT = types.InlineKeyboardButton(text='Old Town Road', callback_data='ODT')
            key_FD = types.InlineKeyboardButton(text='Falling Down', callback_data='FD')
            key_GPK = types.InlineKeyboardButton(text='Горы по колено', callback_data='GPK')
            key_CT = types.InlineKeyboardButton(text='Cheap Thrills', callback_data='CP')
            key_SAD = types.InlineKeyboardButton(text='SAD - XXX', callback_data='SAD')
            key_HAV = types.InlineKeyboardButton(text='Havana - Camilla Cabello', callback_data='HAV')
            key_SYW = types.InlineKeyboardButton(text='Say You Wont let Go', callback_data='SYW')
            key_SHNT = types.InlineKeyboardButton(text='Шантаж - Макс Корж', callback_data='SHNT')
            key_OOU = types.InlineKeyboardButton(text='One Of Us - Joan Osborne', callback_data='OOU')
            key_RS = types.InlineKeyboardButton(text='ROCKSTAR', callback_data='RS')
            key_MAL = types.InlineKeyboardButton(text="Малолетка - Макс Корж", callback_data='MAL')
            key_PR = types.InlineKeyboardButton(text="Прятки - HammAli & Navai", callback_data='PR')
            key_ASTR = types.InlineKeyboardButton(text="Astronomia - COFFIN DANCE MEME", callback_data='ASTR')

            kb.add(key_ASTR)
            kb.add(key_PR)
            kb.add(key_MAL)
            kb.add(key_RS)
            kb.add(key_OOU)
            kb.add(key_SHNT)
            kb.add(key_SYW)
            kb.add(key_HAV)
            kb.add(key_SAD)
            kb.add(key_CT)
            kb.add(key_GPK)
            kb.add(key_ODT)
            kb.add(key_Comet)
            kb.add(key_GD)
            kb.add(key_JB)
            kb.add(key_MM)
            bot.send_message(message.chat.id, 'Выбери произведение: ', reply_to_message_id=message.message_id,
                             reply_markup=kb)



    hitext = "👋🏻 Рады видеть тебя в нашем чате подписчиков канала 'Ваня научи' , посвящённому гитаре и фингерстайлу. 🎸                 \n\nПравила: \n\n1)   Зашёл - представся!   \n\n2) Обязательно поделись своими успехами в игре на гитаре.   \n\n3) Также в нашем чате ты найдёшь эксклюзивные табы, которые тебе выдаст наш супербот @VanyaNauchiBot. 🤖😜   \n\nДля получения табов пиши команду /tab . \n \n Ни в коем случае не распространяй  пиратские табы в этом чате \n \n Внимание! Большая просьба не засорять группу и общаться с ботом в личке 😉  \n \nУважай других участников группы, соблюдай тактичность, цензуру и рекламную чистоту! \n\nХэв фан! 😜🎸🔥"


    @bot.message_handler(commands=['test'])
    def start_message(message):
        bot.send_message(message.chat.id,
                         "Привет, " + message.from_user.first_name + hitext.format(message.from_user.first_name))


    @bot.message_handler(content_types=["new_chat_members"])
    def handler_new_member(message):
        user_name = message.new_chat_member.first_name
        bot.send_message(message.chat.id, "Привет, " + user_name + hitext.format(user_name))
        # bot.send_message(714203526, 'Новый учатсник: '+user_name+','+message.new_chat_member.id)


    @bot.message_handler(commands=['send'])
    def start_message(message):
        if message.chat.id == -1001292652798:
            bot.send_message(message.chat.id, '🤫')
        else:
            bot.send_message(message.chat.id, 'Секретная команда активирована. ')

            text = message.text.replace("/", "")
            text = text.replace("s", "")
            text = text.replace("e", "")
            text = text.replace("n", "")
            text = text.replace("d", "")

            bot.send_message(-1001292652798, text)
            bot.send_message(message.chat.id, 'Переслал) ')
            # bot.register_next_step_handler(message, send


    @bot.message_handler(commands=['rules'])
    def start_message(message):
        bot.send_message(message.chat.id,
                         '\n В первую очередь чат создан для общения 😁\n\n Здесь мы делимся своими видео на гитаре, развиваемся, указываем на ошибки и недочёты, помогаем их исправить, делимся опытом и поддерживаем друг друга, поэтому не стесняйся делиться своими успехами!  😎 \n\n  Также в нашем чате ты найдёшь эксклюзивные табы, которые тебе выдаст наш супербот @VanyaNauchiBot. 🤖😜 \n \n Для того чтобы получить табы достаточно написать команду /tab, и бот выдаст тебе список табов, а дальше решение за тобой. \n \n  РАСПРОСТРАНЕНИЕ/ПЕРЕПРОДАЖА ПИРАТСКИХ ТАБОВ В ЧАТЕ СТРОГО ЗАПРЕЩЕНО! \n \n  Внимание! Большая просьба не засорять группу и общаться с ботом в личке 😉 \n  \n Уважай других участников группы, соблюдай тактичность, цензуру и рекламную чистоту! \n \n Хэв фан! 😜🎸🔥 ',
                         reply_to_message_id=message.message_id)


    @bot.message_handler(commands=['admin'])
    def start_message(message):

        kb = types.ReplyKeyboardMarkup()
        kb.row('Рассылка', 'Участники')
        bot.send_message(message.chat.id, 'Привет админу :)', reply_markup=kb)


    @bot.message_handler(commands=['help'])
    def start_message(message):
        global users
        global indb
        bot.send_message(message.chat.id,
                         'Команды: \n /tab - получить бесплатные табы; \n /rules - правила чата; \n /last_review - самый свежий обзор с участием Вани \n /last_video - последний видос на канале "Ваня, научи!" ; \n /profile - получить информацию о твоем профиле; \n В дальшейшем список команд будет пополняться! ',
                         reply_to_message_id=message.message_id)
        print(message.chat.id)
        bot.send_message(714203526, str(message.from_user.first_name) + '"s id: ' + str(message.chat.id))
        bot.send_message(714203526, str(message.from_user.first_name) + ' сказал(а): ' + message.text)
        indb = False
        con = sql.connect('spv.db')

        with con:

            cur = con.cursor()

            cur.execute("CREATE TABLE IF NOT EXISTS `svb` (`username` STRING, `id` INTEGER, `urs` INTEGER)")

            cur.execute("SELECT * FROM `svb`")

            rows = cur.fetchall()

            for row in rows:
                if row[1] == message.chat.id:
                    indb = True
                    break

            if indb == False:
                username = message.from_user.username
                id = message.chat.id
                users = users + 1
                urs = users
                cur.execute(f"INSERT INTO `svb` VALUES ('{username}', '{id}', '{urs}')")
                bot.send_message(714203526, '+1 к базе')

            con.commit()
            cur.close()


    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, 'Привет) Напиши /help, чтобы узнать больше! ')


    string = ['Держи! ', 'Лови! ', 'Принимай) ', 'Как заказывали, сэр. ']


    @bot.message_handler(commands=['edit_review'])
    def start_message(message):
        bot.send_message(message.chat.id, 'Новая ссылка: ')
        bot.register_next_step_handler(message, edit_review)


    def edit_review(message):
        last_review = message.text


    @bot.message_handler(commands=['last_review'])
    def start_message(message):
        bot.send_message(message.chat.id, last_review)


    last_video = 'https://www.youtube.com/watch?v=dvu6ym9O8Yc'


    @bot.message_handler(commands=['last_video'])
    def start_message(message):
        bot.send_message(message.chat.id, last_video)


    """
    @bot.message_handler(commands=['edit_video'])
    def start_message(message):
        bot.send_message(message.chat.id, 'Новая ссылка последнего видео: ')
        bot.register_next_step_handler(message, edit_video(message))


    def edit_video(message):
        last_video = message.text
        bot.send_message(message.chat.id, 'Изменено. ')
    """


    @bot.callback_query_handler(func=lambda call: True)
    def callback_worker(call):
        if call.data == "MM":  # call.data это callback_data, которую мы указали при объявлении кнопки
            MM = open('Magic Moments.pdf', 'rb')
            bot.send_message(call.message.chat.id, random.choice(string))
            bot.send_document(call.message.chat.id, MM)
        elif call.data == "JB":  # call.data это callback_data, которую мы указали при объявлении кнопки
            JB = open('Jingle Bells Rock.pdf', 'rb')
            bot.send_message(call.message.chat.id, random.choice(string))
            bot.send_document(call.message.chat.id, JB)
        elif call.data == "Comet":  # call.data это callback_data, которую мы указали при объявлении кнопки
            Comet = open('Комета.pdf', 'rb')
            bot.send_message(call.message.chat.id, random.choice(string))
            bot.send_document(call.message.chat.id, Comet)
        elif call.data == "GD":  # call.data это callback_data, которую мы указали при объявлении кнопки
            GD = open('Грустный дэнс.pdf', 'rb')
            bot.send_message(call.message.chat.id, random.choice(string))
            bot.send_document(call.message.chat.id, GD)
        elif call.data == "ODT":  # call.data это callback_data, которую мы указали при объявлении кнопки
            ODT = open('Old_Town_Road.pdf', 'rb')
            bot.send_message(call.message.chat.id, random.choice(string))
            bot.send_document(call.message.chat.id, ODT)
        elif call.data == "FD":  # call.data это callback_data, которую мы указали при объявлении кнопки
            FD = open('Falling_Down.pdf', 'rb')
            bot.send_message(call.message.chat.id, random.choice(string))
            bot.send_document(call.message.chat.id, FD)
        elif call.data == "GPK":  # call.data это callback_data, которую мы указали при объявлении кнопки
            GPK = open('Горы_по_колено.pdf', 'rb')
            bot.send_message(call.message.chat.id, random.choice(string))
            bot.send_document(call.message.chat.id, GPK)
        elif call.data == "SAD":  # call.data это callback_data, которую мы указали при объявлении кнопки
            SAD = open('SAD_XXXTENTACION.pdf', 'rb')
            bot.send_message(call.message.chat.id, random.choice(string))
            bot.send_document(call.message.chat.id, SAD)
        elif call.data == "CP":  # call.data это callback_data, которую мы указали при объявлении кнопки
            CP = open('Cheap_Thrills.pdf', 'rb')
            bot.send_message(call.message.chat.id, random.choice(string))
            bot.send_document(call.message.chat.id, CP)
        elif call.data == "OOU":  # call.data это callback_data, которую мы указали при объявлении кнопки
            OOU = open('One_of_Us.pdf', 'rb')
            bot.send_message(call.message.chat.id, random.choice(string))
            bot.send_document(call.message.chat.id, OOU)

        elif call.data == "SHNT":  # call.data это callback_data, которую мы указали при объявлении кнопки
            SHNT = open('Шантаж.pdf', 'rb')
            bot.send_message(call.message.chat.id, random.choice(string))
            bot.send_document(call.message.chat.id, SHNT)
        elif call.data == "HAV":  # call.data это callback_data, которую мы указали при объявлении кнопки
            HAV = open('Havana.pdf', 'rb')
            bot.send_message(call.message.chat.id, random.choice(string))
            bot.send_document(call.message.chat.id, HAV)
        elif call.data == "SYW":  # call.data это callback_data, которую мы указали при объявлении кнопки
            SYW = open('Say_you_wont_let_Go.pdf', 'rb')
            bot.send_message(call.message.chat.id, random.choice(string))
            bot.send_document(call.message.chat.id, SYW)
        elif call.data == "RS":  # call.data это callback_data, которую мы указали при объявлении кнопки
            RS = open('Rockstar.pdf', 'rb')
            bot.send_message(call.message.chat.id, random.choice(string))
            bot.send_document(call.message.chat.id, RS)
        elif call.data == "MAL":  # call.data это callback_data, которую мы указали при объявлении кнопки
            MAL = open('Малолетка.pdf', 'rb')
            bot.send_message(call.message.chat.id, random.choice(string))
            bot.send_document(call.message.chat.id, MAL)
        elif call.data == "PR":  # call.data это callback_data, которую мы указали при объявлении кнопки
            PR = open('Прятки.pdf', 'rb')
            bot.send_message(call.message.chat.id, random.choice(string))
            bot.send_document(call.message.chat.id, PR)
        elif call.data == "ASTR":  # call.data это callback_data, которую мы указали при объявлении кнопки
            ASTR = open('Astronomia.pdf', 'rb')
            bot.send_message(call.message.chat.id, random.choice(string))
            bot.send_document(call.message.chat.id, ASTR)


    fingers = 0
    covers = 0
    chars = ['=', '*', '$', '~']
    smiles = ['(⌒‿⌒)', '(◕‿◕)', '(✯◡✯)', '(o˘◡˘o)']



    @bot.message_handler(commands=['profile'])
    def start_message(message):
        global fingers
        global cover
        fingers = 0
        covers = 0
        if message.from_user.first_name == 'Альба':
            fingers = 12
            covers = 2
        elif message.from_user.first_name == 'Виталий':
            fingers = 9
            covers = 1

        num = random.randint(0, 3)
        profiles = chars[num] * 28 + '\n' + message.from_user.first_name.center(30) + '\n' + chars[
            num] * 28 + '\n Заработанных фингебаллов: ' + str(fingers) + '\n ' + 'Записал каверов:' + str(
            covers) + '\n Ранг: \n  \n \n \n' + random.choice(smiles)
        # profiles = '='*30+'\n'+' '*int(((30-len(message.from_user.first_name))/2)) + message.from_user.first_name + '\n============================== \n Заработанных фингебаллов: \n ' + 'Записал каверов: \n Ранг: '
        bot.send_message(message.chat.id, profiles)


    @bot.message_handler(content_types=['text'])
    def send_text(message):
        bot.send_message(714203526, str(message.from_user.first_name) + ' ' + str(
            message.from_user.last_name) + ' сказал(а): ' + message.text)

        if message.text == 'Участники':
            bot.send_message(message.chat.id, 'Всего писавших боту: ' + str(users))

        if message.text == 'Рассылка':
            bot.send_message(message.chat.id, 'Текст рассылки: ')
            bot.register_next_step_handler(message, spam)


    def spam(message):
        con = sql.connect('spv.db')

        with con:
            cur = con.cursor()

            cur.execute("SELECT * FROM `svb`")

            rows = cur.fetchall()

            for row in rows:
                bot.send_message(row[1], message.text)

        con.commit()
        cur.close()
        bot.send_message(message.chat.id, "Разослал ;)")


    bot.polling(none_stop=True, interval=0)

except requests.exceptions.Timeout:
    print("Timeout occurred")
