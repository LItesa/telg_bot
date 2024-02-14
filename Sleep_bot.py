import telebot
from telebot import types

client = telebot.TeleBot('6928681770:AAHWAOOmBMwTvTa2oKO6OEf9O8-EVxIc5IA')

f = False
answer_night_up = 0
answer_giper = 0
disorder = ''


@client.message_handler(commands=['start', 'back'])
def start(message):
    global f
    if f is False:
        client.send_message(message.chat.id,
                            'Привет, я бот, который поможет тебе со сном и расскажет о разных расстройствах сна')
        f = True
    start_line = types.InlineKeyboardMarkup()
    item_start = types.InlineKeyboardButton(text='Продолжить', callback_data='Старт')

    start_line.add(item_start)
    client.send_message(message.chat.id, 'Перейти в основные пункты ->', reply_markup=start_line)


@client.message_handler(commands=['time_sleep'])
def time_sleep(message):
    client.send_message(message.chat.id, 'Хочешь узнать сколько нужно спать?')
    sleep_but = types.InlineKeyboardMarkup()
    item_age = types.InlineKeyboardButton(text='Выбрать возраст', callback_data='age')
    sleep_but.add(item_age)
    client.send_message(message.chat.id, 'Нажмите на кнопку', reply_markup=sleep_but)
    f = True


@client.message_handler(commands=['sleep_des'])
def help_sleep(message):
    client.send_message(message.chat.id, 'Информация о расстройствах сна')
    client.send_message(message.chat.id,
                        '‼️Важно помнить, что только врач может поставить вам точный диагноз.‼️')
    hp_sp_but = types.InlineKeyboardMarkup()
    item_no_sleep = types.InlineKeyboardButton(text='Инсомния(бессонница)', callback_data='insomnia')
    item_ritm = types.InlineKeyboardButton(text='Нарушение ритма сна', callback_data='ritm')
    item_giper = types.InlineKeyboardButton(text='Гиперсомнии', callback_data='giper')
    item_low_time_sleep = types.InlineKeyboardButton(text='Короткий сон', callback_data='low_time')
    item_hight_time_sleep = types.InlineKeyboardButton(text='Длинный сон', callback_data='high_time')
    hp_sp_but.add(item_no_sleep, item_ritm, item_giper, item_low_time_sleep, item_hight_time_sleep)
    client.send_message(message.chat.id, 'Выберите один из пунктов:', reply_markup=hp_sp_but)
    f = True


@client.message_handler(commands=['test'])
def test_start(message):
    global answer_giper
    global answer_night_up
    st_but = types.ReplyKeyboardMarkup(resize_keyboard=True)
    st_but.add(types.KeyboardButton('Да'), types.KeyboardButton('Нет'))
    answ = client.send_message(message.chat.id, '🔵Хотите пройти тест на расстройства сна?', reply_markup=st_but)
    client.register_next_step_handler(answ, user_message)
    answer_giper = 0
    answer_night_up = 0
    f = True


def user_message(message):
    if message.text == 'Да':
        time_button = types.ReplyKeyboardMarkup(resize_keyboard=True)
        time_button.add(types.KeyboardButton('до 30 минут'), types.KeyboardButton('больше 30 минут'))
        answ = client.send_message(message.chat.id, '🔵Сколько времени у вас уходит, что бы заснуть?',
                                   reply_markup=time_button)
        client.register_next_step_handler(answ, asleep)
    elif message.text == 'Нет':
        client.send_message(message.chat.id, 'Введите команду /back')


def asleep(message):
    global answer_night_up
    if message.text == 'больше 30 минут':
        answer_night_up += 1
    answ_but = types.ReplyKeyboardMarkup(resize_keyboard=True)
    answ_but.add(types.KeyboardButton('Да'), types.KeyboardButton('Нет'))
    answ = client.send_message(message.chat.id, '🔵Часто ли вы просыпаетесь ночью или ранним утром?',
                               reply_markup=answ_but)
    client.register_next_step_handler(answ, asleep2)


def asleep2(message):
    global answer_night_up
    if message.text == 'Да':
        time_button = types.ReplyKeyboardMarkup(resize_keyboard=True)
        time_button.add(types.KeyboardButton('до 30 минут'), types.KeyboardButton('больше 30 минут'))
        answ = client.send_message(message.chat.id, '🔵Сколько у вас уходит времени, что бы заснуть после пробуждения?',
                                   reply_markup=time_button)
        client.register_next_step_handler(answ, asleep_ins)
    elif message.text == 'Нет':
        ins_but = types.ReplyKeyboardMarkup(resize_keyboard=True)
        ins_but.add(types.KeyboardButton('Да'), types.KeyboardButton('Нет'))
        answ = client.send_message(message.chat.id, '🔵Тяжолое ли у вас пробуждение?', reply_markup=ins_but)
        client.register_next_step_handler(answ, asleep_ins2)


