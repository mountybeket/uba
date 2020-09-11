# - *- coding: utf- 8 - *-
import config
import telebot
from telebot import types
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

bot = telebot.TeleBot(config.token) #должно быть в начале. Вызывает токен

cred = credentials.Certificate("C:/Users/erhsh/Desktop/work/uba/key.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://ubabot-61ae0.firebaseio.com/' })

@bot.message_handler(commands=['start'])
def start_message(message):
    user_id = message.from_user.id
    current = db.reference("/bot/users/"+str(user_id)+"/current").get()

    bot.send_message(message.from_user.id,"Здравствуйте, введите название своего города/села:")
    db.reference("/bot/users/"+str(user_id)).update({"current": "who"})

@bot.message_handler(content_types = ['text'])
def start_dialog(message):
    user_id = message.from_user.id
    current = db.reference("/bot/users/"+str(user_id)+"/current").get()
    if current == "who":
        user_id = message.from_user.id
        user_markup = telebot.types.ReplyKeyboardMarkup(True)
        user_markup.row("Директор")
        user_markup.row("Завуч")
        user_markup.row("Учитель")
        user_markup.row("Ученик")
        user_markup.row("Методист")
        user_markup.row("Автор учебника")
        user_markup.row("Другое")
        db.reference("/bot/users/"+str(user_id)).update({"city": message.text})
        bot.send_message(user_id,"Кем вы являетесь?",reply_markup = user_markup)

        db.reference("/bot/users/"+str(user_id)).update({"current": "city"})

    elif current == "city":
        user_id = message.from_user.id
        user_markup = telebot.types.ReplyKeyboardMarkup(True)
        user_markup.row("Русский", "Қазақша")
        db.reference("/bot/users/"+str(user_id)).update({"who": message.text})
        bot.send_message(user_id,"Выберите язык:",reply_markup = user_markup)

        db.reference("/bot/users/"+str(user_id)).update({"current": "content"})

    elif current == "content":
        if message.text == "Русский":
            user_id = message.from_user.id
            user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
            user_markup.row("Нормативное правовое обеспечение")
            user_markup.row("Тенденции развития современного образования")
            user_markup.row("Педагог в системе образования")
            user_markup.row("Воспитательная работа")
            user_markup.row("Организация образовательного процесса в 2020-2021 учебном году")
            user_markup.row("Система оценивания учебных достижений")
            user_markup.row("Учебно-методическое обеспечение МКШ")
            user_markup.row("Цифровые образовательные ресурсы")
            user_markup.row("Апробация учебных программ в пилотных организациях образвания")
            user_markup.row("Приложения")
            user_markup.row("◀️ Назад")
            db.reference("/bot/users/"+str(user_id)).update({"lang": "Русский"})
            bot.send_message(user_id,"Содержание:",reply_markup = user_markup)

            db.reference("/bot/users/"+str(user_id)).update({"current": "block_2"})

        elif message.text == "Қазақша":
            user_id = message.from_user.id
            user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
            user_markup.row("Нормативтік-құқықтық қамтамасыз ету")
            user_markup.row("Қазіргі білім берудің дамуындағы тенденциялары")
            user_markup.row("Білім беру жүйесіндегі педагог")
            user_markup.row("Тәрбие жұмысы")
            user_markup.row("2020-2021 оқу жылында білім беру процесін ұйымдастыру")
            user_markup.row("Бағалау жүйесі")
            user_markup.row("Шағынжинақты мектепті оқу-әдістемелік қамтамасыз ету")
            user_markup.row("Ресурстар")
            user_markup.row("Пилоттық білім беру ұйымдарында бағдарламаларын сынақтан өткізу")
            user_markup.row("Қосымша")
            user_markup.row("◀️ Қайту")
            db.reference("/bot/users/"+str(user_id)).update({"lang": "Қазақша"})
            bot.send_message(user_id,"Мазмұны",reply_markup = user_markup)

            db.reference("/bot/users/"+str(user_id)).update({"current": "block_3"})

        else:
            bot.send_message(message.from_user.id,"Ошибка! Выберите из перечисленных.")

    elif current == "block_2":
        if message.text == "Нормативное правовое обеспечение":
            user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
            user_markup.row("НПА используемые в образовательном процессе")
            user_markup.row("Образовательный процесс в 1-4 кл")
            user_markup.row("Образовательный процесс в 5-11 кл")
            user_markup.row("НПА утвержденные в рамках принятия Закона «О статусе педагога» и др")
            user_markup.row("Каникулярные дни в 2020-2021 учебном году")
            user_markup.row("Ведение электронных журналов")
            user_markup.row("Внутришкольный контроль")
            user_markup.row("◀️ Назад")
            db.reference("/bot/users/"+str(user_id)).update({"current": "block_2/1"})
            bot.send_message(message.from_user.id,"Выберите:",reply_markup = user_markup)

        elif message.text == "Тенденции развития современного образования":
            user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
            user_markup.row("Комплекс системных мер по развитию образования и науки")
            user_markup.row("Ключевые позиции по совершенствованию системы")
            user_markup.row("Использование дистанционных образовательных технологий")
            user_markup.row("◀️ Назад")
            db.reference("/bot/users/"+str(user_id)).update({"current": "block_2/2"})
            bot.send_message(message.from_user.id,"Выберите:",reply_markup = user_markup)

        elif message.text == "Педагог в системе образования":
            user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
            user_markup.row("Статус педагога")
            user_markup.row("Личностные и профессиональные компетенции педагога")
            user_markup.row("Требования к квалификационным категориям")
            user_markup.row("◀️ Назад")
            db.reference("/bot/users/"+str(user_id)).update({"current": "block_2/3"})
            bot.send_message(message.from_user.id,"Выберите:",reply_markup = user_markup)

        elif message.text == "Воспитательная работа":
            user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
            user_markup.row("Основные нормативно-правовые документы")
            user_markup.row("Основные направления воспитательной работы в 2020-2021 у.г.")
            user_markup.row("Организация воспитательной работы в условиях ЧП")
            user_markup.row("Ресурсы по воспитательной работе")
            user_markup.row("◀️ Назад")
            db.reference("/bot/users/"+str(user_id)).update({"current": "block_2/4"})
            bot.send_message(message.from_user.id,"Выберите:",reply_markup = user_markup)

        elif message.text == "Организация образовательного процесса в 2020-2021 учебном году":
            user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
            user_markup.row("Группы и классы предшкольной подготовки")
            user_markup.row("Начальный уровень образования")
            user_markup.row("Основной средний уровень образования")
            user_markup.row("Общий средний уровень образования")
            user_markup.row("◀️ Назад")
            db.reference("/bot/users/"+str(user_id)).update({"current": "block_2/5"})
            bot.send_message(message.from_user.id,"Выберите:",reply_markup = user_markup)



        elif message.text == "Система оценивания учебных достижений":
            user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
            user_markup.row("Критериальная система оценивания учебных достижений обучающихся")
            user_markup.row("Оценивание учебных достижений обучающихся в условиях ограничительных мер")
            user_markup.row("Инструменты критериального оценивания")
            user_markup.row("ПАМЯТКА по выставлению формативных баллов")
            user_markup.row("Методические разработки по критериальному оцениванию")
            user_markup.row("Система оценивания учащихся специальных школ")
            user_markup.row("Проведение итоговой аттестации")
            user_markup.row("◀️ Назад")
            db.reference("/bot/users/"+str(user_id)).update({"current": "block_2/6"})
            bot.send_message(message.from_user.id,"Выберите:",reply_markup = user_markup)

        elif message.text == "Учебно-методическое обеспечение МКШ":
            bot.send_message(message.chat.id, '[Учебно-методическое обеспечение МКШ](https://telegra.ph/UCHEBNO-METODICHESKOE-OBESPECHENIE-MALOKOMPLEKTNYH-SHKOL-09-06)', parse_mode='Markdown')

        elif message.text == "Цифровые образовательные ресурсы":
            bot.send_message(message.chat.id, '[Цифровые образовательные ресурсы](https://telegra.ph/CIFROVYE-OBRAZOVATELNYE-RESURSY-09-06)', parse_mode='Markdown')


        elif message.text == "Апробация учебных программ в пилотных организациях образвания":
            bot.send_message(message.chat.id, '[Апробация учебных программ в пилотных организациях образвания](https://telegra.ph/APROBACIYA-UCHEBNYH-PROGRAMM-V-PILOTNYH-ORGANIZACIYAH-OBRAZOVANIYA-09-06)', parse_mode='Markdown')


        elif message.text == "Приложения":
                markup = types.InlineKeyboardMarkup()
                btn_docs= types.InlineKeyboardButton(text='Заявление', url='https://docs.google.com/document/d/1kmv3Q78lUNL_gNk1SOXh9eTApuIbKydvQsanS-R5ETc/edit?usp=sharing')
                btn_docs2= types.InlineKeyboardButton(text='Список рекомендованной литературы для педагогов', url='https://docs.google.com/document/d/1D9ve4VxbJZXxHKJpc6CWBfr7PSeMMo6u7euCmttbFXc/edit?usp=sharing')
                btn_docs3= types.InlineKeyboardButton(text='Қазақ тілінде оқытатын мектеп үшін қосымша оқуға арналған кітаптар', url='https://docs.google.com/document/d/1_UfCCZYFRaNb-otYYTV-Fi68t4P_MrnVwpWjQaW39R4/edit?usp=sharing')
                btn_docs4= types.InlineKeyboardButton(text='Лист наблюдения урока', url='https://docs.google.com/document/d/1jyAkHBda4ljcKivLQWjnTOpwo1VSI4UK0q4gkK0Fcxk/edit?usp=sharing')
                markup.add(btn_docs)
                markup.add(btn_docs2)
                markup.add(btn_docs3)
                markup.add(btn_docs4)
                bot.send_message(message.chat.id, "Приложения:", reply_markup = markup)

        elif message.text == "◀️ Назад":
            user_id = message.from_user.id
            user_markup = telebot.types.ReplyKeyboardMarkup(True)
            user_markup.row("Русский", "Қазақша")
            bot.send_message(user_id,"Выберите язык:",reply_markup = user_markup)

            db.reference("/bot/users/"+str(user_id)).update({"current": "content"})
        else:
            bot.send_message(message.from_user.id,"Ошибка! Выберите из перечисленных.")

    elif current == "block_2/1":
        if message.text == "НПА используемые в образовательном процессе":
            user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
            user_markup.row("Предшкольная подготовка")
            user_markup.row("1-4 классы")
            user_markup.row("5-9 классы")
            user_markup.row("10-11 классы")
            user_markup.row("◀️ Назад")
            db.reference("/bot/users/"+str(user_id)).update({"current": "block_2/1/2"})
            bot.send_message(message.from_user.id,"Выберите уровень образования:",reply_markup = user_markup)

        elif message.text == "Образовательный процесс в 1-4 кл":
            bot.send_message(message.chat.id, '[Образовательный процесс в 1-4 кл](https://telegra.ph/Obrazovatelnyj-process-v-1-4-h-klassah-budet-osushchestvlyatsya-na-osnove-09-05-2)', parse_mode='Markdown')


        elif message.text == "Образовательный процесс в 5-11 кл":
            bot.send_message(message.chat.id, '[Образовательный процесс в 5-11 кл](https://telegra.ph/Obrazovatelnyj-process-v-5-11-h-klassah-budet-osushchestvlyatsya-na-osnove-09-05)', parse_mode='Markdown')

        elif message.text == "НПА утвержденные в рамках принятия Закона «О статусе педагога» и др":
            bot.send_message(message.chat.id, '[НПА утвержденные в рамках принятия Закона «О статусе педагога» и др](https://telegra.ph/NPA-utverzhdennye-v-ramkah-prinyatiya-Zakona-O-statuse-pedagoga-i-drugie-obnovlennye-osnovnye-normativnye-dokumenty-09-05)', parse_mode='Markdown')

        elif message.text == "Каникулярные дни в 2020-2021 учебном году":
            user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
            user_markup.row("В 1-11 классах общеобразовательных школах")
            user_markup.row("В классах предшкольной подготовки")
            user_markup.row("◀️ Назад")
            db.reference("/bot/users/"+str(user_id)).update({"current": "block_2/1/2"})
            bot.send_message(message.from_user.id,"«Об определении начала, продолжительности и каникулярных периодов  2020-2021  учебного года в органзациях среднего образования»  приказ МОН РК от 12.08.20 года №340",reply_markup = user_markup)

        elif message.text == "Ведение электронных журналов":
            user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
            user_markup.row("Электронный журнал")
            user_markup.row("В журнал критериального оценивания выставляется")
            user_markup.row("Частотные вопросы по заполнению")

            user_markup.row("◀️ Назад")
            db.reference("/bot/users/"+str(user_id)).update({"current": "block_2/1/2"})
            bot.send_message(message.from_user.id,"Выберите:",reply_markup = user_markup)

        elif message.text == "Внутришкольный контроль":
            user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
            user_markup.row("План внутришкольного контроля на учебный год")
            user_markup.row("Нормативы внутришкольного контроля")
            user_markup.row("◀️ Назад")
            db.reference("/bot/users/"+str(user_id)).update({"current": "block_2/1/2"})
            bot.send_message(message.from_user.id,"Выберите уровень образования:",reply_markup = user_markup)


        elif message.text == "◀️ Назад":
            user_id = message.from_user.id
            user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
            user_markup.row("Нормативное правовое обеспечение")
            user_markup.row("Тенденции развития современного образования")
            user_markup.row("Педагог в системе образования")
            user_markup.row("Воспитательная работа")
            user_markup.row("Организация образовательного процесса в 2020-2021 учебном году")
            user_markup.row("Система оценивания учебных достижений")
            user_markup.row("Учебно-методическое обеспечение МКШ")
            user_markup.row("Цифровые образовательные ресурсы")
            user_markup.row("Апробация учебных программ в пилотных организациях образвания")
            user_markup.row("Приложения")
            user_markup.row("◀️ Назад")
            db.reference("/bot/users/"+str(user_id)).update({"lang": "Русский"})
            bot.send_message(user_id,"Содержание:",reply_markup = user_markup)

            db.reference("/bot/users/"+str(user_id)).update({"current": "block_2"})

        else:
            bot.send_message(message.from_user.id,"Ошибка! Выберите из перечисленных.")

    elif current == "block_2/1/2":
        if message.text == "Предшкольная подготовка":
            user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
            user_markup.row("Типовые учебные планы (П.П)")
            user_markup.row("Типовые учебные программы (П.П)")
            user_markup.row("◀️ Назад")
            db.reference("/bot/users/"+str(user_id)).update({"current": "block_2/1/2/1"})
            bot.send_message(message.from_user.id,"Выберите:",reply_markup = user_markup)


        elif message.text == "1-4 классы":
            user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
            user_markup.row("Типовые учебные планы (1-4)")
            user_markup.row("Типовые учебные программы (1-4)")
            user_markup.row("◀️ Назад")
            db.reference("/bot/users/"+str(user_id)).update({"current": "block_2/1/2/1"})
            bot.send_message(message.from_user.id,"Выберите:",reply_markup = user_markup)

        elif message.text == "5-9 классы":
            user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
            user_markup.row("Типовые учебные планы (5-9)")
            user_markup.row("Типовые учебные программы (5-9)")
            user_markup.row("◀️ Назад")
            db.reference("/bot/users/"+str(user_id)).update({"current": "block_2/1/2/1"})
            bot.send_message(message.from_user.id,"Выберите:",reply_markup = user_markup)

        elif message.text == "10-11 классы":
            user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
            user_markup.row("Типовые учебные планы (10-11)")
            user_markup.row("Типовые учебные программы (10-11)")
            user_markup.row("◀️ Назад")
            db.reference("/bot/users/"+str(user_id)).update({"current": "block_2/1/2/1"})
            bot.send_message(message.from_user.id,"Выберите:",reply_markup = user_markup)


###########################



        elif message.text == "В 1-11 классах общеобразовательных школах":
            bot.send_message(message.chat.id, "1) начало 2020 - 2021 учебного года - 1 сентября 2020 года; \n 2) продолжительность учебного года в 1 классах – 33 учебные недели, во 2-11 (12) классах – 34 учебные недели. Занятия, выпавшие на праздничные дни, переносятся на следующие дни с учетом интеграции содержания учебных программ за счет часов, отведенных на повторение; \n 3) каникулярные периоды в течение учебного года: \n в 1-11 (12) классах: осенние – 10 дней (со 5 по 14 ноября 2020 года включительно), зимние – 11 дней (с 31 декабря 2020 года по 10 января 2021 года включительно), весенние – 12 дней (с 20 по 31 марта 2021 года включительно); в 1 классах: дополнительные каникулы – 7 дней (с 8 по 14 февраля 2021 года включительно).")

        elif message.text == "В классах предшкольной подготовки":
            bot.send_message(message.chat.id, "Продолжительность учебного года в предшкольных классах 32 учебные недели. " \
                                                    "В предшкольных классах: \n" +
                                                    "осенние – 10 дней (с 5 по 14 ноября 2020 года включительно), " \
                                                    "зимние – 11 дней (с 31 декабря 2020 года по 10 января 2021 года включительно), " \
                                                    "весенние – 12 дней (с 20 по 31 марта 2021 года включительно), " \
                                                    "дополнительные каникулы – 7 дней (с 8 по14 февраля 2021 года включительно).")

############################


        elif message.text == "Электронный журнал":
            bot.send_message(message.chat.id, '[Электронный журнал](https://telegra.ph/EHlektronnyj-zhurnal-09-05)', parse_mode='Markdown')

        elif message.text == "В журнал критериального оценивания выставляется":
            bot.send_message(message.chat.id, "1. балл за формативное оценивание (от 1 до 10 баллов) с использованием комментариев для обратной связи; \n " \
                                                "2. балл за суммативную работу за раздел (СОР) – сумма набранных баллов и соответствующий уровень учебных достижений; \n" \
                                                "3. балл за суммативную работу за учебный период (СОЧ) – сумма набранных баллов согласно спецификации; \n " \
                                                "4. годовая оценка  – процентное соотношение набранной суммы баллов к максимально возможному баллу за все учебные периоды согласно шкале. \n ")

        elif message.text == "Частотные вопросы по заполнению":
            bot.send_message(message.chat.id, '[Частотные вопросы по заполнению](https://telegra.ph/CHastotnye-voprosy-po-zapolneniyu-ehlektronnogo-zhurnala-09-05)', parse_mode='Markdown')

##############################

        elif message.text == "План внутришкольного контроля на учебный год":
            bot.send_message(message.chat.id, "План внутришкольного контроля на учебный год составляется в " \
                                                    "соответствии с приложением 17 приказа Министра образования и науки Республики Казахстан " \
                                                    "«Об утверждении Перечня документов, обязательных для ведения педагогами организаций среднего, технического и профессионального, послесреднего образования, и их формы» от 6 апреля 2020 года № 130. \n" \
                                                    "Внутришкольный контроль  включает проверку выполнения ГОСО, Типовых учебных планов, Типовых учебных программ, среднесрочных, краткосрочных планов, личных дел обучающихся и т.д.")

        elif message.text == "Нормативы внутришкольного контроля":
            bot.send_message(message.chat.id, '[Нормативы внутришкольного контроля](https://telegra.ph/Normativy-vnutrishkolnogo-kontrolya-dlya-administracii-organizacij-obrazovaniya-09-05)', parse_mode='Markdown')



        elif message.text == "◀️ Назад":
            user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
            user_markup.row("НПА используемые в образовательном процессе")
            user_markup.row("Образовательный процесс в 1-4 кл")
            user_markup.row("Образовательный процесс в 5-11 кл")
            user_markup.row("НПА утвержденные в рамках принятия Закона «О статусе педагога» и др")
            user_markup.row("Каникулярные дни в 2020-2021 учебном году")
            user_markup.row("Ведение электронных журналов")
            user_markup.row("Внутришкольный контроль")
            user_markup.row("◀️ Назад")
            db.reference("/bot/users/"+str(user_id)).update({"current": "block_2/1"})
            bot.send_message(message.from_user.id,"Выберите:",reply_markup = user_markup)


        else:
            bot.send_message(message.from_user.id,"Ошибка! Выберите из перечисленных.")

    elif current == "block_2/1/2/1":
        if message.text == "Типовые учебные планы (П.П)":
                markup = types.InlineKeyboardMarkup()
                btn_docs= types.InlineKeyboardButton(text='12.12.2012   №557', url='http://adilet.zan.kz/rus/docs/V1200008275')
                markup.add(btn_docs)
                bot.send_message(message.chat.id, "Типовые учебные планы предшкольной программы:", reply_markup = markup)

        elif message.text == "Типовые учебные программы (П.П)":
                markup = types.InlineKeyboardMarkup()
                btn_docs= types.InlineKeyboardButton(text='12.08.2016    №499', url='http://adilet.zan.kz/rus/archive/docs/V1600014235/12.08.2016')
                markup.add(btn_docs)
                bot.send_message(message.chat.id, "Типовые учебные программы предшкольной программы:", reply_markup = markup)

        elif message.text == "Типовые учебные планы (1-4)":
                markup = types.InlineKeyboardMarkup()
                btn_docs= types.InlineKeyboardButton(text='8.11.2012    №500', url='http://adilet.zan.kz/rus/docs/V1200008170')
                btn_docs2= types.InlineKeyboardButton(text='(4.09.2018    №441)', url='http://adilet.zan.kz/rus/docs/V1200008170')
                markup.add(btn_docs)
                markup.add(btn_docs2)
                bot.send_message(message.chat.id, "Типовые учебные планы (1-4):", reply_markup = markup)

        elif message.text == "Типовые учебные программы (1-4)":
                markup = types.InlineKeyboardMarkup()
                btn_docs= types.InlineKeyboardButton(text='3.04.2013    №115', url='http://adilet.zan.kz/rus/docs/V1300008424')
                btn_docs2= types.InlineKeyboardButton(text='8.04.2016    №226', url='http://adilet.zan.kz/rus/docs/V1300008424')
                btn_docs3= types.InlineKeyboardButton(text='10.05.2018    №199', url='http://adilet.zan.kz/rus/docs/V1300008424')
                btn_docs4= types.InlineKeyboardButton(text='17.10.2018    №576', url='http://adilet.zan.kz/rus/docs/V1300008424')
                markup.add(btn_docs)
                markup.add(btn_docs2)
                markup.add(btn_docs3)
                markup.add(btn_docs4)
                bot.send_message(message.chat.id, "Типовые учебные программы (1-4):", reply_markup = markup)

        elif message.text == "Типовые учебные планы (5-9)":
                markup = types.InlineKeyboardMarkup()
                btn_docs= types.InlineKeyboardButton(text='8.11.2012   №500', url='http://adilet.zan.kz/rus/docs/V1200008170')
                btn_docs2= types.InlineKeyboardButton(text='(4.09.2018   №441)', url='http://adilet.zan.kz/rus/docs/V1200008170')
                btn_docs2= types.InlineKeyboardButton(text='(17.08.2020 г №350)', url='http://adilet.zan.kz/rus/docs/V2000021105#z7')
                markup.add(btn_docs)
                markup.add(btn_docs2)
                markup.add(btn_docs3)
                bot.send_message(message.chat.id, "Типовые учебные планы (5-9):", reply_markup = markup)

        elif message.text == "Типовые учебные программы (5-9)":
                markup = types.InlineKeyboardMarkup()
                btn_docs= types.InlineKeyboardButton(text='3.04.2013    №115', url='http://adilet.zan.kz/rus/docs/V1300008424')
                btn_docs2= types.InlineKeyboardButton(text='(25.10.2017   №545)', url='http://adilet.zan.kz/rus/docs/V1300008424')
                markup.add(btn_docs)
                markup.add(btn_docs2)
                bot.send_message(message.chat.id, "Типовые учебные программы (5-9):", reply_markup = markup)

        elif message.text == "Типовые учебные планы (10-11)":
                markup = types.InlineKeyboardMarkup()
                btn_docs= types.InlineKeyboardButton(text='8.11.2012   №500', url='http://adilet.zan.kz/rus/docs/V1200008170')
                btn_docs2= types.InlineKeyboardButton(text='4.09.2018    №441', url='http://adilet.zan.kz/rus/docs/V1200008170')
                btn_docs3= types.InlineKeyboardButton(text='15.05.2019  №205', url='http://adilet.zan.kz/rus/docs/V1900018705')
                markup.add(btn_docs)
                markup.add(btn_docs2)
                markup.add(btn_docs3)
                bot.send_message(message.chat.id, "Типовые учебные планы (10-11):", reply_markup = markup)

        elif message.text == "Типовые учебные программы (10-11)":
                markup = types.InlineKeyboardMarkup()
                btn_docs= types.InlineKeyboardButton(text='8.11.2012   №500', url='http://adilet.zan.kz/rus/docs/V1200008170')
                btn_docs2= types.InlineKeyboardButton(text='4.09.2018    №441', url='http://adilet.zan.kz/rus/docs/V1200008170')
                btn_docs3= types.InlineKeyboardButton(text='15.05.2019   №205', url='http://adilet.zan.kz/rus/docs/V1900018705')
                markup.add(btn_docs)
                markup.add(btn_docs2)
                markup.add(btn_docs3)
                bot.send_message(message.chat.id, "Типовые учебные программы (10-11):", reply_markup = markup)


        elif message.text == "◀️ Назад":
                user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
                user_markup.row("Предшкольная подготовка")
                user_markup.row("1-4 классы")
                user_markup.row("5-9 классы")
                user_markup.row("10-11 классы")
                user_markup.row("◀️ Назад")
                db.reference("/bot/users/"+str(user_id)).update({"current": "block_2/1/2"})
                bot.send_message(message.from_user.id,"Выберите уровень образования:",reply_markup = user_markup)

        else:
                bot.send_message(message.from_user.id,"Ошибка! Выберите из перечисленных.")



    elif current == "block_2/2":

        if message.text == "Комплекс системных мер по развитию образования и науки":
            bot.send_message(message.chat.id, '[Комплекс системных мер по развитию образования и науки](https://telegra.ph/Kompleks-sistemnyh-mer-po-razvitiyu-obrazovaniya-i-nauki-09-06)', parse_mode='Markdown')


        elif message.text == "Ключевые позиции по совершенствованию системы":
            bot.send_message(message.chat.id, "Ключевые позиции по совершенствованию системы среднего образования по ГПРОН на 2020-2025 годы. \n" \
                                                    "	завершение к переходу на обновленное содержание образования \n" \
                                                    "	новая система разработки, экспертизы и издания учебников \n" \
                                                    "	совершенствование критериальной системы оценивания \n" \
                                                    "	переход на 12-летнее образование \n" \
                                                    "	организация процесса обучения с использованием  дистанционных образовательных  технологий.")

        elif message.text == "Использование дистанционных образовательных технологий":
                user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
                user_markup.row("НПА по дистанционному обучению.")
                user_markup.row("Применение ДОТ")
                user_markup.row("Дистанционное обучение в условиях карантина")
                user_markup.row("Процесс обучения в условиях ограничительных мер")
                user_markup.row("Главы методических рекомендаций")
                user_markup.row("Ссылка на методические рекомендации")
                user_markup.row("◀️ Назад")
                db.reference("/bot/users/"+str(user_id)).update({"current": "block_2/2/1"})
                bot.send_message(message.from_user.id,"Выберите:",reply_markup = user_markup)


        elif message.text == "◀️ Назад":
            user_id = message.from_user.id
            user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
            user_markup.row("Нормативное правовое обеспечение")
            user_markup.row("Тенденции развития современного образования")
            user_markup.row("Педагог в системе образования")
            user_markup.row("Воспитательная работа")
            user_markup.row("Организация образовательного процесса в 2020-2021 учебном году")
            user_markup.row("Система оценивания учебных достижений")
            user_markup.row("Учебно-методическое обеспечение МКШ")
            user_markup.row("Цифровые образовательные ресурсы")
            user_markup.row("Апробация учебных программ в пилотных организациях образвания")
            user_markup.row("Приложения")
            user_markup.row("◀️ Назад")
            db.reference("/bot/users/"+str(user_id)).update({"lang": "Русский"})
            bot.send_message(user_id,"Содержание:",reply_markup = user_markup)

            db.reference("/bot/users/"+str(user_id)).update({"current": "block_2"})
        else:
                bot.send_message(message.from_user.id,"Ошибка! Выберите из перечисленных.")

    elif current == "block_2/2/1":

        if message.text == "НПА по дистанционному обучению.":
            bot.send_message(message.chat.id, "1) ГОСО утвержденное приказом  Министра образования и науки Республики Казахстан от 31 октября 2018 года № 604 \n" \
                                                    "2)	Закон Республики Казахстан «Об образовании» \n" \
                                                    "3)	Приказ Министра образования и науки Республики Казахстан от 20 марта 2015 года № 137 «Об утверждении Правил организации учебного процесса по дистанционным образовательным технологиям» \n" \
                                                    "4) Приказ Министра образования и науки Республики Казахстан от 28 августа 2020 года № 374 «О внесении изменения в приказ Министра образования и науки Республики Казахстан от 20 марта 2015 года № 137 «Об утверждении Правил организации учебного процесса по дистанционным образовательным технологиям» \n")
        elif message.text == "Применение ДОТ":
            bot.send_message(message.chat.id, "ДОТ применяются в отношении: \n" \
                                                    "1) лиц с особыми образовательными потребностями, в том числе детей-инвалидов, инвалидов детства, инвалидов I и II групп на всех уровнях образования; \n" \
                                                    "2) лиц, имеющих временные ограничения возможностей здоровья и не имеющих возможности регулярно посещать организации образования; \n" \
                                                    "3) осужденных, содержащихся в учреждениях уголовно-исполнительной системы и к наказаниям не связанным с лишением свободы при наличии соответствующих технических условий в учреждении. \n" \
                                                    "В 2020-2021 учебном году дистанционно обучаются учающиеся по образовательным программам дополнительного образования, среднего, технического и профессионального, послесреднего в условиях ограничительных мер соответствующих государственных органов, в том числе карантина, чрезвычайных ситуаций социального, природного и техногенного характера на основани")


        elif message.text == "Дистанционное обучение в условиях карантина":
            bot.send_message(message.chat.id, "В первой четверти 2020-2021 учебного года организация дистанционного обучения и обучение в штатном режиме реализуется на основе методических рекомендации утвержденного приказом МОН РК №345 от 13.08.20 г «Методические рекомендации по организации учебного процесса в организациях среднего образования в период ограничительных мер, связанных с распространением коронавирусной инфекции»")

        elif message.text == "Процесс обучения в условиях ограничительных мер":
            bot.send_message(message.chat.id, '[Процесс обучения в условиях ограничительных мер](https://telegra.ph/Osnovnye-trebovaniya-k-organizacii-processa-obucheniya-v-usloviyah-ogranichitelnyh-mer-09-06)', parse_mode='Markdown')

        elif message.text == "Главы методических рекомендаций":
            bot.send_message(message.chat.id, '[Главы методических рекомендаций](https://telegra.ph/Glavy-metodicheskih-rekomendacii-po-organizacii-uchebnogo-processa-v-organizaciyah-srednego-obrazovaniya-v-period-ogranichitelny-09-06)', parse_mode='Markdown')

        elif message.text == "Ссылка на методические рекомендации":
                markup = types.InlineKeyboardMarkup()
                btn_docs= types.InlineKeyboardButton(text='www.nao.kz', url='http://www.nao.kz/')
                markup.add(btn_docs)
                bot.send_message(message.chat.id, "Ссылка на методические рекомендации: ", reply_markup = markup)

        elif message.text == "◀️ Назад":
            user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
            user_markup.row("Комплекс системных мер по развитию образования и науки")
            user_markup.row("Ключевые позиции по совершенствованию системы")
            user_markup.row("Использование дистанционных образовательных технологий")
            user_markup.row("◀️ Назад")
            db.reference("/bot/users/"+str(user_id)).update({"current": "block_2/2"})
            bot.send_message(message.from_user.id,"Выберите:",reply_markup = user_markup)

        else:
            bot.send_message(message.from_user.id,"Ошибка! Выберите из перечисленных.")


    elif current == "block_2/3":

        if message.text == "Статус педагога":
            bot.send_message(message.chat.id, '[Статус педагога](https://telegra.ph/Status-pedagoga-09-06)', parse_mode='Markdown')

        elif message.text == "Личностные и профессиональные компетенции педагога":
            bot.send_message(message.chat.id, '[Личностные и профессиональные компетенции педагога](https://telegra.ph/Lichnostnye-i-professionalnye-kompetencii-pedagoga-09-06)', parse_mode='Markdown')


        elif message.text == "Требования к квалификационным категориям":
            bot.send_message(message.chat.id, "Проведение аттестации педагогов осуществляется в соответствии с приказом " \
                                                    "Министра образования и науки РК №83 от 27 января 2016 года (с изменениями и дополнениями от 14.05.2020 г №202). \n" \
                                                    "Правила и условия проведения аттестации педагогов, занимающих должности в организациях образования, реализующих общеобразовательные учебные программы дошкольного воспитания и обучения, начального, основного среднего и общего среднего образования, образовательные программы технического и профессионального, послесреднего, дополнительного, специализированного и специального образования, и иных гражданских служащих в области образования и науки изложены в новой редакции согласно приложению к приказу МОН РК №202 от 14 апреля 2020 года.")

        elif message.text == "◀️ Назад":
            user_id = message.from_user.id
            user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
            user_markup.row("Нормативное правовое обеспечение")
            user_markup.row("Тенденции развития современного образования")
            user_markup.row("Педагог в системе образования")
            user_markup.row("Воспитательная работа")
            user_markup.row("Организация образовательного процесса в 2020-2021 учебном году")
            user_markup.row("Система оценивания учебных достижений")
            user_markup.row("Учебно-методическое обеспечение МКШ")
            user_markup.row("Цифровые образовательные ресурсы")
            user_markup.row("Апробация учебных программ в пилотных организациях образвания")
            user_markup.row("Приложения")
            user_markup.row("◀️ Назад")
            db.reference("/bot/users/"+str(user_id)).update({"lang": "Русский"})
            bot.send_message(user_id,"Содержание:",reply_markup = user_markup)

            db.reference("/bot/users/"+str(user_id)).update({"current": "block_2"})
        else:
                bot.send_message(message.from_user.id,"Ошибка! Выберите из перечисленных.")


    elif current == "block_2/4":

        if message.text == "Основные нормативно-правовые документы":
            bot.send_message(message.chat.id, '[Основные нормативно-правовые документы](https://telegra.ph/Osnovnye-normativno-pravovye-dokumenty-09-09)', parse_mode='Markdown')

        elif message.text == "Основные направления воспитательной работы в 2020-2021 у.г.":
                user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
                user_markup.row("Воспитание казахстанского патриотизма, правовое воспитание")
                user_markup.row("Духовно-нравственное воспитание")
                user_markup.row("Национальное воспитание")
                user_markup.row("Семейное воспитание")
                user_markup.row("Трудовое, экономическое и экологическое воспитание")
                user_markup.row("Поликультурное и художественно-эстетическое воспитание")
                user_markup.row("Интеллектуальное воспитание")
                user_markup.row("Физическое воспитание")
                user_markup.row("◀️ Назад")
                db.reference("/bot/users/"+str(user_id)).update({"current": "block_2/4/1"})
                bot.send_message(message.from_user.id,"Выберите:",reply_markup = user_markup)


        elif message.text == "Организация воспитательной работы в условиях ЧП":
            bot.send_message(message.chat.id, '[Организация воспитательной работы в условиях ЧП](https://telegra.ph/Organizaciya-vospitatelnoj-raboty-v-usloviyah-chrezvychajnogo-polozheniya-09-06)', parse_mode='Markdown')


        elif message.text == "Ресурсы по воспитательной работе":
            bot.send_message(message.chat.id, "Все методические материалы по организации и проведению  воспитательной работы в организациях среднего образования  размещены на сайтах: https://www.nao.kz (раздел «Научно-методическое обеспечение образования. Методические пособия»),    https://iite.unesco.org/ru/  (раздел «Публикации»)")



        elif message.text == "◀️ Назад":
            user_id = message.from_user.id
            user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
            user_markup.row("Нормативное правовое обеспечение")
            user_markup.row("Тенденции развития современного образования")
            user_markup.row("Педагог в системе образования")
            user_markup.row("Воспитательная работа")
            user_markup.row("Организация образовательного процесса в 2020-2021 учебном году")
            user_markup.row("Система оценивания учебных достижений")
            user_markup.row("Учебно-методическое обеспечение МКШ")
            user_markup.row("Цифровые образовательные ресурсы")
            user_markup.row("Апробация учебных программ в пилотных организациях образвания")
            user_markup.row("Приложения")
            user_markup.row("◀️ Назад")
            db.reference("/bot/users/"+str(user_id)).update({"lang": "Русский"})
            bot.send_message(user_id,"Содержание:",reply_markup = user_markup)

            db.reference("/bot/users/"+str(user_id)).update({"current": "block_2"})
        else:
                bot.send_message(message.from_user.id,"Ошибка! Выберите из перечисленных.")

    elif current == "block_2/4/1":

        if message.text == "Воспитание казахстанского патриотизма, правовое воспитание":
                user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
                user_markup.row("Воспитание казахстанского патриотизма, правовое воспитание")
                user_markup.row("Материалы по популяризации краеведческих знаний среди обуч-ся")
                user_markup.row("Деятельность военно-патриотических клубов")
                user_markup.row("Правовое воспитание")
                user_markup.row("Инклюзивная культура")
                user_markup.row("◀️ Назад")
                db.reference("/bot/users/"+str(user_id)).update({"current": "block_2/4/1/1"})
                bot.send_message(message.from_user.id,"Выберите:",reply_markup = user_markup)


        elif message.text == "Духовно-нравственное воспитание":
                user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
                user_markup.row("Духовно-нравственное воспитание")
                user_markup.row("«Қоғамға қызмет»")
                user_markup.row("Формирование нравственных ценностей чтением книг")
                user_markup.row("◀️ Назад")
                db.reference("/bot/users/"+str(user_id)).update({"current": "block_2/4/1/2"})
                bot.send_message(message.from_user.id,"Выберите:",reply_markup = user_markup)


        elif message.text == "Национальное воспитание":
            bot.send_message(message.chat.id, '[Национальное воспитание](https://telegra.ph/Nacionalnoe-vospitanie-09-06)', parse_mode='Markdown')

        elif message.text == "Семейное воспитание":
            bot.send_message(message.chat.id, '[Семейное воспитание](https://telegra.ph/Semejnoe-vospitanie-09-06)', parse_mode='Markdown')

        elif message.text == "Трудовое, экономическое и экологическое воспитание":
            bot.send_message(message.chat.id, '[Трудовое, экономическое и экологическое воспитание](https://telegra.ph/Trudovoe-ehkonomicheskoe-i-ehkologicheskoe-vospitaniya-09-06)', parse_mode='Markdown')

        elif message.text == "Поликультурное и художественно-эстетическое воспитание":
            bot.send_message(message.chat.id, '[Поликультурное и художественно-эстетическое воспитание](https://telegra.ph/Polikulturnoe-i-hudozhestvenno-ehsteticheskoe-vospitanie-09-06)', parse_mode='Markdown')

        elif message.text == "Интеллектуальное воспитание":
            bot.send_message(message.chat.id, '[Интеллектуальное воспитание](https://telegra.ph/Intellektualnoe-vospitanie-09-06)', parse_mode='Markdown')

        elif message.text == "Физическое воспитание":
            bot.send_message(message.chat.id, '[Физическое воспитание](https://telegra.ph/Fizicheskoe-vospitanie-09-06)', parse_mode='Markdown')



        elif message.text == "◀️ Назад":
            user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
            user_markup.row("Основные нормативно-правовые документы")
            user_markup.row("Основные направления воспитательной работы в 2020-2021 у.г.")
            user_markup.row("Организация воспитательной работы в условиях ЧП")
            user_markup.row("Ресурсы по воспитательной работе")
            user_markup.row("◀️ Назад")
            db.reference("/bot/users/"+str(user_id)).update({"current": "block_2/4"})
            bot.send_message(message.from_user.id,"Выберите:",reply_markup = user_markup)
        else:
                bot.send_message(message.from_user.id,"Ошибка! Выберите из перечисленных.")


    elif current == "block_2/4/1/1":


        if message.text == "Воспитание казахстанского патриотизма, правовое воспитание":
            bot.send_message(message.chat.id, "Данное направление воспитательной работы формирует у обучающихся  чувства  патриотизма, правовое и гражданское самосознание; ценность индивидуальной свободы; ценность межчеловеческой и межгрупповой терпимости; недопустимость насилия и агрессии; ценность собственности и материального достатка; уважение к труду; уважение к жизни; недопустимость дискриминации разного рода, идею принципиального  равенства «равных и разных людей». \n " \
                                            "В рамках выполнения  данного направления воспитательной работы в 2020-2021 учебном году необходимо  продолжить реализацию  проекта \"Ұлы дала мұрагерлері\", включающего общереспубликанскую экспедицию \"Туған елге тағзым\"; социальных проектов \"Тарих тағылымы\" и \"Қазақ мәдениетінің антологиясы\", проекта «Духовные святыни Казахстана» («Сакральная география Казахстана»).   ")

        elif message.text == "Материалы по популяризации краеведческих знаний среди обуч-ся":
            bot.send_message(message.chat.id, '[Материалы по популяризации краеведческих знаний среди обуч-ся](https://telegra.ph/Materialy-po-populyarizacii-i-propagande-kraevedcheskih-znanij-sredi-obuchayushchihsya-09-06)', parse_mode='Markdown')

        elif message.text == "Деятельность военно-патриотических клубов":
            bot.send_message(message.chat.id, "       В целях  формирования и развития гражданственности и патриотизма у  обучающихся необходимо усилить работу по организации деятельности военно-патриотических клубов, детско-юношеских движений: «Жас қыран» (1-4 классы), «Жас Ұлан» (5-10-е классы), «Жас Сарбаз». В организациях среднего образования важно придать значимую   роль органам школьного самоуправления и выстроить работу по образцу работы Школьного комитета Единой детско-юношеской организации «Жас Ұлан». («Методические рекомендации по организации деятельности Республиканского Общественного Объединения «Единая детско-юношеская организация «Жас Ұлан»). \n" \
                                            "        Для повышения квалификации старших вожатых, ответственных за развитие детско-юношеского движения, рекомендуются авторские методические материалы и пособия по организации деятельности старших вожатых, размещенные на сайте www.zhasulan.kz в разделе «Копилка старшего вожатого» https://www.zhasulan.kz/kz/project/view?id=14.")



        elif message.text == "Правовое воспитание":
            bot.send_message(message.chat.id, '[Правовое воспитание](https://telegra.ph/Pravovoe-vospitanie-09-06)', parse_mode='Markdown')

        elif message.text == "Инклюзивная культура":
            bot.send_message(message.chat.id, '[Инклюзивная культура](https://telegra.ph/Inklyuzivnaya-kultura-09-06)', parse_mode='Markdown')


        elif message.text == "◀️ Назад":
                user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
                user_markup.row("Воспитание казахстанского патриотизма, правовое воспитание")
                user_markup.row("Духовно-нравственное воспитание")
                user_markup.row("Национальное воспитание")
                user_markup.row("Семейное воспитание")
                user_markup.row("Трудовое, экономическое и экологическое воспитание")
                user_markup.row("Поликультурное и художественно-эстетическое воспитание")
                user_markup.row("Интеллектуальное воспитание")
                user_markup.row("Физическое воспитание")
                user_markup.row("◀️ Назад")
                db.reference("/bot/users/"+str(user_id)).update({"current": "block_2/4/1"})
                bot.send_message(message.from_user.id,"Выберите:",reply_markup = user_markup)
        else:
                bot.send_message(message.from_user.id,"Ошибка! Выберите из перечисленных.")




    elif current == "block_2/4/1/2":


        if message.text == "Духовно-нравственное воспитание":
            bot.send_message(message.chat.id, "Духовно-нравственное воспитание формирует такие ценности как  нравственный облик, нравственное сознание; ценностные чувства и качества - гуманизм, совесть, честь, долг, вера, ответственность, товарищество, доброта, стыд, принципиальность, милосердие, солидарность, ценность национального согласия, уважения и почитания культуры, традиций и языка других народов; этически ответственное отношение к жизни.")

        elif message.text == "«Қоғамға қызмет»":
            bot.send_message(message.chat.id, '[«Қоғамға қызмет»](https://telegra.ph/Socialnyj-volonterskij-proekt-%D2%9Ao%D2%93am%D2%93a-%D2%9Byzmet-09-06)', parse_mode='Markdown')

        elif message.text == "Формирование нравственных ценностей чтением книг":
            bot.send_message(message.chat.id, '[Формирование нравственных ценностей чтением книг](https://telegra.ph/Formirovanie-sistemy-nravstvennyh-cennostej-cherez-chtenie-knig-09-06)', parse_mode='Markdown')

        elif message.text == "◀️ Назад":
                user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
                user_markup.row("Воспитание казахстанского патриотизма, правовое воспитание")
                user_markup.row("Духовно-нравственное воспитание")
                user_markup.row("Национальное воспитание")
                user_markup.row("Семейное воспитание")
                user_markup.row("Трудовое, экономическое и экологическое воспитание")
                user_markup.row("Поликультурное и художественно-эстетическое воспитание")
                user_markup.row("Интеллектуальное воспитание")
                user_markup.row("Физическое воспитание")
                user_markup.row("◀️ Назад")
                db.reference("/bot/users/"+str(user_id)).update({"current": "block_2/4/1"})
                bot.send_message(message.from_user.id,"Выберите:",reply_markup = user_markup)
        else:
                bot.send_message(message.from_user.id,"Ошибка! Выберите из перечисленных.")


    elif current == "block_2/5":

        if message.text == "Группы и классы предшкольной подготовки":
                user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
                user_markup.row("Нормативное правовое обеспечение дошкольного воспитания и обучения")
                user_markup.row("Изменения и дополнения в нормативных правовых актах")
                user_markup.row("Организация воспитательно-образовательного процесса")
                user_markup.row("Рекомендации по организации воспитательно-образовательного процесса")
                user_markup.row("Методологическое и методическое обеспечение системы")
                user_markup.row("Организация  работы дежурных групп в дошкольных организациях")


                user_markup.row("◀️ Назад")
                db.reference("/bot/users/"+str(user_id)).update({"current": "block_2/5/1"})
                bot.send_message(message.from_user.id,"Основные задачи воспитательно-образовательного процесса: \n - формирование и развитие двигательных, коммуникативных, познавательных, творческих умений и навыков, навыков социализации у детей дошкольного возраста; \n - создание безопасной образовательной среды в воспитательно-образовательном процессе; \n - создание равных стартовых возможностей для успешной подготовки воспитанников к обучению в школе; \n - формирование духовно-нравственных навыков, основанных на национальных традициях и общечеловеческих ценностях, в рамках реализации программы «Рухани жаңғыру».",reply_markup = user_markup)


        elif message.text == "Начальный уровень образования":
                user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
                user_markup.row("Образовательная область «Язык и Литература»")
                user_markup.row("Образовательная область «Математика и Информатика»")
                user_markup.row("Образовательная область «Естествознание»")
                user_markup.row("Образовательная область «Человек и общество»")
                user_markup.row("Образовательная область «Технология и искусство»")
                user_markup.row("Образовательная область «Физическая культутра»")
                user_markup.row("Инклюзивное образование")
                user_markup.row("Специальное образование")
                user_markup.row("◀️ Назад")
                db.reference("/bot/users/"+str(user_id)).update({"current": "block_2/5/2"})
                bot.send_message(message.from_user.id,'[Начальный уровень образования](https://telegra.ph/Nachalnyj-uroven-obrazovaniya-09-09)',parse_mode='Markdown', reply_markup = user_markup)

        elif message.text == "Основной средний уровень образования":
                user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
                user_markup.row("Образовательная область «Язык и Литература»")
                user_markup.row("Образовательная область «Математика и Информатика»")
                user_markup.row("Образовательная область «Естествознание»")
                user_markup.row("Образовательная область «Человек и общество»")
                user_markup.row("Образовательная область «Технология и искусство»")
                user_markup.row("Образовательная область «Физическая культутра»")
                user_markup.row("Инклюзивное образование")
                user_markup.row("Специальное образование")
                user_markup.row("◀️ Назад")
                db.reference("/bot/users/"+str(user_id)).update({"current": "block_2/5/3"})
                bot.send_message(message.from_user.id,'[Основной средний уровень образования](https://telegra.ph/OSOBENNOSTI-ORGANIZACII-OBRAZOVATELNOGO-PROCESSA-V-5-9-KLASSAH-09-09)',parse_mode='Markdown', reply_markup = user_markup)

        elif message.text == "Общий средний уровень образования":
                user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
                user_markup.row("Образовательная область «Язык и Литература»")
                user_markup.row("Образовательная область «Математика и Информатика»")
                user_markup.row("Образовательная область «Естествознание»")
                user_markup.row("Образовательная область «Человек и общество»")
                user_markup.row("Образовательная область «Физическая культутра»")
                user_markup.row("Инклюзивное образование")
                user_markup.row("◀️ Назад")
                db.reference("/bot/users/"+str(user_id)).update({"current": "block_2/5/4"})
                bot.send_message(message.from_user.id,'[Общий средний уровень образования](https://telegra.ph/OBSHCHIJ-SREDNIJ-UROVEN-OBRAZOVANIYA-09-09)',parse_mode='Markdown', reply_markup = user_markup)



        elif message.text == "◀️ Назад":
            user_id = message.from_user.id
            user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
            user_markup.row("Нормативное правовое обеспечение")
            user_markup.row("Тенденции развития современного образования")
            user_markup.row("Педагог в системе образования")
            user_markup.row("Воспитательная работа")
            user_markup.row("Организация образовательного процесса в 2020-2021 учебном году")
            user_markup.row("Система оценивания учебных достижений")
            user_markup.row("Учебно-методическое обеспечение МКШ")
            user_markup.row("Цифровые образовательные ресурсы")
            user_markup.row("Апробация учебных программ в пилотных организациях образвания")
            user_markup.row("Приложения")
            user_markup.row("◀️ Назад")
            db.reference("/bot/users/"+str(user_id)).update({"lang": "Русский"})
            bot.send_message(user_id,"Содержание:",reply_markup = user_markup)

            db.reference("/bot/users/"+str(user_id)).update({"current": "block_2"})
        else:
                bot.send_message(message.from_user.id,"Ошибка! Выберите из перечисленных.")



    elif current == "block_2/5/1":


        if message.text == "Нормативное правовое обеспечение дошкольного воспитания и обучения":
            bot.send_message(message.chat.id, '[Нормативное правовое обеспечение дошкольного воспитания и обучения](https://telegra.ph/Normativnoe-pravovoe-obespechenie-doshkolnogo-vospitaniya-i-obucheniya-09-09)', parse_mode='Markdown')

        elif message.text == "Изменения и дополнения в нормативных правовых актах":
            bot.send_message(message.chat.id, '[Изменения и дополнения в нормативных правовых актах](https://telegra.ph/Izmeneniya-i-dopolneniya-v-normativnyh-pravovyh-aktah-09-09)', parse_mode='Markdown')

        elif message.text == "Организация воспитательно-образовательного процесса":
            bot.send_message(message.chat.id, '[Организация воспитательно-образовательного процесса](https://telegra.ph/Organizaciya-vospitatelno-obrazovatelnogo-processa-09-09)', parse_mode='Markdown')

        elif message.text == "Рекомендации по организации воспитательно-образовательного процесса":
            bot.send_message(message.chat.id, '[Рекомендации по организации воспитательно-образовательного процесса](https://telegra.ph/Rekomendacii-po-organizacii-vospitatelno-obrazovatelnogo-processa-s-detmi-doshkolnogo-vozrasta-v-period-ogranichitelnyh-mer-09-09)', parse_mode='Markdown')


        elif message.text == "Методологическое и методическое обеспечение системы":
            bot.send_message(message.chat.id, '[Методологическое и методическое обеспечение системы](https://telegra.ph/Metodologicheskoe-i-metodicheskoe-obespechenie-sistemy-doshkolnogo-vospitaniya-i-obucheniya-09-09)', parse_mode='Markdown')


        elif message.text == "Организация  работы дежурных групп в дошкольных организациях":
            bot.send_message(message.chat.id, '[Организация  работы дежурных групп в дошкольных организациях](https://telegra.ph/Organizaciya-raboty-dezhurnyh-grupp-v-doshkolnyh-organizaciyah-09-09)', parse_mode='Markdown')


        elif message.text == "◀️ Назад":

            user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
            user_markup.row("Группы и классы предшкольной подготовки")
            user_markup.row("Начальный уровень образования")
            user_markup.row("Основной средний уровень образования")
            user_markup.row("Общий средний уровень образования")
            user_markup.row("◀️ Назад")
            db.reference("/bot/users/"+str(user_id)).update({"current": "block_2/5"})
            bot.send_message(message.from_user.id,"Выберите:",reply_markup = user_markup)

        else:
                bot.send_message(message.from_user.id,"Ошибка! Выберите из перечисленных.")



    elif current == "block_2/5/2":


        if message.text == "Образовательная область «Язык и Литература»":
                user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
                user_markup.row("Обучение грамоте")
                user_markup.row("Русский язык (Я1)")
                user_markup.row("Литературное чтение")
                user_markup.row("Казахский язык (Т2)")
                user_markup.row("Иностранный язык")
                user_markup.row("◀️ Назад")
                db.reference("/bot/users/"+str(user_id)).update({"current": "block_2/5/2/1"})
                bot.send_message(message.from_user.id,"        Содержание образовательной области «Язык и литература» реализуется в учебных предметах: «Обучение грамоте», «Қазақ тілі (Т1)», «Русский язык (Я1)» «Әдебиеттік оқу», «Литературное чтение», «Казахский язык (Т2)» в классах с неказахским языком обучения», «Русский язык (Я2)» в классах с казахским языком обучения, «Иностранный язык». \n        При изучении языковых учебных предметов реализуется коммуникативный подход. Коммуникативный подход нацелен на развитие читательской грамотности обучающихся, т.е. на развитие способности к осмыслению текстов и их рефлексии, к использованию их содержания для достижения собственных целей, развития знаний и возможностей, для активного участия в жизни общества.",reply_markup = user_markup)

        elif message.text == "Образовательная область «Математика и Информатика»":
                user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
                user_markup.row("Математика")
                user_markup.row("Информационно-коммуникационные технологии")
                user_markup.row("◀️ Назад")
                db.reference("/bot/users/"+str(user_id)).update({"current": "block_2/5/2/1"})
                bot.send_message(message.from_user.id,"Содержание образовательной области «Математика и информатика» реализуется в учебных предметах: «Математика» и «Информационно-коммуникационные технологии».",reply_markup = user_markup)

        elif message.text == "Образовательная область «Естествознание»":
            bot.send_message(message.chat.id, '[Образовательная область «Естествознание»](https://telegra.ph/Uchebnyj-predmet-Estestvoznanie-09-09)', parse_mode='Markdown')


        elif message.text == "Образовательная область «Человек и общество»":
                user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
                user_markup.row("Познание мира")
                user_markup.row("Самопознание")
                user_markup.row("◀️ Назад")
                db.reference("/bot/users/"+str(user_id)).update({"current": "block_2/5/2/1"})
                bot.send_message(message.from_user.id,"В образовательную область «Человек и общество» входят предметы «Познание мира» и «Самопознание».",reply_markup = user_markup)

        elif message.text == "Образовательная область «Технология и искусство»":
                user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
                user_markup.row("Музыка")
                user_markup.row("Художественный труд")
                user_markup.row("◀️ Назад")
                db.reference("/bot/users/"+str(user_id)).update({"current": "block_2/5/2/1"})
                bot.send_message(message.from_user.id,"Выберите:",reply_markup = user_markup)

        elif message.text == "Образовательная область «Физическая культутра»":
            bot.send_message(message.chat.id, '[Образовательная область «Физическая культутра»](https://telegra.ph/Uchebnyj-predmet-Fizicheskaya-kultura-09-09)', parse_mode='Markdown')

        elif message.text == "Инклюзивное образование":
            bot.send_message(message.chat.id, '[Инклюзивное образование](https://telegra.ph/Inklyuzivnoe-obrazovanie-v-nachalnyh-klassah-09-09)', parse_mode='Markdown')

        elif message.text == "Специальное образование":
            user_id = message.from_user.id
            user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
            user_markup.row("НПА специальных школ на уровне начальных классов")
            user_markup.row("Продолжительность учебного года  и  учебно-методическое обеспечение процесса обучения")
            user_markup.row("Перечень разделов и учебных дисциплин Типового учебного плана")
            user_markup.row("Индивидуальная учебная программа")
            user_markup.row("Деятельность педагога начальных классов в системе специального образования")
            user_markup.row("Учебно-воспитательный процесс в специальной школе/классе")
            user_markup.row("Учебные и коррекционные занятия для детей, обучающихся вне организации образования")
            user_markup.row("◀️ Назад")
            bot.send_message(user_id,"Обучение школьников в специальных школах / классах организуется по видам нарушений развития: \n – для детей с нарушением слуха; \n – для детей с нарушением зрения; \n – для детей с тяжелыми нарушениями речи; \n – для детей с нарушениями опорно-двигательного аппарата; \n – для детей с задержкой психического развития (далее – ЗПР); \n – для детей с нарушением интеллекта (легкая и умеренная умственная отсталость).",reply_markup = user_markup)

            db.reference("/bot/users/"+str(user_id)).update({"current": "block_2/5/2/1"})


        elif message.text == "◀️ Назад":

            user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
            user_markup.row("Группы и классы предшкольной подготовки")
            user_markup.row("Начальный уровень образования")
            user_markup.row("Основной средний уровень образования")
            user_markup.row("Общий средний уровень образования")
            user_markup.row("◀️ Назад")
            db.reference("/bot/users/"+str(user_id)).update({"current": "block_2/5"})
            bot.send_message(message.from_user.id,"Выберите:",reply_markup = user_markup)

        else:
                bot.send_message(message.from_user.id,"Ошибка! Выберите из перечисленных.")


    elif current == "block_2/5/2/1":

        if message.text == "Обучение грамоте":
            bot.send_message(message.chat.id, '[Обучение грамоте](https://telegra.ph/Uchebnyj-predmet-Obuchenie-gramote-s-russkim-yazykom-obucheniya-09-09)', parse_mode='Markdown')

        elif message.text == "Русский язык (Я1)":
            bot.send_message(message.chat.id, '[Русский язык (Я1)](https://telegra.ph/Uchebnyj-predmet-Russkij-yazyk-YA1-s-russkim-yazykom-obucheniya-09-09)', parse_mode='Markdown')

        elif message.text == "Литературное чтение":
            bot.send_message(message.chat.id, '[Литературное чтение](https://telegra.ph/Uchebnyj-predmet-Literaturnoe-chtenie-s-russkim-yazykom-obucheniya-09-09)', parse_mode='Markdown')

        elif message.text == "Казахский язык (Т2)":
            bot.send_message(message.chat.id, '[Казахский язык (Т2)](https://telegra.ph/Uchebnyj-predmet-Kazahskij-yazyk-T2-09-10)', parse_mode='Markdown')

        elif message.text == "Иностранный язык":
            bot.send_message(message.chat.id, '[Иностранный язык](https://telegra.ph/Uchebnyj-predmet-Inostrannyj-yazyk-09-09)', parse_mode='Markdown')

        elif message.text == "Математика":
            bot.send_message(message.chat.id, '[Математика](https://telegra.ph/Uchebnyj-predmet-Matematika-09-09)', parse_mode='Markdown')

        elif message.text == "Информационно-коммуникационные технологии":
            bot.send_message(message.chat.id, '[Информационно-коммуникационные технологии](https://telegra.ph/Uchebnyj-predmet-Informacionno-kommunikacionnye-tehnologii-09-09)', parse_mode='Markdown')

        elif message.text == "Познание мира":
            bot.send_message(message.chat.id, '[Познание мира](https://telegra.ph/Uchebnyj-predmet-Poznanie-mira-09-09)', parse_mode='Markdown')

        elif message.text == "Самопознание":
            bot.send_message(message.chat.id, '[Самопознание](https://telegra.ph/Uchebnyj-predmet-Samopoznanie-09-09)', parse_mode='Markdown')

        elif message.text == "Музыка":
            bot.send_message(message.chat.id, '[Музыка](https://telegra.ph/Uchebnyj-predmet-Muzyka-09-09)', parse_mode='Markdown')

        elif message.text == "Художественный труд":
            bot.send_message(message.chat.id, '[Художественный труд](https://telegra.ph/Uchebnyj-predmet-Hudozhestvennyj-trud-09-09)', parse_mode='Markdown')

        elif message.text == "НПА специальных школ на уровне начальных классов":
            bot.send_message(message.chat.id, '[НПА специальных школ на уровне начальных классов](https://telegra.ph/NPA-specialnyh-shkol-na-urovne-nachalnyh-klassov-09-09)', parse_mode='Markdown')

        elif message.text == "Продолжительность учебного года  и  учебно-методическое обеспечение процесса обучения":
            bot.send_message(message.chat.id, '[Продолжительность учебного года  и  учебно-методическое обеспечение процесса обучения](https://telegra.ph/Prodolzhitelnost-uchebnogo-goda-i-uchebno-metodicheskoe-obespechenie-processa-obucheniya-09-09)', parse_mode='Markdown')

        elif message.text == "Перечень разделов и учебных дисциплин Типового учебного плана":
            bot.send_message(message.chat.id, '[Перечень разделов и учебных дисциплин Типового учебного плана](https://telegra.ph/Perechen-razdelov-i-uchebnyh-disciplin-Tipovogo-uchebnogo-plana-09-09)', parse_mode='Markdown')

        elif message.text == "Индивидуальная учебная программа":
            bot.send_message(message.chat.id, '[Индивидуальная учебная программа](https://telegra.ph/Individualnaya-uchebnaya-programma-09-09)', parse_mode='Markdown')

        elif message.text == "Деятельность педагога начальных классов в системе специального образования":
            bot.send_message(message.chat.id, '[Деятельность педагога начальных классов в системе специального образования](https://telegra.ph/Deyatelnost-pedagoga-nachalnyh-klassov-v-sisteme-specialnogo-obrazovaniya-09-09)', parse_mode='Markdown')

        elif message.text == "Учебно-воспитательный процесс в специальной школе/классе":
            bot.send_message(message.chat.id, '[Учебно-воспитательный процесс в специальной школе/классе](https://telegra.ph/Uchebno-vospitatelnyj-process-v-specialnoj-shkoleklasse-09-09)', parse_mode='Markdown')

        elif message.text == "Учебные и коррекционные занятия для детей, обучающихся вне организации образования":
            bot.send_message(message.chat.id, '[Учебные и коррекционные занятия для детей, обучающихся вне организации образования](https://telegra.ph/Uchebnye-i-korrekcionnye-zanyatiya-organizuyutsya-dlya-detej-prohodyashchih-kurs-lecheniya-v-uchrezhdeniyah-zdravoohraneniya-i-o-09-09)', parse_mode='Markdown')


        elif message.text == "◀️ Назад":

                user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
                user_markup.row("Образовательная область «Язык и Литература»")
                user_markup.row("Образовательная область «Математика и Информатика»")
                user_markup.row("Образовательная область «Естествознание»")
                user_markup.row("Образовательная область «Человек и общество»")
                user_markup.row("Образовательная область «Технология и искусство»")
                user_markup.row("Образовательная область «Физическая культутра»")
                user_markup.row("Инклюзивное образование")
                user_markup.row("Специальное образование")
                user_markup.row("◀️ Назад")
                db.reference("/bot/users/"+str(user_id)).update({"current": "block_2/5/2"})
                bot.send_message(message.from_user.id,"Выбери: ",reply_markup = user_markup)

        else:
                bot.send_message(message.from_user.id,"Ошибка! Выберите из перечисленных.")


    elif current == "block_2/5/3":


        if message.text == "Образовательная область «Язык и Литература»":
                user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
                user_markup.row("Русский язык")
                user_markup.row("Русская литература")
                user_markup.row("Қазақ тілі мен әдебиеті")
                user_markup.row("Иностранный язык")
                user_markup.row("◀️ Назад")
                db.reference("/bot/users/"+str(user_id)).update({"current": "block_2/5/3/1"})
                bot.send_message(message.from_user.id,"        В РАМКАХ ОБРАЗОВАТЕЛЬНОЙ ОБЛАСТИ «ЯЗЫК И ЛИТЕРАТУРА» ИЗУЧАЮТСЯ СЛЕДУЮЩИЕ ПРЕДМЕТЫ:\n"
                                                      "         «Қазақ тілі», «Русский язык», «Қазақ әдебиеті», «Русская литература», «Қазақ тілі мен әдебиеті», «Русский язык и литература», «Родной язык», «Уйгурская/Узбекская/Таджикская литература»,  «Иностранный язык».",reply_markup = user_markup)

        elif message.text == "Образовательная область «Математика и Информатика»":
            bot.send_message(message.chat.id, '[Образовательная область «Математика и Информатика»](https://telegra.ph/OBRAZOVATELNAYA-OBLAST-MATEMATIKA-I-INFORMATIKA-09-09)', parse_mode='Markdown')
            bot.send_message(message.chat.id, '[Информатика»](https://telegra.ph/Uchebnyj-predmet-Informatika-09-09)', parse_mode='Markdown')


        elif message.text == "Образовательная область «Естествознание»":
                user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
                user_markup.row("Естествознание")
                user_markup.row("Физика")
                user_markup.row("География")
                user_markup.row("Биология")
                user_markup.row("Химия")
                user_markup.row("◀️ Назад")
                db.reference("/bot/users/"+str(user_id)).update({"current": "block_2/5/3/1"})
                bot.send_message(message.from_user.id,'[Образовательная область «Естествознание»](https://telegra.ph/OBRAZOVATELNAYA-OBLAST-ESTESTVOZNANIE-09-09)',parse_mode='Markdown', reply_markup = user_markup)


        elif message.text == "Образовательная область «Человек и общество»":
                user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
                user_markup.row("История Казахстана и Всемирная история")
                user_markup.row("Основы права")
                user_markup.row("Светскость и основы религиоведения")
                user_markup.row("Самопознание")

                user_markup.row("◀️ Назад")
                db.reference("/bot/users/"+str(user_id)).update({"current": "block_2/5/3/1"})
                bot.send_message(message.from_user.id,"    Содержание учебных предметов образовательной области «Человек и общество» реализуется в учебных предметах «История Казахстана», «Всемирная история», «Основы права», «Самопознание». \n" \
                                                      "    Содержание образовательной области «Человек и общество»  направлено на формирование у обучающихся основ знаний по общественно- гуманитарным наукам в рамках системы «Человек – Общество».",reply_markup = user_markup)

        elif message.text == "Образовательная область «Технология и искусство»":
                user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
                user_markup.row("Музыка")
                user_markup.row("Художественный труд")
                user_markup.row("◀️ Назад")
                db.reference("/bot/users/"+str(user_id)).update({"current": "block_2/5/3/1"})
                bot.send_message(message.from_user.id,"В рамках образовательной области «Искусство» изучаются следующие предметы: «Музыка» – 5, 6-е классы, «Художественный труд» – 7-9-е классы.",reply_markup = user_markup)

        elif message.text == "Образовательная область «Физическая культутра»":
            bot.send_message(message.chat.id, '[Образовательная область «Физическая культутра](https://telegra.ph/OBRAZOVATELNAYA-OBLAST-FIZICHESKAYA-KULTURA-09-09)', parse_mode='Markdown')

        elif message.text == "Инклюзивное образование":
            bot.send_message(message.chat.id, '[Инклюзивное образование](https://telegra.ph/Inklyuzivnoe-obrazovanie-09-09)', parse_mode='Markdown')

        elif message.text == "Специальное образование":
            bot.send_message(message.chat.id, '[Специальное образование](https://telegra.ph/Specialnoe-obrazovanie-09-09)', parse_mode='Markdown')


        elif message.text == "◀️ Назад":

            user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
            user_markup.row("Группы и классы предшкольной подготовки")
            user_markup.row("Начальный уровень образования")
            user_markup.row("Основной средний уровень образования")
            user_markup.row("Общий средний уровень образования")
            user_markup.row("◀️ Назад")
            db.reference("/bot/users/"+str(user_id)).update({"current": "block_2/5"})
            bot.send_message(message.from_user.id,"Выберите:",reply_markup = user_markup)

        else:
                bot.send_message(message.from_user.id,"Ошибка! Выберите из перечисленных.")



    elif current == "block_2/5/3/1":

        if message.text == "Русский язык":
            bot.send_message(message.chat.id, '[Русский язык](https://telegra.ph/Uchebnyj-predmet-Russkij-yazyk-s-russkim-yazykom-obucheniya-09-09)', parse_mode='Markdown')

        elif message.text == "Русская литература":
            bot.send_message(message.chat.id, '[Литературное чтение](https://telegra.ph/Uchebnyj-predmet-Russkaya-literatura-s-russkim-yazykom-obucheniya-09-09)', parse_mode='Markdown')

        elif message.text == "Қазақ тілі мен әдебиеті":
            bot.send_message(message.chat.id, '[Қазақ тілі мен әдебиеті](https://telegra.ph/%D2%9Aaza%D2%9B-t%D1%96l%D1%96-men-%D3%99debiet%D1%96-o%D2%9Bytu-p%D3%99n%D1%96-5-9-synyptar-09-09)', parse_mode='Markdown')

        elif message.text == "Иностранный язык":
            bot.send_message(message.chat.id, '[Иностранный язык](https://telegra.ph/Uchebnyj-predmet-Inostrannyj-yazyk-09-09-2)', parse_mode='Markdown')

        elif message.text == "Естествознание":
            bot.send_message(message.chat.id, '[Естествознание](https://telegra.ph/Uchebnyj-predmet-Estestvoznanie-09-09-2)', parse_mode='Markdown')

        elif message.text == "Физика":
            bot.send_message(message.chat.id, '[Физика](https://telegra.ph/Uchebnyj-predmet-Fizika-09-09)', parse_mode='Markdown')

        elif message.text == "География":
            bot.send_message(message.chat.id, '[География](https://telegra.ph/Uchebnyj-predmet-Geografiya-09-09)', parse_mode='Markdown')

        elif message.text == "Биология":
            bot.send_message(message.chat.id, '[Биология](https://telegra.ph/Uchebnyj-predmet-Biologiya-09-09)', parse_mode='Markdown')

        elif message.text == "Химия":
            bot.send_message(message.chat.id, '[Химия](https://telegra.ph/Uchebnyj-predmet-Himiya-09-09)', parse_mode='Markdown')

        elif message.text == "История Казахстана и Всемирная история":
            bot.send_message(message.chat.id, '[История Казахстана и Всемирная история](https://telegra.ph/Uchebnye-predmety-Istoriya-Kazahstana-i-Vsemirnaya-istoriya-09-09)', parse_mode='Markdown')

        elif message.text == "Основы права":
            bot.send_message(message.chat.id, '[Основы права](https://telegra.ph/Uchebnyj-predmet-Osnovy-prava-09-09-2)', parse_mode='Markdown')

        elif message.text == "Светскость и основы религиоведения":
            bot.send_message(message.chat.id, '[Светскость и основы религиоведения](https://telegra.ph/Fakultativnyj-kurs-Svetskost-i-osnovy-religiovedeniya-09-09)', parse_mode='Markdown')

        elif message.text == "Самопознание":
            bot.send_message(message.chat.id, '[Самопознание](https://telegra.ph/Uchebnyj-predmet-Samopoznanie-09-09-2)', parse_mode='Markdown')

        elif message.text == "Музыка":
            bot.send_message(message.chat.id, '[Музыка](https://telegra.ph/Uchebnyj-predmet-Muzyka-09-09-2)', parse_mode='Markdown')

        elif message.text == "Художественный труд":
            bot.send_message(message.chat.id, '[Художественный труд](https://telegra.ph/Uchebnyj-predmet-Hudozhestvennyj-trud-09-09-2)', parse_mode='Markdown')


        elif message.text == "◀️ Назад":

                user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
                user_markup.row("Образовательная область «Язык и Литература»")
                user_markup.row("Образовательная область «Математика и Информатика»")
                user_markup.row("Образовательная область «Естествознание»")
                user_markup.row("Образовательная область «Человек и общество»")
                user_markup.row("Образовательная область «Технология и искусство»")
                user_markup.row("Образовательная область «Физическая культутра»")
                user_markup.row("Инклюзивное образование")
                user_markup.row("Специальное образование")
                user_markup.row("◀️ Назад")
                db.reference("/bot/users/"+str(user_id)).update({"current": "block_2/5/3"})
                bot.send_message(message.from_user.id,"Выбери: ",reply_markup = user_markup)

        else:
                bot.send_message(message.from_user.id,"Ошибка! Выберите из перечисленных.")



    elif current == "block_2/5/4":


        if message.text == "Образовательная область «Язык и Литература»":
                user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
                user_markup.row("Русский язык")
                user_markup.row("Русская литература")
                user_markup.row("Қазақ тілі мен әдебиеті")
                user_markup.row("Иностранный язык")
                user_markup.row("◀️ Назад")
                db.reference("/bot/users/"+str(user_id)).update({"current": "block_2/5/4/1"})
                bot.send_message(message.from_user.id,"         В рамках образовательной области «Язык и литература» изучаются следующие предметы:\n"
                                                      "         «Қазақ тілі», «Русский язык», «Қазақ әдебиеті», «Русская литература», «Қазақ тілі мен әдебиеті», «Русский язык и литература», «Иностранный язык».",reply_markup = user_markup)

        elif message.text == "Образовательная область «Математика и Информатика»":
            bot.send_message(message.chat.id, '[Образовательная область «Математика и Информатика»](https://telegra.ph/OBRAZOVATELNAYA-OBLAST-MATEMATIKA-I-INFORMATIKA-09-09-2)', parse_mode='Markdown')

        elif message.text == "Образовательная область «Естествознание»":
                user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
                user_markup.row("Физика")
                user_markup.row("География")
                user_markup.row("Биология")
                user_markup.row("Химия")
                user_markup.row("◀️ Назад")
                db.reference("/bot/users/"+str(user_id)).update({"current": "block_2/5/4/1"})
                bot.send_message(message.from_user.id,"    В рамках образовательной области «Естествознание» по учебным программам обновленного содержания изучаются следующие предметы: «Физика», «География», «Биология», «Химия».",reply_markup = user_markup)


        elif message.text == "Образовательная область «Человек и общество»":
                user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
                user_markup.row("История Казахстана")
                user_markup.row("Всемирная история")
                user_markup.row("Основы права")
                user_markup.row("Самопознание")
                user_markup.row("Основы предпринимательства и бизнеса")
                user_markup.row("Графика и проектирование")


                user_markup.row("◀️ Назад")
                db.reference("/bot/users/"+str(user_id)).update({"current": "block_2/5/4/1"})
                bot.send_message(message.from_user.id,'[Образовательная область «Человек и общество»](https://telegra.ph/OBRAZOVATELNAYA-OBLAST-CHELOVEK-I-OBSHCHESTVO-09-09-2)',parse_mode='Markdown', reply_markup = user_markup)


        elif message.text == "Образовательная область «Физическая культутра»":
                user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
                user_markup.row("Физическая культура")
                user_markup.row("Начальная военная и технологическая подготовка")
                user_markup.row("◀️ Назад")
                db.reference("/bot/users/"+str(user_id)).update({"current": "block_2/5/4/1"})
                bot.send_message(message.from_user.id,"    В рамках образовательной области «Естествознание» по учебным программам обновленного содержания изучаются следующие предметы: «Физика», «География», «Биология», «Химия».",reply_markup = user_markup)

        elif message.text == "Инклюзивное образование":
            bot.send_message(message.chat.id, '[Инклюзивное образование](https://telegra.ph/Inklyuzivnoe-obrazovanie-09-09-2)', parse_mode='Markdown')
            bot.send_message(message.chat.id, '[Инклюзивное образование 2](https://telegra.ph/Inklyuzivnoe-obrazovanieCHast-2-09-09)', parse_mode='Markdown')

        elif message.text == "◀️ Назад":

            user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
            user_markup.row("Группы и классы предшкольной подготовки")
            user_markup.row("Начальный уровень образования")
            user_markup.row("Основной средний уровень образования")
            user_markup.row("Общий средний уровень образования")
            user_markup.row("◀️ Назад")
            db.reference("/bot/users/"+str(user_id)).update({"current": "block_2/5"})
            bot.send_message(message.from_user.id,"Выберите:",reply_markup = user_markup)

        else:
                bot.send_message(message.from_user.id,"Ошибка! Выберите из перечисленных.")


    elif current == "block_2/5/4/1":

        if message.text == "Русский язык":
            bot.send_message(message.chat.id, '[Русский язык](https://telegra.ph/Uchebnyj-predmet-Russkij-yazyk-s-russkim-yazykom-obucheniya-10-11-kl-09-09)', parse_mode='Markdown')

        elif message.text == "Русская литература":
            bot.send_message(message.chat.id, '[Русская литература](https://telegra.ph/Uchebnyj-predmet-Russkaya-literatura-s-russkim-yazykom-obucheniya-09-09-2)', parse_mode='Markdown')

        elif message.text == "Қазақ тілі мен әдебиеті":
            bot.send_message(message.chat.id, '[Қазақ тілі мен әдебиеті](https://telegra.ph/%D2%9Aaza%D2%9B-t%D1%96l%D1%96-men-%D3%99debiet%D1%96-10-11-synyptar-09-09)', parse_mode='Markdown')

        elif message.text == "Иностранный язык":
            bot.send_message(message.chat.id, '[Иностранный язык](https://telegra.ph/Uchebnyj-predmet-Inostrannyj-yazyk-09-09-3)', parse_mode='Markdown')

        elif message.text == "Физика":
            bot.send_message(message.chat.id, '[Физика](https://telegra.ph/Uchebnyj-predmet-Fizika-09-09-2)', parse_mode='Markdown')

        elif message.text == "География":
            bot.send_message(message.chat.id, '[География](https://telegra.ph/Uchebnyj-predmet-Geografiya-09-09-2)', parse_mode='Markdown')

        elif message.text == "Биология":
            bot.send_message(message.chat.id, '[Биология](https://telegra.ph/Uchebnyj-predmet-Biologiya-10-11-klassy-09-09)', parse_mode='Markdown')

        elif message.text == "Химия":
            bot.send_message(message.chat.id, '[Химия](https://telegra.ph/Uchebnyj-predmet-Himiya-09-09-2)', parse_mode='Markdown')

        elif message.text == "История Казахстана":
            bot.send_message(message.chat.id, '[История Казахстана](https://telegra.ph/Uchebnyj-predmet-Istoriya-Kazahstana-09-09)', parse_mode='Markdown')

        elif message.text == "Всемирная история":
            bot.send_message(message.chat.id, '[Всемирная история](https://telegra.ph/Uchebnyj-predmet-Vsemirnaya-istoriya-09-09)', parse_mode='Markdown')

        elif message.text == "Основы права":
            bot.send_message(message.chat.id, '[Основы права](https://telegra.ph/Uchebnyj-predmet-Osnovy-prava-09-09)', parse_mode='Markdown')

        elif message.text == "Самопознание":
            bot.send_message(message.chat.id, '[Самопознание](https://telegra.ph/Uchebnyj-predmet-Samopoznanie-09-09-3)', parse_mode='Markdown')

        elif message.text == "Основы предпринимательства и бизнеса":
            bot.send_message(message.chat.id, '[Основы предпринимательства и бизнеса](https://telegra.ph/Uchebnyj-predmet-Osnovy-predprinimatelstva-i-biznesa-09-09)', parse_mode='Markdown')

        elif message.text == "Графика и проектирование":
            bot.send_message(message.chat.id, '[Графика и проектирование](https://telegra.ph/Uchebnyj-predmet-Grafika-i-proektirovanie-09-09)', parse_mode='Markdown')

        elif message.text == "Физическая культура":
            bot.send_message(message.chat.id, '[Физическая культура](https://telegra.ph/Fizicheskaya-kultura-10-11-klassy-09-09)', parse_mode='Markdown')

        elif message.text == "Начальная военная и технологическая подготовка":
            bot.send_message(message.chat.id, '[Начальная военная и технологическая подготовка](https://telegra.ph/Nachalnaya-voennaya-i-tehnologicheskaya-podgotovka-09-09)', parse_mode='Markdown')


        elif message.text == "◀️ Назад":

                user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
                user_markup.row("Образовательная область «Язык и Литература»")
                user_markup.row("Образовательная область «Математика и Информатика»")
                user_markup.row("Образовательная область «Естествознание»")
                user_markup.row("Образовательная область «Человек и общество»")
                user_markup.row("Образовательная область «Технология и искусство»")
                user_markup.row("Образовательная область «Физическая культутра»")
                user_markup.row("Инклюзивное образование")
                user_markup.row("◀️ Назад")
                db.reference("/bot/users/"+str(user_id)).update({"current": "block_2/5/4"})
                bot.send_message(message.from_user.id,"Выбери: ",reply_markup = user_markup)

        else:
                bot.send_message(message.from_user.id,"Ошибка! Выберите из перечисленных.")




    elif current == "block_2/6":

        if message.text == "Критериальная система оценивания учебных достижений обучающихся":
            bot.send_message(message.chat.id, '[Критериальная система оценивания учебных достижений обучающихся](https://telegra.ph/Kriterialnaya-sistema-ocenivaniya-uchebnyh-dostizhenij-obuchayushchihsya-09-06)', parse_mode='Markdown')

        elif message.text == "Оценивание учебных достижений обучающихся в условиях ограничительных мер":
            bot.send_message(message.chat.id, '[Оценивание учебных достижений обучающихся в условиях ограничительных мер](https://telegra.ph/Ocenivanie-uchebnyh-dostizhenij-obuchayushchihsya-v-usloviyah-ogranichitelnyh-mer-09-06)', parse_mode='Markdown')

        elif message.text == "Инструменты критериального оценивания":
            bot.send_message(message.chat.id, '[Инструменты критериального оценивания](https://telegra.ph/Instrumenty-kriterialnogo-ocenivaniya-09-06)', parse_mode='Markdown')

        elif message.text == "ПАМЯТКА по выставлению формативных баллов":
            bot.send_message(message.chat.id, '[ПАМЯТКА по выставлению формативных баллов](https://telegra.ph/PAMYATKA-po-vystavleniyu-formativnyh-ballov-09-06)', parse_mode='Markdown')

        elif message.text == "Методические разработки по критериальному оцениванию":
            bot.send_message(message.chat.id, '[Методические разработки по критериальному оцениванию](https://telegra.ph/Metodicheskie-razrabotki-po-kriterialnomu-ocenivaniyu-09-06)', parse_mode='Markdown')

        elif message.text == "Система оценивания учащихся специальных школ":
            bot.send_message(message.chat.id, '[Система оценивания учащихся специальных школ](https://telegra.ph/Sistema-ocenivaniya-uchashchihsya-specialnyh-shkol-09-06)', parse_mode='Markdown')

        elif message.text == "Проведение итоговой аттестации":
            bot.send_message(message.chat.id, '[Проведение итоговой аттестации](https://telegra.ph/PROVEDENIE-ITOGOVOJ-ATTESTACII-09-06)', parse_mode='Markdown')



        elif message.text == "◀️ Назад":
            user_id = message.from_user.id
            user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
            user_markup.row("Нормативное правовое обеспечение")
            user_markup.row("Тенденции развития современного образования")
            user_markup.row("Педагог в системе образования")
            user_markup.row("Воспитательная работа")
            user_markup.row("Организация образовательного процесса в 2020-2021 учебном году")
            user_markup.row("Система оценивания учебных достижений")
            user_markup.row("Учебно-методическое обеспечение МКШ")
            user_markup.row("Цифровые образовательные ресурсы")
            user_markup.row("Апробация учебных программ в пилотных организациях образвания")
            user_markup.row("Приложения")
            user_markup.row("◀️ Назад")
            db.reference("/bot/users/"+str(user_id)).update({"lang": "Русский"})
            bot.send_message(user_id,"Содержание:",reply_markup = user_markup)

            db.reference("/bot/users/"+str(user_id)).update({"current": "block_2"})
        else:
                bot.send_message(message.from_user.id,"Ошибка! Выберите из перечисленных.")













#############################################################################################################################


    elif current == "block_3":
        if message.text == "Нормативтік-құқықтық қамтамасыз ету":
            user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
            user_markup.row("Білім беру процесін ұйымдастыруда қолданыста болатын НҚА")
            user_markup.row("1-4-сыныптарда білім беру процесі")
            user_markup.row("5-11-сыныптарда білім беру процесі")
            user_markup.row("«Педагог мәртебесі туралы» Заңның қабылдануына байланысты бекітілген орта білім беру жүйесіне қатысты НҚА")
            user_markup.row("2020-2021 оқу жылындағы каникул күндері")
            user_markup.row("Электронды журналды толтыру")
            user_markup.row("Мектепішілік бақылау")
            user_markup.row("◀️ Қайту")
            db.reference("/bot/users/"+str(user_id)).update({"current": "block_3/1"})
            bot.send_message(message.from_user.id,"Таңдаңыз:",reply_markup = user_markup)

        elif message.text == "Қазіргі білім берудің дамуындағы тенденциялары":
            user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
            user_markup.row("Білім мен ғылымды дамыту бойынша жүйелі кешенді шаралар")
            user_markup.row("БҒДМБ бойынша орта білім беру жүйесін дамытудың негізгі ұстанымдары")
            user_markup.row("Қашықтан білім беру технологияларын қолдану")
            user_markup.row("◀️ Қайту")
            db.reference("/bot/users/"+str(user_id)).update({"current": "block_3/2"})
            bot.send_message(message.from_user.id,"Таңдаңыз:",reply_markup = user_markup)

        elif message.text == "Білім беру жүйесіндегі педагог":
            user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
            user_markup.row("Педагог статусы")
            user_markup.row("Тұлғалық және кәсіби құзыреттілік")
            user_markup.row("Біліктілік санаттарына қойылатын талаптар")
            user_markup.row("◀️ Қайту")
            db.reference("/bot/users/"+str(user_id)).update({"current": "block_3/3"})
            bot.send_message(message.from_user.id,"Таңдаңыз:",reply_markup = user_markup)

        elif message.text == "Тәрбие жұмысы":
            user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
            user_markup.row("Тәрбие жұмыстарын ұйымдастырудың нормативті-құқықтық базасы")
            user_markup.row("2020-2021 оқу ж-ғы тәрбие жұмысының негізгі бағыттары")
            user_markup.row("Төтенше жағдай кезінде тәрбие жұмысын ұйымдастыру")
            user_markup.row("Тәрбие жұмысы бойынша ресурстар")
            user_markup.row("◀️ Қайту")
            db.reference("/bot/users/"+str(user_id)).update({"current": "block_3/4"})
            bot.send_message(message.from_user.id,"Таңдаңыз:",reply_markup = user_markup)

        elif message.text == "2020-2021 оқу жылында білім беру процесін ұйымдастыру":
            user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
            user_markup.row("Мектепалды даярлық топтары сыныптары")
            user_markup.row("Бастауыш білім беру деңгейі")
            user_markup.row("Негізгі орта білім беру деңгейі")
            user_markup.row("Жалпы орта білім беру деңгейі")
            user_markup.row("◀️ Қайту")
            db.reference("/bot/users/"+str(user_id)).update({"current": "block_3/5"})
            bot.send_message(message.from_user.id,"Таңдаңыз:",reply_markup = user_markup)



        elif message.text == "Бағалау жүйесі":
            user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
            user_markup.row("Білім алушылардың жетістіктерін бағалаудың критериалды жүйесі")
            user_markup.row("Шектеу шаралары кезінде білім алушылардың оқудағы жетістіктерін бағалау")
            user_markup.row("Критериалды бағалау құралдары")
            user_markup.row("Қалыптастырушы бағалауға балл қою бойынша ЖАДЫНАМА")
            user_markup.row("Критериалды бағалау бойынша Әдістемелік ұсынымдар")
            user_markup.row("Арнайы мектеп оқушыларын бағалау жүйесі")
            user_markup.row("Қорытынды аттестаттау өткізу")
            user_markup.row("◀️ Қайту")
            db.reference("/bot/users/"+str(user_id)).update({"current": "block_3/6"})
            bot.send_message(message.from_user.id,"Таңдаңыз:",reply_markup = user_markup)

        elif message.text == "Шағынжинақты мектепті оқу-әдістемелік қамтамасыз ету":
            bot.send_message(message.chat.id, '[Шағынжинақты мектепті оқу-әдістемелік қамтамасыз ету](https://telegra.ph/SHA%D2%92YNZHINA%D2%9ATY-MEKTEPT%D0%86-O%D2%9AU-%D3%98D%D0%86STEMEL%D0%86K-%D2%9AAMTAMASYZ-ETU-09-07)', parse_mode='Markdown')

        elif message.text == "Ресурстар":
            bot.send_message(message.chat.id, '[Ресурстар](https://telegra.ph/SANDY%D2%9A-B%D0%86L%D0%86M-BERU-RESURSTARY-09-07)', parse_mode='Markdown')


        elif message.text == "Пилоттық білім беру ұйымдарында бағдарламаларын сынақтан өткізу":
            bot.send_message(message.chat.id, '[Пилоттық білім беру ұйымдарында бағдарламаларын сынақтан өткізу](https://telegra.ph/PILOTTY%D2%9A-B%D0%86L%D0%86M-BERU-%D2%B0JYMDARYNDA-O%D2%9AU-BA%D2%92DARLAMALARYN-SYNA%D2%9ATAN-%D3%A8TK%D0%86ZU-09-07)', parse_mode='Markdown')


        elif message.text == "Қосымша":
                markup = types.InlineKeyboardMarkup()
                btn_docs= types.InlineKeyboardButton(text='Өтініш', url='https://docs.google.com/document/d/1rdI7RmtUXkr4yzrI2uFnff4TYuI8y3m846ZUKggQKjA/edit?usp=sharing')
                btn_docs2= types.InlineKeyboardButton(text='Педагогтерге арналған әдебиеттер тізімі', url='https://docs.google.com/document/d/1Duq9eullfoMXC2w19w4MlfI4W_aSlw_ktiSmgBe8Ieo/edit?usp=sharing')
                btn_docs3= types.InlineKeyboardButton(text='Білім алушыларға арналған әдебиеттер тізімі', url='https://docs.google.com/document/d/1nJs1NMC_C7TwYye7_xp-JHPgvzDVoVbtjsOVa5kUNtM/edit?usp=sharing')
                btn_docs4= types.InlineKeyboardButton(text='Сабақты бақылау парағы', url='https://docs.google.com/document/d/1GDgS2Hr0kZimWKCRGch4BgXd0Gx6hnKOUYW0ocCV-WA/edit?usp=sharing')
                markup.add(btn_docs)
                markup.add(btn_docs2)
                markup.add(btn_docs3)
                markup.add(btn_docs4)
                bot.send_message(message.chat.id, "Қосымша:", reply_markup = markup)

        elif message.text == "◀️ Қайту":
            user_id = message.from_user.id
            user_markup = telebot.types.ReplyKeyboardMarkup(True)
            user_markup.row("Русский", "Қазақша")
            bot.send_message(user_id,"Выберите язык:",reply_markup = user_markup)

            db.reference("/bot/users/"+str(user_id)).update({"current": "content"})
        else:
            bot.send_message(message.from_user.id,"Қате! Төмендегілердің бірін таңдаңыз.")

    elif current == "block_3/1":
        if message.text == "Білім беру процесін ұйымдастыруда қолданыста болатын НҚА":
            user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
            user_markup.row("Мектепалды дайындық")
            user_markup.row("1-4 сыныптар")
            user_markup.row("5-9 сыныптар")
            user_markup.row("10-11 сыныптар")
            user_markup.row("◀️ Қайту")
            db.reference("/bot/users/"+str(user_id)).update({"current": "block_3/1/2"})
            bot.send_message(message.from_user.id,"Білім беру деңгейлері:",reply_markup = user_markup)

        elif message.text == "1-4-сыныптарда білім беру процесі":
            bot.send_message(message.chat.id, '[1-4-сыныптарда білім беру процесі](https://telegra.ph/1-4-synyptarda-b%D1%96l%D1%96m-beru-proces%D1%96-keles%D1%96-%D2%9B%D2%B1zhattar-neg%D1%96z%D1%96nde-zh%D2%AFzege-asyrylady-09-07)', parse_mode='Markdown')


        elif message.text == "5-11-сыныптарда білім беру процесі":
            bot.send_message(message.chat.id, '[5-11-сыныптарда білім беру процесі](https://telegra.ph/5-11-synyptarda-b%D1%96l%D1%96m-beru-proces%D1%96-keles%D1%96-%D2%9B%D2%B1zhattar-neg%D1%96z%D1%96nde-zh%D2%AFzege-asyrylady-09-07)', parse_mode='Markdown')

        elif message.text == "«Педагог мәртебесі туралы» Заңның қабылдануына байланысты бекітілген орта білім беру жүйесіне қатысты НҚА":
            bot.send_message(message.chat.id, '[«Педагог мәртебесі туралы» Заңның қабылдануына байланысты бекітілген орта білім беру жүйесіне қатысты НҚА](https://telegra.ph/Pedagog-m%D3%99rtebes%D1%96-turaly-Za%D2%A3ny%D2%A3-%D2%9Babyldanuyna-bajlanysty-bek%D1%96t%D1%96lgen-orta-b%D1%96l%D1%96m-beru-zh%D2%AFjes%D1%96ne-%D2%9Batysty-N%D2%9AA-zh%D3%99ne-zha%D2%A3adan-%D2%9Babyldan-09-07)', parse_mode='Markdown')

        elif message.text == "2020-2021 оқу жылындағы каникул күндері":
            user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
            user_markup.row("Жалпы орта білім беретін мектептердің 1-11-сыныптарында")
            user_markup.row("Мектепалды даярлық сыныптарында")
            user_markup.row("◀️ Қайту")
            db.reference("/bot/users/"+str(user_id)).update({"current": "block_3/1/2"})
            bot.send_message(message.from_user.id,"««Орта білім беру ұйымдарында 2020 - 2021 оқу жылының басталуын, ұзақтығын және каникул кезеңдерін айқындау туралы»  Қазақстан Республикасы Білім және ғылым министрінің 2020 жылғы 12 тамыздағы №340 бұйрығы",reply_markup = user_markup)

        elif message.text == "Электронды журналды толтыру":
            user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
            user_markup.row("Электронды журнал")
            user_markup.row("Жиынтық бағалау журналы")
            user_markup.row("Электронды журналды толтыруда жиі кездесетін сұрақтар")

            user_markup.row("◀️ Қайту")
            db.reference("/bot/users/"+str(user_id)).update({"current": "block_3/1/2"})
            bot.send_message(message.from_user.id,"Таңдаңыз:",reply_markup = user_markup)

        elif message.text == "Мектепішілік бақылау":
            user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
            user_markup.row("Оқу жылына мектепішілік бақылау жоспары")
            user_markup.row("Мектепішілік бақылау нормативтері")
            user_markup.row("◀️ Қайту")
            db.reference("/bot/users/"+str(user_id)).update({"current": "block_3/1/2"})
            bot.send_message(message.from_user.id,"Таңдаңыз:",reply_markup = user_markup)


        elif message.text == "◀️ Қайту":
            user_id = message.from_user.id
            user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
            user_markup.row("Нормативтік-құқықтық қамтамасыз ету")
            user_markup.row("Қазіргі білім берудің дамуындағы тенденциялары")
            user_markup.row("Білім беру жүйесіндегі педагог")
            user_markup.row("Тәрбие жұмысы")
            user_markup.row("2020-2021 оқу жылында білім беру процесін ұйымдастыру")
            user_markup.row("Бағалау жүйесі")
            user_markup.row("Шағынжинақты мектепті оқу-әдістемелік қамтамасыз ету")
            user_markup.row("Ресурстар")
            user_markup.row("Пилоттық білім беру ұйымдарында бағдарламаларын сынақтан өткізу")
            user_markup.row("Қосымша")
            user_markup.row("◀️ Қайту")
            db.reference("/bot/users/"+str(user_id)).update({"lang": "Қазақша"})
            bot.send_message(user_id,"Мазмұны",reply_markup = user_markup)

            db.reference("/bot/users/"+str(user_id)).update({"current": "block_3"})

        else:
            bot.send_message(message.from_user.id,"Қате! Төмендегілердің бірін таңдаңыз.")

    elif current == "block_3/1/2":
        if message.text == "Мектепалды дайындық":
            user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
            user_markup.row("Типтік оқу жоспарлары (М.Д)")
            user_markup.row("Типтік оқу бағдарламалары (М.Д)")
            user_markup.row("◀️ Қайту")
            db.reference("/bot/users/"+str(user_id)).update({"current": "block_3/1/2/1"})
            bot.send_message(message.from_user.id,"Таңдаңыз:",reply_markup = user_markup)


        elif message.text == "1-4 сыныптар":
            user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
            user_markup.row("Типтік оқу жоспарлары (1-4)")
            user_markup.row("Типтік оқу бағдарламалары (1-4)")
            user_markup.row("◀️ Қайту")
            db.reference("/bot/users/"+str(user_id)).update({"current": "block_3/1/2/1"})
            bot.send_message(message.from_user.id,"Таңдаңыз:",reply_markup = user_markup)

        elif message.text == "5-9 сыныптар":
            user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
            user_markup.row("Типтік оқу жоспарлары (5-9)")
            user_markup.row("Типтік оқу бағдарламалары (5-9)")
            user_markup.row("◀️ Қайту")
            db.reference("/bot/users/"+str(user_id)).update({"current": "block_3/1/2/1"})
            bot.send_message(message.from_user.id,"Таңдаңыз:",reply_markup = user_markup)

        elif message.text == "10-11 сыныптар":
            user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
            user_markup.row("Типтік оқу жоспарлары (10-11)")
            user_markup.row("Типтік оқу бағдарламалары (10-11)")
            user_markup.row("◀️ Қайту")
            db.reference("/bot/users/"+str(user_id)).update({"current": "block_3/1/2/1"})
            bot.send_message(message.from_user.id,"Таңдаңыз:",reply_markup = user_markup)


###########################



        elif message.text == "Жалпы орта білім беретін мектептердің 1-11-сыныптарында":
            bot.send_message(message.chat.id, "1) 2020 - 2021 оқу жылының басталуы - 2020 жылғы 1 қыркүйек; \n 2) оқу жылының ұзақтығы 1-сыныптарда – 33 оқу аптасы, 2-11 (12)- сыныптарда – 34 оқу аптасы. Мейрам күндеріне түскен сабақтар оқу бағдарламасы мазмұнының кіріктірілуі ескеріле отырып, қайталауға арналған сағаттар есебінен келесі жұмыс күндеріне ауыстырылады. \n 3) оқу жылы ішіндегі каникул кезеңдері: \n 1-11 (12) – сыныптарда: күзгі каникул – 10 күн (2020 жылғы 5-14 қараша аралығында) қысқы – 11 күн (2020 жылғы 31 желтоқсан мен 2021 жылғы 10 қаңтар аралығында), көктемгі – 12 күн (2021 жылғы 20-31 наурыз аралығында); 1-сыныптарда: қосымша каникул – 7 күн (2021 жылғы 8-14 ақпан аралығында).")

        elif message.text == "Мектепалды даярлық сыныптарында":
            bot.send_message(message.chat.id, "Мектепалды сыныптарда оқу жылының ұзақтығы 32 аптаны құрайды. " \
                                                    "Мектепалды сыныптарда: \n" +
                                                    "күзгі каникул – 10 күн (2020 жылғы 5-14 қараша аралығында), " \
                                                    "қысқы – 11 күн (2020 жылғы 31 желтоқсан мен 2021 жылғы 10 қаңтар аралығында), " \
                                                    "көктемгі – 12 күн (2021 жылғы 20 наурыз – 31 наурыз қоса алғанда); " \
                                                    "қосымша каникулдар: 7 күн (2021жылғы 8 - 14 ақпанды қоса алғанда).")

############################


        elif message.text == "Электронды журнал":
            bot.send_message(message.chat.id, '[Электронды журнал](https://telegra.ph/EHlektrondy-zhurnal-09-07)', parse_mode='Markdown')

        elif message.text == "Жиынтық бағалау журналы":
            bot.send_message(message.chat.id, "1. кері байланыс үшін түсініктемелерді пайдалана отырып, қалыптастырушы бағалау балы (1-ден 10 балға дейін); \n " \
                                                "2. бөлім бойынша жиынтық жұмыс үшін балл (БЖБ) - жинаған баллдардың сомасы және оқу жетістіктерінің тиісті деңгейі; \n" \
                                                "3. оқу кезеңіндегі жиынтық жұмыс үшін балл (ТЖБ) – спецификацияға сәйкес жиналған балдардың сомасы; \n " \
                                                "4. жылдық баға-шкалаға сәйкес барлық оқу кезеңдерінде жинаған баллдардың максималды мүмкін болатын балға пайыздық қатынасы қойылады. \n ")

        elif message.text == "Электронды журналды толтыруда жиі кездесетін сұрақтар":
            bot.send_message(message.chat.id, '[Электронды журналды толтыруда жиі кездесетін сұрақтар](https://telegra.ph/EHlektrondy-zhurnaldy-toltyruda-zhi%D1%96-kezdeset%D1%96n-s%D2%B1ra%D2%9Btar-09-07)', parse_mode='Markdown')

##############################

        elif message.text == "Оқу жылына мектепішілік бақылау жоспары":
            bot.send_message(message.chat.id, "Оқу жылына мектепішілік бақылау жоспары Қазақстан Республикасы Білім және ғылым министрінің «Орта, техникалық және кәсіптік, орта білімнен кейінгі білім беру ұйымдарының педагогтері жүргізу үшін міндетті құжаттардың тізбесін және олардың нысандарын бекіту туралы» 2020 жылғы 6 сәуірдегі № 130 бұйрығына 17-қосымшаға сәйкес жасалады. \n " \
                                                    "Мектепішілік бақылау МЖМБС, Үлгілік оқу жоспарларының, Үлгілік оқу бағдарламаларының, орта мерзімді, қысқа мерзімді жоспарлардың, оқушылардың жеке істерінің және т.б. орындаған жұмыстарын тексеруді қамтиды. \n" \
                                                    "Білім берудің жаңартылған мазмұнын енгізуді ескере отырып, оқу процесін тиімді ұйымдастыру және мектепішілік бақылауды жүзеге асыру үшін жалпы білім беретін мектептердің әкімшілігі үшін мынадай нормативтер ұсынылады (3-кесте). \n" \
                                                    "Карантиндік және шектеу шаралары кезеңінде оқыту жағдайында мектепішілік бақылау әрбір білім беру ұйымының жағдайына қарай жүргізіледі. Мектепішілік бақылаудың барлық түрлері жүзеге асырылмауы мүмкін.")

        elif message.text == "Мектепішілік бақылау нормативтері":
            bot.send_message(message.chat.id, '[Мектепішілік бақылау нормативтері](https://telegra.ph/ZHalpy-b%D1%96l%D1%96m-beret%D1%96n-mektepterd%D1%96%D2%A3-%D3%99k%D1%96msh%D1%96l%D1%96g%D1%96ne-arnal%D2%93an-mektep%D1%96sh%D1%96l%D1%96k-ba%D2%9Bylau-normativter%D1%96-09-07)', parse_mode='Markdown')



        elif message.text == "◀️ Қайту":
            user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
            user_markup.row("Білім беру процесін ұйымдастыруда қолданыста болатын НҚА")
            user_markup.row("1-4-сыныптарда білім беру процесі")
            user_markup.row("5-11-сыныптарда білім беру процесі")
            user_markup.row("«Педагог мәртебесі туралы» Заңның қабылдануына байланысты бекітілген орта білім беру жүйесіне қатысты НҚА")
            user_markup.row("2020-2021 оқу жылындағы каникул күндері")
            user_markup.row("Электронды журналды толтыру")
            user_markup.row("Мектепішілік бақылау")
            user_markup.row("◀️ Қайту")
            db.reference("/bot/users/"+str(user_id)).update({"current": "block_3/1"})
            bot.send_message(message.from_user.id,"Таңдаңыз:",reply_markup = user_markup)


        else:
            bot.send_message(message.from_user.id,"Қате! Төмендегілердің бірін таңдаңыз.")



    elif current == "block_3/1/2/1":
        if message.text == "Типтік оқу жоспарлары (М.Д)":
                markup = types.InlineKeyboardMarkup()
                btn_docs= types.InlineKeyboardButton(text='12.12.2012   №557', url='http://adilet.zan.kz/rus/docs/V1200008275')
                markup.add(btn_docs)
                bot.send_message(message.chat.id, "Типтік оқу жоспарлары (М.Д):", reply_markup = markup)

        elif message.text == "Типтік оқу бағдарламалары (М.Д)":
                markup = types.InlineKeyboardMarkup()
                btn_docs= types.InlineKeyboardButton(text='12.08.2016    №499', url='http://adilet.zan.kz/rus/archive/docs/V1600014235/12.08.2016')
                markup.add(btn_docs)
                bot.send_message(message.chat.id, "Типтік оқу бағдарламалары (М.Д):", reply_markup = markup)

        elif message.text == "Типтік оқу жоспарлары (1-4)":
                markup = types.InlineKeyboardMarkup()
                btn_docs= types.InlineKeyboardButton(text='8.11.2012    №500', url='http://adilet.zan.kz/rus/docs/V1200008170')
                btn_docs2= types.InlineKeyboardButton(text='(4.09.2018    №441)', url='http://adilet.zan.kz/rus/docs/V1200008170')
                markup.add(btn_docs)
                markup.add(btn_docs2)
                bot.send_message(message.chat.id, "Типтік оқу жоспарлары (1-4):", reply_markup = markup)

        elif message.text == "Типтік оқу бағдарламалары (1-4)":
                markup = types.InlineKeyboardMarkup()
                btn_docs= types.InlineKeyboardButton(text='3.04.2013    №115', url='http://adilet.zan.kz/rus/docs/V1300008424')
                btn_docs2= types.InlineKeyboardButton(text='8.04.2016    №226', url='http://adilet.zan.kz/rus/docs/V1300008424')
                btn_docs3= types.InlineKeyboardButton(text='10.05.2018    №199', url='http://adilet.zan.kz/rus/docs/V1300008424')
                btn_docs4= types.InlineKeyboardButton(text='17.10.2018    №576', url='http://adilet.zan.kz/rus/docs/V1300008424')
                markup.add(btn_docs)
                markup.add(btn_docs2)
                markup.add(btn_docs3)
                markup.add(btn_docs4)
                bot.send_message(message.chat.id, "Типтік оқу бағдарламалары (1-4):", reply_markup = markup)

        elif message.text == "Типтік оқу жоспарлары (5-9)":
                markup = types.InlineKeyboardMarkup()
                btn_docs= types.InlineKeyboardButton(text='8.11.2012   №500', url='http://adilet.zan.kz/rus/docs/V1200008170')
                btn_docs2= types.InlineKeyboardButton(text='(4.09.2018   №441)', url='http://adilet.zan.kz/rus/docs/V1200008170')
                markup.add(btn_docs)
                markup.add(btn_docs2)
                bot.send_message(message.chat.id, "Типтік оқу жоспарлары (5-9):", reply_markup = markup)

        elif message.text == "Типтік оқу бағдарламалары (5-9)":
                markup = types.InlineKeyboardMarkup()
                btn_docs= types.InlineKeyboardButton(text='3.04.2013    №115', url='http://adilet.zan.kz/rus/docs/V1300008424')
                btn_docs2= types.InlineKeyboardButton(text='(25.10.2017   №545)', url='http://adilet.zan.kz/rus/docs/V1300008424')
                markup.add(btn_docs)
                markup.add(btn_docs2)
                bot.send_message(message.chat.id, "Типтік оқу бағдарламалары (5-9):", reply_markup = markup)

        elif message.text == "Типтік оқу жоспарлары (10-11)":
                markup = types.InlineKeyboardMarkup()
                btn_docs= types.InlineKeyboardButton(text='8.11.2012   №500', url='http://adilet.zan.kz/rus/docs/V1200008170')
                btn_docs2= types.InlineKeyboardButton(text='4.09.2018    №441', url='http://adilet.zan.kz/rus/docs/V1200008170')
                btn_docs3= types.InlineKeyboardButton(text='15.05.2019  №205', url='http://adilet.zan.kz/rus/docs/V1900018705')
                markup.add(btn_docs)
                markup.add(btn_docs2)
                markup.add(btn_docs3)
                bot.send_message(message.chat.id, "Типтік оқу жоспарлары (10-11):", reply_markup = markup)

        elif message.text == "Типтік оқу бағдарламалары (10-11)":
                markup = types.InlineKeyboardMarkup()
                btn_docs= types.InlineKeyboardButton(text='8.11.2012   №500', url='http://adilet.zan.kz/rus/docs/V1200008170')
                btn_docs2= types.InlineKeyboardButton(text='4.09.2018    №441', url='http://adilet.zan.kz/rus/docs/V1200008170')
                btn_docs3= types.InlineKeyboardButton(text='15.05.2019   №205', url='http://adilet.zan.kz/rus/docs/V1900018705')
                markup.add(btn_docs)
                markup.add(btn_docs2)
                markup.add(btn_docs3)
                bot.send_message(message.chat.id, "Типтік оқу бағдарламалары (10-11):", reply_markup = markup)


        elif message.text == "◀️ Қайту":
            user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
            user_markup.row("Мектепалды дайындық")
            user_markup.row("1-4 сыныптар")
            user_markup.row("5-9 сыныптар")
            user_markup.row("10-11 сыныптар")
            user_markup.row("◀️ Қайту")
            db.reference("/bot/users/"+str(user_id)).update({"current": "block_3/1/2"})
            bot.send_message(message.from_user.id,"Білім беру деңгейлері:",reply_markup = user_markup)


        else:
                bot.send_message(message.from_user.id,"Қате! Төмендегілердің бірін таңдаңыз.")



    elif current == "block_3/2":

        if message.text == "Білім мен ғылымды дамыту бойынша жүйелі кешенді шаралар":
            bot.send_message(message.chat.id, '[Білім мен ғылымды дамыту бойынша жүйелі кешенді шаралар](https://telegra.ph/B%D1%96l%D1%96m-men-%D2%93ylymdy-damytu-bojynsha-zh%D2%AFjel%D1%96-keshend%D1%96-sharalar-09-07)', parse_mode='Markdown')


        elif message.text == "БҒДМБ бойынша орта білім беру жүйесін дамытудың негізгі ұстанымдары":
            bot.send_message(message.chat.id, "2020-2025 жылдарға арналған БҒДМБ бойынша орта білім беру жүйесін дамытудың негізгі ұстанымдары: \n" \
                                                    "	білім берудің жаңартылған мазмұнына көшуді аяқтау; \n" \
                                                    "	оқулықтарды әзірлеу, сараптау,  шығарудың жаңа жүйесін енгізу; \n" \
                                                    "	критериалды бағалау жүйесін жетілдіру; \n" \
                                                    "	12 жылдық білім беруге көшу; \n" \
                                                    "	қашықтан білім беру технологияларын қолдану арқылы оқыту процесін ұйымдастыру.")

        elif message.text == "Қашықтан білім беру технологияларын қолдану":
                user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
                user_markup.row("Қашықтан оқыту бойынша НҚА")
                user_markup.row("ҚББТ қолдану")
                user_markup.row("Карантин кезінде қашықтан оқыту")
                user_markup.row("Шектеу шараларының кезінде оқыту процесін ұйымдастырудың негізгі талаптары")
                user_markup.row("Шектеу шаралары кезеңінде әдістемелік ұсынымдардың  тараулары")
                user_markup.row("Әдістемелік ұсынымдарға сілтеме")
                user_markup.row("◀️ Қайту")
                db.reference("/bot/users/"+str(user_id)).update({"current": "block_3/2/1"})
                bot.send_message(message.from_user.id,"Таңдаңыз:",reply_markup = user_markup)


        elif message.text == "◀️ Қайту":
            user_id = message.from_user.id
            user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
            user_markup.row("Нормативтік-құқықтық қамтамасыз ету")
            user_markup.row("Қазіргі білім берудің дамуындағы тенденциялары")
            user_markup.row("Білім беру жүйесіндегі педагог")
            user_markup.row("Тәрбие жұмысы")
            user_markup.row("2020-2021 оқу жылында білім беру процесін ұйымдастыру")
            user_markup.row("Бағалау жүйесі")
            user_markup.row("Шағынжинақты мектепті оқу-әдістемелік қамтамасыз ету")
            user_markup.row("Ресурстар")
            user_markup.row("Пилоттық білім беру ұйымдарында бағдарламаларын сынақтан өткізу")
            user_markup.row("Қосымша")
            user_markup.row("◀️ Қайту")
            db.reference("/bot/users/"+str(user_id)).update({"lang": "Қазақша"})
            bot.send_message(user_id,"Мазмұны",reply_markup = user_markup)

            db.reference("/bot/users/"+str(user_id)).update({"current": "block_3"})
        else:
                bot.send_message(message.from_user.id,"Қате! Төмендегілердің бірін таңдаңыз.")

    elif current == "block_3/2/1":

        if message.text == "Қашықтан оқыту бойынша НҚА":
            bot.send_message(message.chat.id, "1) Қазақстан Республикасы Білім және ғылым министрінің Мемлекеттік жалпыға міндетті бастауыш білім беру деңгейінің стандарты, 2018 жылғы 31 қазандағы № 604 бұйрығымен бекітілген \n" \
                                                    "2)	«Білім туралы» Қазақстан Республикасы Заңы \n" \
                                                    "3)	«Қашықтан білім беру технологиялары бойынша оқу процесін ұйымдастыру қағидаларын бекіту туралы» Қазақстан Республикасы Білім және ғылым министрінің 2015 жылғы 20 наурыздағы №137 бұйрығы \n" \
                                                    "4) «Қашықтан білім беру технологиялары бойынша оқу процесін ұйымдастыру қағидаларын бекіту туралы» Қазақстан Республикасы Білім және ғылым министрінің 2015 жылғы 20 наурыздағы №137 бұйрығына на өзгерістер мен толықтырулар енгізу туралы ҚР БҒМ 2020 жылғы 28 тамыздағы №374 бұйрығы \n")
        elif message.text == "ҚББТ қолдану":
            bot.send_message(message.chat.id, "ҚБТ мыналарға: \n" \
                                                    "1) білім берудің барлық деңгейлерінде ерекше білім беру қажеттіліктері бар, оның ішінде мүгедек балалар, бала кезінен мүгедектер, I және II топтағы мүгедектер болып табылатын тұлғаларға; \n" \
                                                    "2) денсаулық мүмкіндіктері уақытша шектелген және білім беру ұйымдарына тұрақты баруға мүмкіндігі жоқ тұлғаларға; \n" \
                                                    "3) мекемеде тиісті техникалық жағдайлар болған кезде қылмыстық-атқару жүйесі мекемелерінде ұсталатын және бас бостандығынан айыруға байланысты емес жазаларға сотталғандарға жүргізіледі. \n" \
                                                    "2020-2021 оқу жылында тиісті мемлекеттік органдардың шектеу шаралары, оның ішінде карантин, әлеуметтік, табиғи және техногендік сипаттағы төтенше жағдайлар жағдайында қосымша білім беру, орта, техникалық және кәсіптік, орта білімнен кейінгі білім беру бағдарламалары бойынша білім алушылар қашықтан білім алуда.")


        elif message.text == "Карантин кезінде қашықтан оқыту":
            bot.send_message(message.chat.id, "2020-2021 оқу жылының бірінші тоқсанында қашықтықтан оқыту технологияларын қолдану арқылы оқуға көшу ҚР БҒМ 13.08.20ж №345 бұйрығымен бекітілген «Коронавирустық инфекцияның таралуына байланысты шектеу шаралары кезеңінде орта білім беру ұйымдарында оқу процесін іске асыру жөніндегі   әдістемелік ұсынымдар» негізінде жүргізіледі.")

        elif message.text == "Шектеу шараларының кезінде оқыту процесін ұйымдастырудың негізгі талаптары":
            bot.send_message(message.chat.id, '[Шектеу шараларының кезінде оқыту процесін ұйымдастырудың негізгі талаптары](https://telegra.ph/SHekteu-sharalaryny%D2%A3-kez%D1%96nde-o%D2%9Bytu-proces%D1%96n-%D2%B1jymdastyrudy%D2%A3-neg%D1%96zg%D1%96-talaptary-09-07)', parse_mode='Markdown')

        elif message.text == "Шектеу шаралары кезеңінде әдістемелік ұсынымдардың  тараулары":
            bot.send_message(message.chat.id, '[Шектеу шаралары кезеңінде әдістемелік ұсынымдардың  тараулары](https://telegra.ph/SHekteu-sharalary-keze%D2%A3%D1%96nde-orta-b%D1%96l%D1%96m-beru-%D2%B1jymdarynda-o%D2%9Bu-proces%D1%96n-%D2%B1jymdastyru-zh%D3%A9n%D1%96ndeg%D1%96-%D3%99d%D1%96stemel%D1%96k-%D2%B1synymdardy%D2%A3-taraulary-09-07)', parse_mode='Markdown')

        elif message.text == "Әдістемелік ұсынымдарға сілтеме":
                markup = types.InlineKeyboardMarkup()
                btn_docs= types.InlineKeyboardButton(text='www.nao.kz', url='https://www.nao.kz/?lang=kz')
                markup.add(btn_docs)
                bot.send_message(message.chat.id, "Әдістемелік ұсынымдарға сілтеме: ", reply_markup = markup)

        elif message.text == "◀️ Қайту":
            user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
            user_markup.row("Білім мен ғылымды дамыту бойынша жүйелі кешенді шаралар")
            user_markup.row("БҒДМБ бойынша орта білім беру жүйесін дамытудың негізгі ұстанымдары")
            user_markup.row("Қашықтан білім беру технологияларын қолдану")
            user_markup.row("◀️ Қайту")
            db.reference("/bot/users/"+str(user_id)).update({"current": "block_3/2"})
            bot.send_message(message.from_user.id,"Таңдаңыз:",reply_markup = user_markup)

        else:
            bot.send_message(message.from_user.id,"Қате! Төмендегілердің бірін таңдаңыз.")


    elif current == "block_3/3":

        if message.text == "Педагог статусы":
            bot.send_message(message.chat.id, '[Педагог статусы](https://telegra.ph/Pedagog-statusy-09-07)', parse_mode='Markdown')

        elif message.text == "Тұлғалық және кәсіби құзыреттілік":
            bot.send_message(message.chat.id, '[Тұлғалық және кәсіби құзыреттілік](https://telegra.ph/T%D2%B1l%D2%93aly%D2%9B-zh%D3%99ne-k%D3%99s%D1%96bi-%D2%9B%D2%B1zyrett%D1%96l%D1%96k-09-07)', parse_mode='Markdown')


        elif message.text == "Біліктілік санаттарына қойылатын талаптар":
            bot.send_message(message.chat.id, "Педагогтерді аттестаттаудан өткізу ҚР Білім және ғылым министрінің 2016 жылғы 27 қаңтардағы №83 бұйрығына сәйкес жүзеге асырылады (14.05.2020 ж. №202 өзгерістермен және толықтырулармен). \n " \
                                                    "Мектепке дейінгі тәрбие мен оқытудың, бастауыш, негізгі орта және жалпы орта білім беретін оқу бағдарламаларын, техникалық және кәсіптік, орта білімнен кейінгі, қосымша, мамандандырылған және арнайы білім беру бағдарламаларын іске асыратын білім беру ұйымдарында лауазымдарды атқаратын педагогтерді және білім және ғылым саласындағы өзге де азаматтық қызметшілерді аттестаттаудан өткізу Қағидалары мен шарттары Қазақстан Республикасы Білім және ғылым министрлігінің 2020 жылғы 14 сәуірдегі №202 бұйрығының қосымшасына сәйкес жаңа редакцияда жазылған.")

        elif message.text == "◀️ Қайту":
            user_id = message.from_user.id
            user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
            user_markup.row("Нормативтік-құқықтық қамтамасыз ету")
            user_markup.row("Қазіргі білім берудің дамуындағы тенденциялары")
            user_markup.row("Білім беру жүйесіндегі педагог")
            user_markup.row("Тәрбие жұмысы")
            user_markup.row("2020-2021 оқу жылында білім беру процесін ұйымдастыру")
            user_markup.row("Бағалау жүйесі")
            user_markup.row("Шағынжинақты мектепті оқу-әдістемелік қамтамасыз ету")
            user_markup.row("Ресурстар")
            user_markup.row("Пилоттық білім беру ұйымдарында бағдарламаларын сынақтан өткізу")
            user_markup.row("Қосымша")
            user_markup.row("◀️ Қайту")
            db.reference("/bot/users/"+str(user_id)).update({"lang": "Қазақша"})
            bot.send_message(user_id,"Мазмұны",reply_markup = user_markup)

            db.reference("/bot/users/"+str(user_id)).update({"current": "block_3"})
        else:
                bot.send_message(message.from_user.id,"Қате! Төмендегілердің бірін таңдаңыз.")


    elif current == "block_3/4":

        if message.text == "Тәрбие жұмыстарын ұйымдастырудың нормативті-құқықтық базасы":
            bot.send_message(message.chat.id, '[Тәрбие жұмыстарын ұйымдастырудың нормативті-құқықтық базасы](https://telegra.ph/T%D3%99rbie-zh%D2%B1mystaryn-%D2%B1jymdastyrudy%D2%A3-normativt%D1%96-%D2%9B%D2%B1%D2%9By%D2%9Bty%D2%9B-bazasy-09-07)', parse_mode='Markdown')

        elif message.text == "2020-2021 оқу ж-ғы тәрбие жұмысының негізгі бағыттары":
                user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
                user_markup.row("Жаңа қазақстандық патриотизм мен азаматтыққа тәрбиелеу, құқықтық тәрбие")
                user_markup.row("Рухани-танымдық тәрбие")
                user_markup.row("Ұлттық тәрбие")
                user_markup.row("Отбасылық тәрбие")
                user_markup.row("Еңбек, экономикалық және экологиялық тәрбие")
                user_markup.row("Көпмәдениетті және көркем-эстетикалық тәрбие")
                user_markup.row("Зияткерлік тәрбие, ақпараттық мәдениетті тәрбиелеу")
                user_markup.row("Дене тәрбиесі, салауатты өмір салтын қалыптастыру")
                user_markup.row("◀️ Қайту")
                db.reference("/bot/users/"+str(user_id)).update({"current": "block_3/4/1"})
                bot.send_message(message.from_user.id,"Таңдаңыз:",reply_markup = user_markup)


        elif message.text == "Төтенше жағдай кезінде тәрбие жұмысын ұйымдастыру":
            bot.send_message(message.chat.id, '[Төтенше жағдай кезінде тәрбие жұмысын ұйымдастыру](https://telegra.ph/T%D3%A9tenshe-zha%D2%93daj-kez%D1%96nde-t%D3%99rbie-zh%D2%B1mysyn-%D2%B1jymdastyru-09-07)', parse_mode='Markdown')


        elif message.text == "Тәрбие жұмысы бойынша ресурстар":
            bot.send_message(message.chat.id, "Ы. Алтынсарин атындағы ҰБА ғылыми қызметкерлері әзірлеген барлық әдістемелік материалдарды Академия сайтынан https://www.nao.kz «Білім беруді ғылыми-әдістемелік қамтамасыз ету. Әдістемелік құралдар» бөлімінен табуға болады.")



        elif message.text == "◀️ Қайту":
            user_id = message.from_user.id
            user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
            user_markup.row("Нормативтік-құқықтық қамтамасыз ету")
            user_markup.row("Қазіргі білім берудің дамуындағы тенденциялары")
            user_markup.row("Білім беру жүйесіндегі педагог")
            user_markup.row("Тәрбие жұмысы")
            user_markup.row("2020-2021 оқу жылында білім беру процесін ұйымдастыру")
            user_markup.row("Бағалау жүйесі")
            user_markup.row("Шағынжинақты мектепті оқу-әдістемелік қамтамасыз ету")
            user_markup.row("Ресурстар")
            user_markup.row("Пилоттық білім беру ұйымдарында бағдарламаларын сынақтан өткізу")
            user_markup.row("Қосымша")
            user_markup.row("◀️ Қайту")
            db.reference("/bot/users/"+str(user_id)).update({"lang": "Қазақша"})
            bot.send_message(user_id,"Мазмұны",reply_markup = user_markup)
            db.reference("/bot/users/"+str(user_id)).update({"current": "block_3"})
        else:
                bot.send_message(message.from_user.id,"Қате! Төмендегілердің бірін таңдаңыз.")

    elif current == "block_3/4/1":

        if message.text == "Жаңа қазақстандық патриотизм мен азаматтыққа тәрбиелеу, құқықтық тәрбие":
                user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
                user_markup.row("Патриоттық тәрбие")
                user_markup.row("Білім алушылар арасында өлкетанулық білімді насихаттау мен тарату")
                user_markup.row("Әскери-патриоттық клубтарының, балалар мен жасөспірімдер қозғалысының қызметі")
                user_markup.row("Құқықтық тәрбие")
                user_markup.row("Инклюзивті мәдениет")
                user_markup.row("◀️ Қайту")
                db.reference("/bot/users/"+str(user_id)).update({"current": "block_3/4/1/1"})
                bot.send_message(message.from_user.id,"Выберите:",reply_markup = user_markup)


        elif message.text == "Рухани-танымдық тәрбие":
            bot.send_message(message.chat.id, '[Рухани-танымдық тәрбие](https://telegra.ph/Ruhani-tanymdy%D2%9B-t%D3%99rbie-09-07)', parse_mode='Markdown')


        elif message.text == "Ұлттық тәрбие":
            bot.send_message(message.chat.id, '[Ұлттық тәрбие](https://telegra.ph/%D2%B0ltty%D2%9B-t%D3%99rbie-09-07)', parse_mode='Markdown')

        elif message.text == "Отбасылық тәрбие":
            bot.send_message(message.chat.id, '[Отбасылық тәрбие](https://telegra.ph/Otbasyly%D2%9B-t%D3%99rbie-09-07)', parse_mode='Markdown')

        elif message.text == "Еңбек, экономикалық және экологиялық тәрбие":
            bot.send_message(message.chat.id, '[Еңбек, экономикалық және экологиялық тәрбие](https://telegra.ph/E%D2%A3bek-ehkonomikaly%D2%9B-zh%D3%99ne-ehkologiyaly%D2%9B-t%D3%99rbie-09-07)', parse_mode='Markdown')

        elif message.text == "Көпмәдениетті және көркем-эстетикалық тәрбие":
            bot.send_message(message.chat.id, '[Көпмәдениетті және көркем-эстетикалық тәрбие](https://telegra.ph/K%D3%A9pm%D3%99deniett%D1%96-zh%D3%99ne-k%D3%A9rkem-ehstetikaly%D2%9B-t%D3%99rbie-09-07)', parse_mode='Markdown')

        elif message.text == "Зияткерлік тәрбие, ақпараттық мәдениетті тәрбиелеу":
            bot.send_message(message.chat.id, '[Зияткерлік тәрбие, ақпараттық мәдениетті тәрбиелеу](https://telegra.ph/Ziyatkerl%D1%96k-t%D3%99rbie-a%D2%9Bparatty%D2%9B-m%D3%99deniett%D1%96-t%D3%99rbieleu-09-07)', parse_mode='Markdown')

        elif message.text == "Дене тәрбиесі, салауатты өмір салтын қалыптастыру":
            bot.send_message(message.chat.id, '[Дене тәрбиесі, салауатты өмір салтын қалыптастыру](https://telegra.ph/Dene-t%D3%99rbies%D1%96-salauatty-%D3%A9m%D1%96r-saltyn-%D2%9Balyptastyru-09-07)', parse_mode='Markdown')



        elif message.text == "◀️ Қайту":
            user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
            user_markup.row("Тәрбие жұмыстарын ұйымдастырудың нормативті-құқықтық базасы")
            user_markup.row("2020-2021 оқу ж-ғы тәрбие жұмысының негізгі бағыттары")
            user_markup.row("Төтенше жағдай кезінде тәрбие жұмысын ұйымдастыру")
            user_markup.row("Тәрбие жұмысы бойынша ресурстар")
            user_markup.row("◀️ Қайту")
            db.reference("/bot/users/"+str(user_id)).update({"current": "block_3/4"})
            bot.send_message(message.from_user.id,"Таңдаңыз:",reply_markup = user_markup)
        else:
                bot.send_message(message.from_user.id,"Қате! Төмендегілердің бірін таңдаңыз.")


    elif current == "block_3/4/1/1":


        if message.text == "Патриоттық тәрбие":
            bot.send_message(message.chat.id, '[Патриоттық тәрбие](https://telegra.ph/Patriotty%D2%9B-t%D3%99rbie-09-07)', parse_mode='Markdown')

        elif message.text == "Білім алушылар арасында өлкетанулық білімді насихаттау мен тарату":
            bot.send_message(message.chat.id, '[Білім алушылар арасында өлкетанулық білімді насихаттау мен тарату](https://telegra.ph/B%D1%96l%D1%96m-alushylar-arasynda-%D3%A9lketanuly%D2%9B-b%D1%96l%D1%96md%D1%96-nasihattau-men-taratu-09-07)', parse_mode='Markdown')

        elif message.text == "Әскери-патриоттық клубтарының, балалар мен жасөспірімдер қозғалысының қызметі":
            bot.send_message(message.chat.id, '[Әскери-патриоттық клубтарының, балалар мен жасөспірімдер қозғалысының қызметі](https://telegra.ph/%D3%98skeri-patriotty%D2%9B-klubtaryny%D2%A3-balalar-men-zhas%D3%A9sp%D1%96r%D1%96mder-%D2%9Boz%D2%93alysyny%D2%A3-%D2%9Byzmet%D1%96-09-07)', parse_mode='Markdown')



        elif message.text == "Құқықтық тәрбие":
            bot.send_message(message.chat.id, '[Құқықтық тәрбие](https://telegra.ph/%D2%9A%D2%B1%D2%9By%D2%9Bty%D2%9B-t%D3%99rbie-09-07)', parse_mode='Markdown')

        elif message.text == "Инклюзивті мәдениет":
            bot.send_message(message.chat.id, '[Инклюзивті мәдениет](https://telegra.ph/Inklyuzivt%D1%96-m%D3%99deniet-09-07)', parse_mode='Markdown')


        elif message.text == "◀️ Қайту":
                    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
                    user_markup.row("Жаңа қазақстандық патриотизм мен азаматтыққа тәрбиелеу, құқықтық тәрбие")
                    user_markup.row("Рухани-танымдық тәрбие")
                    user_markup.row("Ұлттық тәрбие")
                    user_markup.row("Отбасылық тәрбие")
                    user_markup.row("Еңбек, экономикалық және экологиялық тәрбие")
                    user_markup.row("Көпмәдениетті және көркем-эстетикалық тәрбие")
                    user_markup.row("Зияткерлік тәрбие, ақпараттық мәдениетті тәрбиелеу")
                    user_markup.row("Дене тәрбиесі, салауатты өмір салтын қалыптастыру")
                    user_markup.row("◀️ Қайту")
                    db.reference("/bot/users/"+str(user_id)).update({"current": "block_3/4/1"})
        else:
                bot.send_message(message.from_user.id,"Қате! Төмендегілердің бірін таңдаңыз.")





    elif current == "block_3/5":

        if message.text == "Мектепалды даярлық топтары сыныптары":
            bot.send_message(message.chat.id, '[Мектепалды даярлық топтары  сыныптары](https://telegra.ph/NPA-kasayushchiesya-sistemy-srednego-obrazovaniya-utverzhdennye-na-osnovanii-Zakona-O-statuse-pedagoga-06-13) || [На компьютере 💻](https://tgraph.io/NPA-kasayushchiesya-sistemy-srednego-obrazovaniya-utverzhdennye-na-osnovanii-Zakona-O-statuse-pedagoga-06-13)', parse_mode='Markdown')



        elif message.text == "Бастауыш білім беру деңгейі":
                user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
                user_markup.row("«ТІЛ ЖӘНЕ ӘДЕБИЕТ» БІЛІМ САЛАСЫ")
                user_markup.row("«МАТЕМАТИКА ЖӘНЕ ИНФОРМАТИКА» БІЛІМ САЛАСЫ")
                user_markup.row("«ЖАРАТЫЛЫСТАНУ» БІЛІМ САЛАСЫ")
                user_markup.row("«АДАМ ЖӘНЕ ҚОҒАМ» БІЛІМ САЛАСЫ")
                user_markup.row("«ТЕХНОЛОГИЯ ЖӘНЕ ӨНЕР» БІЛІМ САЛАСЫ")
                user_markup.row("«ДЕНЕ ШЫНЫҚТЫРУ» БІЛІМ САЛАСЫ")
                user_markup.row("Инклюзивті білім беру")
                user_markup.row("Арнайы мектептерде/сыныптарда білім беру")
                user_markup.row("◀️ Қайту")
                bot.send_message(message.from_user.id,'[Бастауыш білім беру деңгейі](https://telegra.ph/Bastauysh-bіlіm-beru-deңgejі-09-09)',parse_mode='Markdown', reply_markup = user_markup)
                db.reference("/bot/users/"+str(user_id)).update({"current": "block_3/5/2"})

        elif message.text == "Негізгі орта білім беру деңгейі":
                user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
                user_markup.row("«ТІЛ ЖӘНЕ ӘДЕБИЕТ» БІЛІМ САЛАСЫ")
                user_markup.row("«МАТЕМАТИКА ЖӘНЕ ИНФОРМАТИКА» БІЛІМ  САЛАСЫ")
                user_markup.row("«ЖАРАТЫЛЫСТАНУ» БІЛІМ САЛАСЫ")
                user_markup.row("«АДАМ ЖӘНЕ ҚОҒАМ» БІЛІМ САЛАСЫ")
                user_markup.row("«ТЕХНОЛОГИЯ ЖӘНЕ ӨНЕР» БІЛІМ САЛАСЫ")
                user_markup.row("«ДЕНЕ ШЫНЫҚТЫРУ» БІЛІМ САЛАСЫ")
                user_markup.row("Инклюзивті білім беру")
                user_markup.row("Арнайы мектептерде/сыныптарда білім беру")
                user_markup.row("◀️ Қайту")
                db.reference("/bot/users/"+str(user_id)).update({"current": "block_3/5/3"})
                bot.send_message(message.from_user.id,'[Негізгі орта білім беру деңгейі](https://telegra.ph/Negіzgі-orta-bіlіm-beru-deңgejі-09-09)',parse_mode='Markdown', reply_markup = user_markup)

        elif message.text == "Жалпы орта білім беру деңгейі":
                user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
                user_markup.row("«ТІЛ ЖӘНЕ ӘДЕБИЕТ» БІЛІМ САЛАСЫ")
                user_markup.row("«МАТЕМАТИКА ЖӘНЕ ИНФОРМАТИКА» БІЛІМ  САЛАСЫ")
                user_markup.row("«ЖАРАТЫЛЫСТАНУ» БІЛІМ САЛАСЫ")
                user_markup.row("«АДАМ ЖӘНЕ ҚОҒАМ» БІЛІМ САЛАСЫ")
                user_markup.row("«ДЕНЕ ШЫНЫҚТЫРУ» БІЛІМ САЛАСЫ")
                user_markup.row("Инклюзивті білім беру")
                user_markup.row("◀️ Қайту")
                db.reference("/bot/users/"+str(user_id)).update({"current": "block_3/5/4"})
                bot.send_message(message.from_user.id,'[Жалпы орта білім беру деңгейі](https://telegra.ph/ZHalpy-orta-bіlіm-beru-deңgejі-09-09)',parse_mode='Markdown', reply_markup = user_markup)



        elif message.text == "◀️ Қайту":
            user_id = message.from_user.id
            user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
            user_markup.row("Нормативтік-құқықтық қамтамасыз ету")
            user_markup.row("Қазіргі білім берудің дамуындағы тенденциялары")
            user_markup.row("Білім беру жүйесіндегі педагог")
            user_markup.row("Тәрбие жұмысы")
            user_markup.row("2020-2021 оқу жылында білім беру процесін ұйымдастыру")
            user_markup.row("Бағалау жүйесі")
            user_markup.row("Шағынжинақты мектепті оқу-әдістемелік қамтамасыз ету")
            user_markup.row("Ресурстар")
            user_markup.row("Пилоттық білім беру ұйымдарында бағдарламаларын сынақтан өткізу")
            user_markup.row("Қосымша")
            user_markup.row("◀️ Қайту")
            db.reference("/bot/users/"+str(user_id)).update({"lang": "Қазақша"})
            bot.send_message(user_id,"Мазмұны",reply_markup = user_markup)

            db.reference("/bot/users/"+str(user_id)).update({"current": "block_3"})
        else:
                bot.send_message(message.from_user.id,"Қате! Төмендегілердің бірін таңдаңыз.")



    elif current == "block_3/5/2":


        if message.text == "«ТІЛ ЖӘНЕ ӘДЕБИЕТ» БІЛІМ САЛАСЫ":
                user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
                user_markup.row("Сауат ашу")
                user_markup.row("Қазақ тілі (Т1)")
                user_markup.row("Әдебиеттік оқу")
                user_markup.row("Русский язык (Я2)")
                user_markup.row("Шетел тілі")
                user_markup.row("◀️ Қайту")
                db.reference("/bot/users/"+str(user_id)).update({"current": "block_3/5/2/1"})
                bot.send_message(message.from_user.id,"        «Тіл және әдебиет» білім саласының мазмұны «Сауат ашу», «Обучение грамоте», «Қазақ тілі» (Т1), «Русский язык» (Я1), «Әдебиеттік оқу», «Литературное чтение», оқыту орыс тілінде емес сыныптарда «Орыс тілі» (Я2), оқыту қазақ тілінде емес сыныптарда «Қазақ тілі» (Т2), «Ағылшын тілі» оқу пәндері арқылы жүзеге асырылады.  \n       Тілдік пәндерді оқытудың ерекшелігі коммуникативтік тәсілді жүзеге асыру болып табылады. Коммуникативтік дағдыларды ортақ тақырыптарды оқыту барысында қалыптастыру қажет. Коммуникативтік тәсіл білім алушылардың оқу сауаттылығын дамыту мақсатын көздейді, яғни мәтіндерді түсіну және оларға рефлексия жасау қабілетін дамытуға, олардың мазмұнын өз мақсаттарына қол жеткізу үшін пайдалануға, білімдерін және мүмкіндіктерін арттыруға, қоғам өміріне белсенді қатысуға бағытталған.",reply_markup = user_markup)

        elif message.text == "«МАТЕМАТИКА ЖӘНЕ ИНФОРМАТИКА» БІЛІМ САЛАСЫ":
                user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
                user_markup.row("Математика")
                user_markup.row("Ақпараттық-коммуникациялық технологиялар")
                user_markup.row("◀️ Қайту")
                db.reference("/bot/users/"+str(user_id)).update({"current": "block_3/5/2/1"})
                bot.send_message(message.from_user.id,"«Математика және информатика» білім беру саласының мазмұны «Математика» және «Ақпараттық-коммуникациялық технологиялар» пәндері арқылы жүзеге асырылады.",reply_markup = user_markup)

        elif message.text == "«ЖАРАТЫЛЫСТАНУ» БІЛІМ САЛАСЫ":
            bot.send_message(message.chat.id, '[«ЖАРАТЫЛЫСТАНУ» БІЛІМ САЛАСЫ](https://telegra.ph/ZHARATYLYSTANU-BІLІM-SALASY-09-09)', parse_mode='Markdown')


        elif message.text == "«АДАМ ЖӘНЕ ҚОҒАМ» БІЛІМ САЛАСЫ":
                user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
                user_markup.row("Дүниетану")
                user_markup.row("Өзін-өзі тану")
                user_markup.row("◀️ Қайту")
                db.reference("/bot/users/"+str(user_id)).update({"current": "block_3/5/2/1"})
                bot.send_message(message.from_user.id,"«Адам және қоғам» білім беру саласының мазмұны «Дүниетану» және «Өзін-өзі тану» пәндері арқылы беріледі.",reply_markup = user_markup)

        elif message.text == "«ТЕХНОЛОГИЯ ЖӘНЕ ӨНЕР» БІЛІМ САЛАСЫ":
                user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
                user_markup.row("Музыка")
                user_markup.row("Көркем еңбек")
                user_markup.row("◀️ Қайту")
                db.reference("/bot/users/"+str(user_id)).update({"current": "block_3/5/2/1"})
                bot.send_message(message.from_user.id,"«Технология және өнер» білім саласының мазмұнына «Көркем еңбек» және «Музыка» пәндері енгізіледі.",reply_markup = user_markup)

        elif message.text == "«ДЕНЕ ШЫНЫҚТЫРУ» БІЛІМ САЛАСЫ":
            bot.send_message(message.chat.id, '[«ДЕНЕ ШЫНЫҚТЫРУ» БІЛІМ САЛАСЫ](https://telegra.ph/DENE-SHYNYҚTYRU-BІLІM-SALASY-09-09)', parse_mode='Markdown')

        elif message.text == "Инклюзивті білім беру":
            bot.send_message(message.chat.id, '[Инклюзивті білім беру](https://telegra.ph/Inklyuzivtі-bіlіm-beru-09-09)', parse_mode='Markdown')

        elif message.text == "Арнайы мектептерде/сыныптарда білім беру":
            bot.send_message(message.chat.id, '[Арнайы мектептерде/сыныптарда білім беру](https://telegra.ph/Arnajy-mektepterdesynyptarda-bіlіm-beru-09-09)', parse_mode='Markdown')



        elif message.text == "◀️ Қайту":

            user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
            user_markup.row("Мектепалды даярлық топтары сыныптары")
            user_markup.row("Бастауыш білім беру деңгейі")
            user_markup.row("Негізгі орта білім беру деңгейі")
            user_markup.row("Жалпы орта білім беру деңгейі")
            user_markup.row("◀️ Қайту")
            db.reference("/bot/users/"+str(user_id)).update({"current": "block_3/5"})
            bot.send_message(message.from_user.id,"Таңдаңыз:",reply_markup = user_markup)

        else:
                bot.send_message(message.from_user.id,"Қате! Төмендегілердің бірін таңдаңыз.")


    elif current == "block_3/5/2/1":

        if message.text == "Сауат ашу":
            bot.send_message(message.chat.id, '[Сауат ашу](https://telegra.ph/Sauat-ashu-09-09)', parse_mode='Markdown')

        elif message.text == "Қазақ тілі (Т1)":
            bot.send_message(message.chat.id, '[Қазақ тілі (Т1)](https://telegra.ph/Қazaқ-tіlі-T1-09-09)', parse_mode='Markdown')

        elif message.text == "Әдебиеттік оқу":
            bot.send_message(message.chat.id, '[Әдебиеттік оқу](https://telegra.ph/Әdebiettіk-oқu-09-09)', parse_mode='Markdown')

        elif message.text == "Русский язык (Я2)":
            bot.send_message(message.chat.id, '[Русский язык (Я2)](https://telegra.ph/Russkij-yazyk-YA2-09-09)', parse_mode='Markdown')

        elif message.text == "Шетел тілі":
            bot.send_message(message.chat.id, '[Шетел тілі](https://telegra.ph/SHetel-tіlі-09-09)', parse_mode='Markdown')

        elif message.text == "Математика":
            bot.send_message(message.chat.id, '[Математика](https://telegra.ph/Matematika-09-09)', parse_mode='Markdown')

        elif message.text == "Ақпараттық-коммуникациялық технологиялар":
            bot.send_message(message.chat.id, '[Ақпараттық-коммуникациялық технологиялар](https://telegra.ph/Aқparattyқ-kommunikaciyalyқ-tehnologiyalar-09-09)', parse_mode='Markdown')

        elif message.text == "Дүниетану":
            bot.send_message(message.chat.id, '[Дүниетану](https://telegra.ph/Dүnietanu-09-09)', parse_mode='Markdown')

        elif message.text == "Өзін-өзі тану":
            bot.send_message(message.chat.id, '[Өзін-өзі тану](https://telegra.ph/Өzіn-өzі-tanu-09-09)', parse_mode='Markdown')

        elif message.text == "Музыка":
            bot.send_message(message.chat.id, '[Музыка](https://telegra.ph/Muzyka-09-09)', parse_mode='Markdown')

        elif message.text == "Көркем еңбек":
            bot.send_message(message.chat.id, '[Көркем еңбек](https://telegra.ph/Kөrkem-eңbek-09-09)', parse_mode='Markdown')


        elif message.text == "◀️ Қайту":
                user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
                user_markup.row("«ТІЛ ЖӘНЕ ӘДЕБИЕТ» БІЛІМ САЛАСЫ")
                user_markup.row("«МАТЕМАТИКА ЖӘНЕ ИНФОРМАТИКА» БІЛІМ САЛАСЫ")
                user_markup.row("«ЖАРАТЫЛЫСТАНУ» БІЛІМ САЛАСЫ")
                user_markup.row("«АДАМ ЖӘНЕ ҚОҒАМ» БІЛІМ САЛАСЫ")
                user_markup.row("«ТЕХНОЛОГИЯ ЖӘНЕ ӨНЕР» БІЛІМ САЛАСЫ")
                user_markup.row("«ДЕНЕ ШЫНЫҚТЫРУ» БІЛІМ САЛАСЫ")
                user_markup.row("Инклюзивті білім беру")
                user_markup.row("Арнайы мектептерде/сыныптарда білім беру")
                user_markup.row("◀️ Қайту")
                db.reference("/bot/users/"+str(user_id)).update({"current": "block_3/5/2"})
                bot.send_message(message.from_user.id,"Таңдаңыз:",reply_markup = user_markup)


        else:
                bot.send_message(message.from_user.id,"Қате! Төмендегілердің бірін таңдаңыз.")


    elif current == "block_3/5/3":


        if message.text == "«ТІЛ ЖӘНЕ ӘДЕБИЕТ» БІЛІМ САЛАСЫ":
                user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
                user_markup.row("Қазақ тілі")
                user_markup.row("Қазақ әдебиеті")
                user_markup.row("Русский язык и литература")
                user_markup.row("Абайтану")
                user_markup.row("Шетел тілі")

                user_markup.row("◀️ Қайту")

                db.reference("/bot/users/"+str(user_id)).update({"current": "block_3/5/3/1"})
                bot.send_message(message.from_user.id,"        «ТІЛ ЖӘНЕ ӘДЕБИЕТ» БІЛІМ САЛАСЫ АЯСЫНДА КЕЛЕСІ ПӘНДЕР ОҚЫТЫЛАДЫ: \n"
                                                      "         «Қазақ тілі», «Русский язык», «Қазақ әдебиеті», «Русская литература», «Қазақ тілі мен әдебиеті», «Русский язык и литература», «Родной язык», «Ұйғыр/Өзбек/Тәжік әдебиеті», «Шетел тілі ».",reply_markup = user_markup)

        elif message.text == "«МАТЕМАТИКА ЖӘНЕ ИНФОРМАТИКА» БІЛІМ  САЛАСЫ":
            bot.send_message(message.chat.id, '[«МАТЕМАТИКА ЖӘНЕ ИНФОРМАТИКА» БІЛІМ  САЛАСЫ](https://telegra.ph/MATEMATIKA-ZHӘNE-INFORMATIKA-BІLІM-SALASY-09-10)', parse_mode='Markdown')
            bot.send_message(message.chat.id, '[«Информатика» оқу пәні](https://telegra.ph/Informatika-oқu-pәnі-09-10)', parse_mode='Markdown')

        elif message.text == "«ЖАРАТЫЛЫСТАНУ» БІЛІМ САЛАСЫ":
                user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
                user_markup.row("Жаратылыстану")
                user_markup.row("Физика")
                user_markup.row("География")
                user_markup.row("Биология")
                user_markup.row("Химия")
                user_markup.row("◀️ Қайту")
                db.reference("/bot/users/"+str(user_id)).update({"current": "block_3/5/3/1"})
                bot.send_message(message.from_user.id,'[«ЖАРАТЫЛЫСТАНУ» БІЛІМ САЛАСЫ](https://telegra.ph/ZHARATYLYSTANU-BІLІM-SALASY-09-10)',parse_mode='Markdown', reply_markup = user_markup)


        elif message.text == "«АДАМ ЖӘНЕ ҚОҒАМ» БІЛІМ САЛАСЫ":
                user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
                user_markup.row("Қазақстан тарихы және Дүниежүзі тарихы")
                user_markup.row("Құқық негіздері")
                user_markup.row("Зайырлылық және дінтану негіздері")
                user_markup.row("Өзін-өзі тану")

                user_markup.row("◀️ Қайту")
                db.reference("/bot/users/"+str(user_id)).update({"current": "block_3/5/3/1"})
                bot.send_message(message.from_user.id,"    «Адам және қоғам» білім беру саласының оқу пәндерінің мазмұны «Қазақстан тарихы», «Дүниежүзі тарихы», «Құқық негіздері» және «Өзін-өзі тану» оқу пәндерінде іске асырылады. \n" \
                                                      "    «Адам және қоғам» білім беру саласының мазмұны білім алушыларда «Адам – Қоғам» жүйесі шеңберінде қоғамдық-гуманитарлық ғылымдар бойынша білім негіздерін қалыптастыруға бағытталады.",reply_markup = user_markup)

        elif message.text == "«ТЕХНОЛОГИЯ ЖӘНЕ ӨНЕР» БІЛІМ САЛАСЫ":
                user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
                user_markup.row("Музыка")
                user_markup.row("Көркем еңбек")
                user_markup.row("◀️ Қайту")
                db.reference("/bot/users/"+str(user_id)).update({"current": "block_3/5/3/1"})
                bot.send_message(message.from_user.id,"«Технология және өнер» білім саласы бойынша келесі пәндер оқытылады: «Музыка» – 5-6-сыныптар, «Көркем еңбек» – 5-9-сыныптар.",reply_markup = user_markup)

        elif message.text == "«ДЕНЕ ШЫНЫҚТЫРУ» БІЛІМ САЛАСЫ":
            bot.send_message(message.chat.id, '[«ДЕНЕ ШЫНЫҚТЫРУ» БІЛІМ САЛАСЫ](https://telegra.ph/DENE-SHYNYҚTYRU-BІLІM-SALASY-09-10)', parse_mode='Markdown')

        elif message.text == "Инклюзивті білім беру":
            bot.send_message(message.chat.id, '[Инклюзивті білім беру](https://telegra.ph/Inklyuzivtі-bіlіm-beru-09-10)', parse_mode='Markdown')

        elif message.text == "Арнайы мектептерде/сыныптарда білім беру":
            bot.send_message(message.chat.id, '[Арнайы мектептерде/сыныптарда білім беру](https://telegra.ph/Arnajy-mektepterdesynyptarda-bіlіm-beru-09-10)', parse_mode='Markdown')


        elif message.text == "◀️ Қайту":

            user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
            user_markup.row("Мектепалды даярлық топтары сыныптары")
            user_markup.row("Бастауыш білім беру деңгейі")
            user_markup.row("Негізгі орта білім беру деңгейі")
            user_markup.row("Жалпы орта білім беру деңгейі")
            user_markup.row("◀️ Қайту")
            db.reference("/bot/users/"+str(user_id)).update({"current": "block_3/5"})
            bot.send_message(message.from_user.id,"Таңдаңыз:",reply_markup = user_markup)

        else:
                bot.send_message(message.from_user.id,"Қате! Төмендегілердің бірін таңдаңыз.")



    elif current == "block_3/5/3/1":

        if message.text == "Қазақ тілі":
            bot.send_message(message.chat.id, '[Қазақ тілі](https://telegra.ph/Қazaқ-tіlі-09-10)', parse_mode='Markdown')

        elif message.text == "Қазақ әдебиеті":
            bot.send_message(message.chat.id, '[Қазақ әдебиеті](https://telegra.ph/Қazaқ-әdebietі-09-10)', parse_mode='Markdown')

        elif message.text == "Русский язык и литература":
            bot.send_message(message.chat.id, '[Русский язык и литература](https://telegra.ph/Russkij-yazyk-i-literatura-09-10)', parse_mode='Markdown')

        elif message.text == "Абайтану":
            bot.send_message(message.chat.id, '[Абайтану](https://telegra.ph/Abajtanu-09-10)', parse_mode='Markdown')

        elif message.text == "Шетел тілі":
            bot.send_message(message.chat.id, '[Шетел тілі](https://telegra.ph/SHetel-tіlі-09-10)', parse_mode='Markdown')

        elif message.text == "Жаратылыстану":
            bot.send_message(message.chat.id, '[Жаратылыстану](https://telegra.ph/ZHaratylystanu-09-10)', parse_mode='Markdown')

        elif message.text == "Физика":
            bot.send_message(message.chat.id, '[Физика](https://telegra.ph/Fizika-09-10-2)', parse_mode='Markdown')

        elif message.text == "География":
            bot.send_message(message.chat.id, '[География](https://telegra.ph/Geografiya-09-10-2)', parse_mode='Markdown')

        elif message.text == "Биология":
            bot.send_message(message.chat.id, '[Биология](https://telegra.ph/Biologiya-09-10-2)', parse_mode='Markdown')

        elif message.text == "Химия":
            bot.send_message(message.chat.id, '[Химия](https://telegra.ph/Himiya-09-10-2)', parse_mode='Markdown')

        elif message.text == "Қазақстан тарихы және Дүниежүзі тарихы":
            bot.send_message(message.chat.id, '[Қазақстан тарихы және Дүниежүзі тарихы](https://telegra.ph/Қazaқstan-tarihy-zhәne-Dүniezhүzі-tarihy-09-10)', parse_mode='Markdown')

        elif message.text == "Құқық негіздері":
            bot.send_message(message.chat.id, '[Құқық негіздері](https://telegra.ph/Құқyқ-negіzderі-09-10)', parse_mode='Markdown')

        elif message.text == "Зайырлылық және дінтану негіздері":
            bot.send_message(message.chat.id, '[Зайырлылық және дінтану негіздері](https://telegra.ph/Zajyrlylyқ-zhәne-dіntanu-negіzderі-09-10)', parse_mode='Markdown')

        elif message.text == "Өзін-өзі тану":
            bot.send_message(message.chat.id, '[Өзін-өзі тану](https://telegra.ph/Өzіn-өzі-tanu-09-10)', parse_mode='Markdown')

        elif message.text == "Музыка":
            bot.send_message(message.chat.id, '[Музыка](https://telegra.ph/Muzyka-09-10)', parse_mode='Markdown')

        elif message.text == "Көркем еңбек":
            bot.send_message(message.chat.id, '[Көркем еңбек](https://telegra.ph/Kөrkem-eңbek-09-10)', parse_mode='Markdown')


        elif message.text == "◀️ Қайту":

                user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
                user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
                user_markup.row("«ТІЛ ЖӘНЕ ӘДЕБИЕТ» БІЛІМ САЛАСЫ")
                user_markup.row("«МАТЕМАТИКА ЖӘНЕ ИНФОРМАТИКА» БІЛІМ  САЛАСЫ")
                user_markup.row("«ЖАРАТЫЛЫСТАНУ» БІЛІМ САЛАСЫ")
                user_markup.row("«АДАМ ЖӘНЕ ҚОҒАМ» БІЛІМ САЛАСЫ")
                user_markup.row("«ТЕХНОЛОГИЯ ЖӘНЕ ӨНЕР» БІЛІМ САЛАСЫ")
                user_markup.row("«ДЕНЕ ШЫНЫҚТЫРУ» БІЛІМ САЛАСЫ")
                user_markup.row("Инклюзивті білім беру")
                user_markup.row("Арнайы мектептерде/сыныптарда білім беру")
                user_markup.row("◀️ Қайту")
                db.reference("/bot/users/"+str(user_id)).update({"current": "block_3/5/3"})
                bot.send_message(message.from_user.id,"Таңдаңыз:",reply_markup = user_markup)

        else:
                bot.send_message(message.from_user.id,"Қате! Төмендегілердің бірін таңдаңыз.")



    elif current == "block_3/5/4":


        if message.text == "ТІЛ ЖӘНЕ ӘДЕБИЕТ» БІЛІМ САЛАСЫ":
                user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
                user_markup.row("Қазақ тілі")
                user_markup.row("Қазақ әдебиеті")
                user_markup.row("Русский язык и литература")
                user_markup.row("Шетел тілі")
                user_markup.row("Абайтану")
                user_markup.row("◀️ Қайту")
                db.reference("/bot/users/"+str(user_id)).update({"current": "block_3/5/4/1"})
                bot.send_message(message.from_user.id,"         «Тіл және әдебиет» білім беру саласы аясында келесі пәндер оқытылады: «Қазақ тілі», «Орыс тілі», «Қазақ әдебиеті», «Орыс әдебиеті», « Қазақ тілі мен әдебиеті», «Орыс тілі мен әдебиеті», «Шетел тілі».",reply_markup = user_markup)

        elif message.text == "«МАТЕМАТИКА ЖӘНЕ ИНФОРМАТИКА» БІЛІМ  САЛАСЫ":
            bot.send_message(message.chat.id, '[«МАТЕМАТИКА ЖӘНЕ ИНФОРМАТИКА» БІЛІМ  САЛАСЫ](https://telegra.ph/MATEMATIKA-ZH%D3%98NE-INFORMATIKA-B%D0%86L%D0%86M-SALASY-09-10-2)', parse_mode='Markdown')

        elif message.text == "«ЖАРАТЫЛЫСТАНУ» БІЛІМ САЛАСЫ":
                user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
                user_markup.row("Физика")
                user_markup.row("География")
                user_markup.row("Биология")
                user_markup.row("Химия")
                user_markup.row("◀️ Қайту")
                db.reference("/bot/users/"+str(user_id)).update({"current": "block_3/5/4/1"})
                bot.send_message(message.from_user.id,"    «Жаратылыстану» білім саласы бойынша жаңартылған оқу бағдарламаларымен келесі пәндер оқытылады: «Физика», «География», «Биология», «Химия».",reply_markup = user_markup)


        elif message.text == "«АДАМ ЖӘНЕ ҚОҒАМ» БІЛІМ САЛАСЫ":
                user_markup = telebot.types.ReplyKeyboardMarkup(True, True)

                user_markup.row("Қазақстан тарихы")
                user_markup.row("Дүниежүзі тарихы")
                user_markup.row("Құқық негіздері")
                user_markup.row("Өзін-өзі тану")
                user_markup.row("Кәсіпкерлік және бизнес негіздері")
                user_markup.row("Графика және жобалау")


                user_markup.row("◀️ Қайту")
                db.reference("/bot/users/"+str(user_id)).update({"current": "block_3/5/4/1"})
                bot.send_message(message.from_user.id,'[«АДАМ ЖӘНЕ ҚОҒАМ» БІЛІМ САЛАСЫ](https://telegra.ph/ADAM-ZH%D3%98NE-%D2%9AO%D2%92AM-B%D0%86L%D0%86M-SALASY-09-10)',parse_mode='Markdown', reply_markup = user_markup)


        elif message.text == "«ДЕНЕ ШЫНЫҚТЫРУ» БІЛІМ САЛАСЫ":
                user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
                user_markup.row("Дене шынықтыру")
                user_markup.row("Алғашқы әскери және технологиялық дайындық")
                user_markup.row("◀️ Қайту")
                db.reference("/bot/users/"+str(user_id)).update({"current": "block_3/5/4/1"})
                bot.send_message(message.from_user.id,"Таңдаңыз",reply_markup = user_markup)

        elif message.text == "Инклюзивті білім беру":
            bot.send_message(message.chat.id, '[Инклюзивті білім беру](https://telegra.ph/Inklyuzivtі-bіlіm-beru-09-10-2)', parse_mode='Markdown')
            bot.send_message(message.chat.id, '[Инклюзивті білім беру (2)](https://telegra.ph/Inklyuzivtі-bіlіm-beru-2-09-10)', parse_mode='Markdown')


        elif message.text == "◀️ Қайту":

            user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
            user_markup.row("Мектепалды даярлық топтары сыныптары")
            user_markup.row("Бастауыш білім беру деңгейі")
            user_markup.row("Негізгі орта білім беру деңгейі")
            user_markup.row("Жалпы орта білім беру деңгейі")
            user_markup.row("◀️ Қайту")
            db.reference("/bot/users/"+str(user_id)).update({"current": "block_3/5"})
            bot.send_message(message.from_user.id,"Таңдаңыз:",reply_markup = user_markup)

        else:
                bot.send_message(message.from_user.id,"Қате! Төмендегілердің бірін таңдаңыз.")


    elif current == "block_3/5/4/1":

        if message.text == "Қазақ тілі":
            bot.send_message(message.chat.id, '[Қазақ тілі](https://telegra.ph/%D2%9Aaza%D2%9B-t%D1%96l%D1%96-o%D2%9Bytu-%D2%9Baza%D2%9B-t%D1%96l%D1%96nde-09-10)', parse_mode='Markdown')

        elif message.text == "Қазақ әдебиеті":
            bot.send_message(message.chat.id, '[Қазақ әдебиеті](https://telegra.ph/%D2%9Aaza%D2%9B-%D3%99debiet%D1%96-o%D2%9Bu-p%D3%99n%D1%96-o%D2%9Bytu-%D2%9Baza%D2%9B-t%D1%96l%D1%96nde-09-10)', parse_mode='Markdown')

        elif message.text == "Русский язык и литература":
            bot.send_message(message.chat.id, '[Русский язык и литература](https://telegra.ph/Russkij-yazyk-i-literatura-o%D2%9Bu-p%D3%99n%D1%96-o%D2%9Bytu-orys-t%D1%96l%D1%96nde-emes-09-10)', parse_mode='Markdown')

        elif message.text == "Шетел тілі":
            bot.send_message(message.chat.id, '[Шетел тілі](https://telegra.ph/SHetel-t%D1%96l%D1%96-o%D2%9Bu-p%D3%99n%D1%96-09-10)', parse_mode='Markdown')

        elif message.text == "Абайтану":
            bot.send_message(message.chat.id, '[Абайтану](https://telegra.ph/Abajtanu-fakultativ-kursy-09-10)', parse_mode='Markdown')

        elif message.text == "Физика":
            bot.send_message(message.chat.id, '[Физика](https://telegra.ph/Fizika-o%D2%9Bu-p%D3%99n%D1%96-09-10)', parse_mode='Markdown')

        elif message.text == "География":
            bot.send_message(message.chat.id, '[География](https://telegra.ph/Geografiya-o%D2%9Bu-p%D3%99n%D1%96-09-10)', parse_mode='Markdown')

        elif message.text == "Биология":
            bot.send_message(message.chat.id, '[Биология](https://telegra.ph/Biologiya-o%D2%9Bu-p%D3%99n%D1%96-09-10)', parse_mode='Markdown')

        elif message.text == "Химия":
            bot.send_message(message.chat.id, '[Химия](https://telegra.ph/Himiya-o%D2%9Bu-p%D3%99n%D1%96-09-10)', parse_mode='Markdown')

        elif message.text == "Қазақстан тарихы":
            bot.send_message(message.chat.id, '[Қазақстан тарихы](https://telegra.ph/%D2%9Aaza%D2%9Bstan-tarihy-o%D2%9Bu-p%D3%99n%D1%96-09-10)', parse_mode='Markdown')

        elif message.text == "Дүниежүзі тарихы":
            bot.send_message(message.chat.id, '[Дүниежүзі тарихы](https://telegra.ph/D%D2%AFniezh%D2%AFz%D1%96-tarihy-o%D2%9Bu-p%D3%99n%D1%96-09-10)', parse_mode='Markdown')

        elif message.text == "Құқық негіздері":
            bot.send_message(message.chat.id, '[Құқық негіздері](https://telegra.ph/%D2%9A%D2%B1%D2%9By%D2%9B-neg%D1%96zder%D1%96-p%D3%99n%D1%96-09-10)', parse_mode='Markdown')

        elif message.text == "Өзін-өзі тану":
            bot.send_message(message.chat.id, '[Өзін-өзі тану](https://telegra.ph/%D3%A8z%D1%96n-%D3%A9z%D1%96-tanu-o%D2%9Bu-p%D3%99n%D1%96-09-10)', parse_mode='Markdown')

        elif message.text == "Кәсіпкерлік және бизнес негіздері":
            bot.send_message(message.chat.id, '[Кәсіпкерлік және бизнес негіздері](https://telegra.ph/K%D3%99s%D1%96pkerl%D1%96k-zh%D3%99ne-biznes-neg%D1%96zder%D1%96-o%D2%9Bu-p%D3%99n%D1%96-09-10)', parse_mode='Markdown')

        elif message.text == "Графика және жобалау":
            bot.send_message(message.chat.id, '[Графика және жобалау](https://telegra.ph/Grafika-zh%D3%99ne-zhobalau-o%D2%9Bu-p%D3%99n%D1%96-09-10https://telegra.ph/Grafika-zh%D3%99ne-zhobalau-o%D2%9Bu-p%D3%99n%D1%96-09-10)', parse_mode='Markdown')

        elif message.text == "Дене шынықтыру":
            bot.send_message(message.chat.id, '[Дене шынықтыру](https://telegra.ph/Dene-shynyқtyru-09-10)', parse_mode='Markdown')

        elif message.text == "Алғашқы әскери және технологиялық дайындық":
            bot.send_message(message.chat.id, '[Алғашқы әскери және технологиялық дайындық](https://telegra.ph/Alғashқy-әskeri-zhәne-tehnologiyalyқ-dajyndyқ-09-10)', parse_mode='Markdown')


        elif message.text == "◀️ Қайту":

                user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
                user_markup.row("«ТІЛ ЖӘНЕ ӘДЕБИЕТ» БІЛІМ САЛАСЫ")
                user_markup.row("«МАТЕМАТИКА ЖӘНЕ ИНФОРМАТИКА» БІЛІМ  САЛАСЫ")
                user_markup.row("«ЖАРАТЫЛЫСТАНУ» БІЛІМ САЛАСЫ")
                user_markup.row("«АДАМ ЖӘНЕ ҚОҒАМ» БІЛІМ САЛАСЫ")
                user_markup.row("«ДЕНЕ ШЫНЫҚТЫРУ» БІЛІМ САЛАСЫ")
                user_markup.row("Инклюзивті білім беру")
                user_markup.row("◀️ Қайту")
                db.reference("/bot/users/"+str(user_id)).update({"current": "block_3/5/4"})
                bot.send_message(message.from_user.id,"Таңдаңыз:",reply_markup = user_markup)


        else:
                bot.send_message(message.from_user.id,"Ошибка! Выберите из перечисленных.")



    elif current == "block_3/6":

        if message.text == "Білім алушылардың жетістіктерін бағалаудың критериалды жүйесі":
            bot.send_message(message.chat.id, '[Білім алушылардың жетістіктерін бағалаудың критериалды жүйесі](https://telegra.ph/B%D1%96l%D1%96m-alushylardy%D2%A3-zhet%D1%96st%D1%96kter%D1%96n-ba%D2%93alaudy%D2%A3-kriterialdy-zh%D2%AFjes%D1%96-09-07)', parse_mode='Markdown')

        elif message.text == "Шектеу шаралары кезінде білім алушылардың оқудағы жетістіктерін бағалау":
            bot.send_message(message.chat.id, '[Шектеу шаралары кезінде білім алушылардың оқудағы жетістіктерін бағалау](https://telegra.ph/SHekteu-sharalary-kez%D1%96nde-b%D1%96l%D1%96m-alushylardy%D2%A3-o%D2%9Buda%D2%93y-zhet%D1%96st%D1%96kter%D1%96n-ba%D2%93alau-09-07)', parse_mode='Markdown')

        elif message.text == "Критериалды бағалау құралдары":
            bot.send_message(message.chat.id, '[Критериалды бағалау құралдары](https://telegra.ph/Kriterialdy-ba%D2%93alau-%D2%9B%D2%B1raldary-09-07)', parse_mode='Markdown')

        elif message.text == "Қалыптастырушы бағалауға балл қою бойынша ЖАДЫНАМА":
            bot.send_message(message.chat.id, '[Қалыптастырушы бағалауға балл қою бойынша ЖАДЫНАМА](https://telegra.ph/%D2%9Aalyptastyrushy-ba%D2%93alau%D2%93a-ball-%D2%9Boyu-bojynsha-ZHADYNAMA-09-07)', parse_mode='Markdown')

        elif message.text == "Критериалды бағалау бойынша Әдістемелік ұсынымдар":
            bot.send_message(message.chat.id, '[Критериалды бағалау бойынша Әдістемелік ұсынымдар](https://telegra.ph/Kriterialdy-ba%D2%93alau-bojynsha-%D3%98d%D1%96stemel%D1%96k-%D2%B1synymdar-09-07)', parse_mode='Markdown')

        elif message.text == "Арнайы мектеп оқушыларын бағалау жүйесі":
            bot.send_message(message.chat.id, '[Арнайы мектеп оқушыларын бағалау жүйесі](https://telegra.ph/Arnajy-mektep-o%D2%9Bushylaryn-ba%D2%93alau-zh%D2%AFjes%D1%96-09-07)', parse_mode='Markdown')

        elif message.text == "Қорытынды аттестаттау өткізу":
            bot.send_message(message.chat.id, '[Қорытынды аттестаттау өткізу](https://telegra.ph/%D2%9AORYTYNDY-ATTESTATTAUDY-%D3%A8TK%D0%86ZU-09-07)', parse_mode='Markdown')



        elif message.text == "◀️ Қайту":
            user_id = message.from_user.id
            user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
            user_markup.row("Нормативтік-құқықтық қамтамасыз ету")
            user_markup.row("Қазіргі білім берудің дамуындағы тенденциялары")
            user_markup.row("Білім беру жүйесіндегі педагог")
            user_markup.row("Тәрбие жұмысы")
            user_markup.row("2020-2021 оқу жылында білім беру процесін ұйымдастыру")
            user_markup.row("Бағалау жүйесі")
            user_markup.row("Шағынжинақты мектепті оқу-әдістемелік қамтамасыз ету")
            user_markup.row("Ресурстар")
            user_markup.row("Пилоттық білім беру ұйымдарында бағдарламаларын сынақтан өткізу")
            user_markup.row("Қосымша")
            user_markup.row("◀️ Қайту")
            db.reference("/bot/users/"+str(user_id)).update({"lang": "Қазақша"})
            bot.send_message(user_id,"Мазмұны",reply_markup = user_markup)

            db.reference("/bot/users/"+str(user_id)).update({"current": "block_3"})
        else:
                bot.send_message(message.from_user.id,"Қате! Төмендегілердің бірін таңдаңыз.")


    else:
        bot.send_message(message.from_user.id,"Ошибка!")







bot.polling(none_stop=True) #в конце. Бесконечно.