def asleep_ritm(message):
    global disorder
    if message.text == 'Да':
        client.send_message(message.chat.id, 'Мы подозреваем, что у вас циркадианное нарушение ритма сна-бодрствования')
        client.send_message(message.chat.id, 'Что бы посмотреть рекомендации вернитесь назад и выберите "Рекомендации"')
        client.send_message(message.chat.id, 'Прежде всего мы рекомендуем пройти обследование у врача')
        client.send_message(message.chat.id, 'Что бы вернуться назад введите команду /back')
        disorder = 'ritm'
    elif message.text == 'Нет':
        giper_but = types.ReplyKeyboardMarkup(resize_keyboard=True)
        giper_but.add(types.KeyboardButton('Да'), types.KeyboardButton('Нет'))
        answ = client.send_message(message.chat.id, '🔵У вас были приступы непреодолимой сонливости?',
                                   reply_markup=giper_but)
        client.register_next_step_handler(answ, asleep_giper)


def asleep_giper(message):
    global answer_giper
    if message.text == 'Да':
        answer_giper += 1
    giper_but = types.ReplyKeyboardMarkup(resize_keyboard=True)
    giper_but.add(types.KeyboardButton('Да'), types.KeyboardButton('Нет'))
    answ = client.send_message(message.chat.id, '🔵У вас были приступы внезапного засыпания?', reply_markup=giper_but)
    client.register_next_step_handler(answ, asleep_giper2)


def asleep_giper2(message):
    global answer_giper
    if message.text == 'Да':
        answer_giper += 1
    giper_but = types.ReplyKeyboardMarkup(resize_keyboard=True)
    giper_but.add(types.KeyboardButton('Да'), types.KeyboardButton('Нет'))
    answ = client.send_message(message.chat.id,
                               '🔵У вас были приступы внезапной утраты мышечного тонуса при ясном сознании (когда вы отдаете отчет в том, что происходит с вами и вокруг вас)?',
                               reply_markup=giper_but)
    client.register_next_step_handler(answ, asleep_giper3)


def asleep_giper3(message):
    global answer_giper
    global disorder
    if message.text == 'Да':
        answer_giper += 1
    if answer_giper > 0:
        client.send_message(message.chat.id, 'Мы подозреваем у вас гиперсомнию')
        client.send_message(message.chat.id, 'Что бы посмотреть рекомендации вернитесь назад и выберите "Рекомендации"')
        client.send_message(message.chat.id, 'Прежде всего мы рекомендуем пройти обследование у врача')
        client.send_message(message.chat.id, 'Что бы вернуться назад введите команду /back')
        disorder = 'giper'
    else:
        client.send_message(message.chat.id, 'У вас нет симптомов, какого-либо расстройства сна')
        client.send_message(message.chat.id, 'Что бы вернуться назад введите команду /back')
        disorder = 'None'


def asleep_ins(message):
    global answer_night_up
    if message.text == 'больше 30 минут':
        answer_night_up += 1
    ins_but = types.ReplyKeyboardMarkup(resize_keyboard=True)
    ins_but.add(types.KeyboardButton('Да'), types.KeyboardButton('Нет'))
    answ = client.send_message(message.chat.id, '🔵Тяжолое ли у вас пробуждение?', reply_markup=ins_but)
    client.register_next_step_handler(answ, asleep_ins2)


def asleep_ins2(message):
    global answer_night_up
    if message.text == 'Да':
        answer_night_up += 1
    ins_but = types.ReplyKeyboardMarkup(resize_keyboard=True)
    ins_but.add(types.KeyboardButton('Да'), types.KeyboardButton('Нет'))
    answ = client.send_message(message.chat.id,
                               '🔵Есть ли у вас, что-то из ниже перечисленного: \n чувство усталости; \n головная боль; \n сниженная работоспособность; \n рассеянность.',
                               reply_markup=ins_but)
    client.register_next_step_handler(answ, asleep_ins_end)


def asleep_ins_end(message):
    global answer_night_up
    global disorder
    if answer_night_up >= 1 and (message.text == 'Да' or message.text == 'Нет'):
        client.send_message(message.chat.id, 'Мы подозреаем, что у вас инсомния (бессонница)')
        client.send_message(message.chat.id, 'Что бы посмотреть рекомендации вернитесь назад и выберите "Рекомендации"')
        client.send_message(message.chat.id, 'Прежде всего мы рекомендуем пройти обследование у врача')
        client.send_message(message.chat.id, 'Что бы вернуться назад введите команду /back')
        disorder = 'insomnia'
    elif answer_night_up < 1 and (message.text == 'Нет' or message.text == 'Да'):
        ritm_but = types.ReplyKeyboardMarkup(resize_keyboard=True)
        ritm_but.add(types.KeyboardButton('Да'), types.KeyboardButton('Нет'))
        answ = client.send_message(message.chat.id,
                                   '🔵Есть ли у вас проблемы засыпания в социально-приемлемое время, более чем на два часа отличающееся от фактического (22:00 - 23:00)',
                                   reply_markup=ritm_but)
        client.register_next_step_handler(answ, asleep_ritm)


@client.message_handler(content_types=['text'])
def help(message):
    global disorder
    if message.text == 'Команды':
        client.send_message(message.chat.id,
                            'У нашего бота есть несколько команд:/time_sleep, /sleep_des, /test')
    elif message.text == 'Рекомендации':
        if disorder == '':
            client.send_message(message.chat.id, 'Перед просмотром рекомендаций пройдите тест')
            client.send_message(message.chat.id, 'Для этого введите команду /test')
        elif disorder == 'insomnia':
            client.send_message(message.chat.id,
                                'Прежде всего вам нужно обратиться к сомнологу или неврологу, чем дольше вы откладываете визит, тем сильнее истощается организм')
            client.send_message(message.chat.id,
                                'Лучше всего будет выбрать стабильный ритм жизни, обеспечить достаточное освещение в дневное время, удилять время физ. активности, а также бороться со стрессом и больше отдыхать')
        elif disorder == 'ritm':
            client.send_message(message.chat.id,
                                'Прежде всего вам нужно обратиться к сомнологу или неврологу')
            client.send_message(message.chat.id, 'Вам нужно стараться вставить в одно и тоже время, включая выходные')
            client.send_message(message.chat.id,
                                'Избегать употребления кофеина и алкоголя за несколько часов перед сном')
            client.send_message(message.chat.id, 'Избегать тяжелой физичеакой нагрузки перед сном')
        elif disorder == 'giper':
            client.send_message(message.chat.id, 'Не работайте перед сном, дайте отдохнуть своему организму')
            client.send_message(message.chat.id, 'Нужно спать днем хотябы 40-50 минут')
            client.send_message(message.chat.id, 'Установить будильник на одно и то же время, даже на выходных')
            client.send_message(message.chat.id, 'Установить будильник на одно и то же время, даже на выходных')
        elif disorder == 'None':
            client.send_message(message.chat.id, 'По результатам теста мы не выявили у вас каких-либо расстройств сна')
            client.send_message(message.chat.id,
                                'Не засиживайтесь до глубокой ночи, не злоупотребляйте кофеинов и алкоголем, и тогда у вас не будет никаких проблем со сном)')
    f = True


@client.callback_query_handler(func=lambda call: True)
def button_start(call):
    if call.data == 'Старт':
        start_button = types.ReplyKeyboardMarkup(resize_keyboard=True)
        items_st = types.KeyboardButton('Команды')
        start_button.add(types.KeyboardButton('Команды'), types.KeyboardButton('Рекомендации'))
        client.send_message(call.message.chat.id, 'Выберите одну из кнопок', reply_markup=start_button)
    elif call.data == '64':
        client.send_message(call.message.chat.id, '❗Вам нужно спать от 7 до 9 часов в сутки')
        client.send_message(call.message.chat.id,
                            '• регулирует высвобождение гормонов, которые контролируют ваш аппетит, метаболизм, рост и заживление;\n•  улучшает работу мозга , концентрацию, внимание и продуктивность; \n• снижает риск сердечных заболеваний и инсульта; \n• помогает с контролем веса; \n• поддерживает вашу иммунную систему; \n• снижает риск хронических заболеваний, таких как диабет и высокое кровяное давление; \n• мышцы, которые вы изнашивали весь день, восстанавливаются во время сна; \n• может снизить риск депрессии.')
    elif call.data == '17':
        client.send_message(call.message.chat.id, '❗Вам нужно спать от 8 до 10 часов в сутки')
        client.send_message(call.message.chat.id,
                            'Если недосыпать, то могут появится разные проблемы:\n• Дефицит внимания \n• Проблемы с памятью, забывчивость\n• Сложности с принятием решений\n• Плохое самочувствие \n• Агрессия и перемены настроения \n• Депрессия \n• Лишний вес \n• Рассеянность, результатом которой могут быть травмы')
    elif call.data == '13':
        client.send_message(call.message.chat.id, '❗Вам нужно спать от 9 до 11 часов в сутки')
        client.send_message(call.message.chat.id,
                            '• Сон помогает сердцу \n• Сон помогает бороться с инфекцией. \n• Сон влияет на рост. \n• Сон влияет на вес. \n• Сон снижает риск диабета I типа. \n• Здоровый сон снижает риск травм. \n• Сон влияет на внимание. \n• Сон помогает учиться.')
    elif call.data == 'age':
        age_button = types.InlineKeyboardMarkup()
        item_age_13 = types.InlineKeyboardButton(text='6 - 13', callback_data='13')
        item_age_17 = types.InlineKeyboardButton(text='14 - 17', callback_data='17')
        item_age_64 = types.InlineKeyboardButton(text='18 - 64', callback_data='64')
        item_back = types.InlineKeyboardButton(text='Назад', callback_data='Старт')
        age_button.add(item_age_13, item_age_17, item_age_64, item_back)
        client.send_message(call.message.chat.id, 'Выберите возраст', reply_markup=age_button)
    elif call.data == 'insomnia':
        client.send_message(call.message.chat.id, '🛑*Инсомния (бессонница)*', parse_mode='Markdown')
        client.send_message(call.message.chat.id,
                            'Инсомния, или же бессонница, - трудность засыпания и/или поддержания сна.')
        back_button = types.InlineKeyboardMarkup()
        item_back = types.InlineKeyboardButton(text='Назад', callback_data='Старт')
        back_button.add(item_back)
        client.send_message(call.message.chat.id, 'Нажмите для возвращения', reply_markup=back_button)
    elif call.data == 'ritm':
        client.send_message(call.message.chat.id, '🛑*Циркадианные нарушения ритма сна-бодорствования*',
                            parse_mode='Markdown')
        client.send_message(call.message.chat.id,
                            'Циркадианное нарушение ритма сна-бодрствования: невозможность заснуть в социально-приемлемое время из-за смещения ритмов сна-бодрствования.')
        back_button = types.InlineKeyboardMarkup()
        item_back = types.InlineKeyboardButton(text='Назад', callback_data='Старт')
        back_button.add(item_back)
        client.send_message(call.message.chat.id, 'Нажмите для возвращения', reply_markup=back_button)
    elif call.data == 'giper':
        client.send_message(call.message.chat.id, '🛑*Гиперсомнии*', parse_mode='Markdown')
        client.send_message(call.message.chat.id,
                            'Гиперсомния: сильно выраженная сонливость, не связанная с низким качеством или малым количеством ночного сна (наиболее распространённые заболевания — нарколепсия и идиопатическая гиперсомния).')
        back_button = types.InlineKeyboardMarkup()
        item_back = types.InlineKeyboardButton(text='Назад', callback_data='Старт')
        back_button.add(item_back)
        client.send_message(call.message.chat.id, 'Нажмите для возвращения', reply_markup=back_button)
    elif call.data == 'low_time':
        client.send_message(call.message.chat.id, '🛑*Короткая продолжительность сна*', parse_mode='Markdown')
        client.send_message(call.message.chat.id,
                            'Короткий сон не ялвляется расстройством, но может причинить серьёзный вред здоровью')
        client.send_message(call.message.chat.id, '_-> продолжительность сна меньше 6 часов_', parse_mode='Markdown')
        back_button = types.InlineKeyboardMarkup()
        item_back = types.InlineKeyboardButton(text='Назад', callback_data='Старт')
        back_button.add(item_back)
        client.send_message(call.message.chat.id, 'Нажмите для возвращения', reply_markup=back_button)
    elif call.data == 'high_time':
        client.send_message(call.message.chat.id, '🛑*Длительный сон*', parse_mode='Markdown')
        client.send_message(call.message.chat.id,
                            'Длительный сон не ялвляется расстройством, но может причинить серьёзный вред здоровью')
        client.send_message(call.message.chat.id, '_-> продолжительность сна больше 9 часов_', parse_mode='Markdown')
        back_button = types.InlineKeyboardMarkup()
        item_back = types.InlineKeyboardButton(text='Назад', callback_data='Старт')
        back_button.add(item_back)
        client.send_message(call.message.chat.id, 'Нажмите для возвращения', reply_markup=back_button)
    f = True


client.polling(non_stop=True, interval=0)
