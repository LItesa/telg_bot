import telebot
from telebot import types
import datetime

client = telebot.TeleBot('6928681770:AAHWAOOmBMwTvTa2oKO6OEf9O8-EVxIc5IA')


@client.message_handler(commands=['start'])
def start(message):
    client.send_message(message.chat.id, 'Привет, я бот, который поможет тебе с режимом сна, нажми продолжить')
    start_line = types.InlineKeyboardMarkup()
    item_start = types.InlineKeyboardButton(text='Продолжить', callback_data='Старт')

    start_line.add(item_start)
    client.send_message(message.chat.id, 'Перейти в основные пункты ->', reply_markup=start_line)


@client.message_handler(commands=['time_sleep'])
def time_sleep(message):
    client.send_message(message.chat.id, 'Пока не работает(')
    sleep_but = types.InlineKeyboardMarkup()
    item_sleep = types.InlineKeyboardButton(text='Клик😘', url='https://youtu.be/dQw4w9WgXcQ?si=t_NBc607adcTTWV7')
    item_age = types.InlineKeyboardButton(text='Выберите возраст', callback_data='age')
    sleep_but.add(item_sleep, item_age)
    client.send_message(message.chat.id, 'Можещь жмякнуть на кнопуку', reply_markup=sleep_but)


@client.message_handler(commands=['help'])
def help(message):
    client.send_message(message.chat.id, 'Я пока не умею помогать людям(')
    help_but = types.InlineKeyboardMarkup()
    item_help = types.InlineKeyboardButton(text='Клик🫠', url='https://youtu.be/dQw4w9WgXcQ?si=t_NBc607adcTTWV7')
    help_but.add(item_help)
    client.send_message(message.chat.id, 'Может эта конопка тебе поможет', reply_markup=help_but)


@client.message_handler(commands=['help_sleep'])
def help_sleep(message):
    client.send_message(message.chat.id, 'Какого рода у вас проблемы со сном')
    hp_sp_but = types.InlineKeyboardMarkup()
    item_no_sleep = types.InlineKeyboardButton(text='Инсомния(бессонница)', callback_data='insomnia')
    item_ritm = types.InlineKeyboardButton(text='Нарушение ритма сна', callback_data='ritm')
    item_giper = types.InlineKeyboardButton(text='Гиперсомния', callback_data='giper')
    item_low_time_sleep = types.InlineKeyboardButton(text='Короткий сон', callback_data='low_time')
    item_hight_time_sleep = types.InlineKeyboardButton(text='Длинный сон', callback_data='hight_time')
    hp_sp_but.add(item_no_sleep, item_ritm, item_giper, item_low_time_sleep, item_hight_time_sleep)
    client.send_message(message.chat.id, 'Выберите один из пунктов:', reply_markup=hp_sp_but)


@client.message_handler(content_types=['text'])
def help(message):
    if message.text == 'Команды':
        client.send_message(message.chat.id, 'У нашего бота есть несколько команд: /help, /time_sleep, /help_sleep')
    elif message.text == 'Рекомендации':
        client.send_message(message.chat.id, 'Здесь будут рекомендации по сну, наверное...')


@client.callback_query_handler(func=lambda call: True)
def button_start(call):
    if call.data == 'Старт':
        start_button = types.ReplyKeyboardMarkup(resize_keyboard=True)
        items_st = types.KeyboardButton('Команды')
        start_button.add(types.KeyboardButton('Команды'), types.KeyboardButton('Рекомендации'))
        client.send_message(call.message.chat.id, 'Можешь пожамкать по кнопочкам', reply_markup=start_button)
    elif call.data == '64':
        client.send_message(call.message.chat.id, 'Вам нужно спать от 7 до 9 часов в сутки')
    elif call.data == '17':
        client.send_message(call.message.chat.id, 'Вам нужно спать от 8 до 10 часов в сутки')
    elif call.data == '13':
        client.send_message(call.message.chat.id, 'Вам нужно спать от 9 до 11 часов в сутки')
    elif call.data == 'age':
        age_button = types.InlineKeyboardMarkup()
        item_age_13 = types.InlineKeyboardButton(text='6 - 13', callback_data='13')
        item_age_17 = types.InlineKeyboardButton(text='14 - 17', callback_data='17')
        item_age_64 = types.InlineKeyboardButton(text='18 - 64', callback_data='64')
        item_back = types.InlineKeyboardButton(text='Назад', callback_data='Старт')
        age_button.add(item_age_13, item_age_17, item_age_64, item_back)
        client.send_message(call.message.chat.id, 'Выберите возраст', reply_markup=age_button)
    elif call.data == 'insomnia':
        client.send_message(call.message.chat.id, '*Инсомния*', parse_mode='Markdown')
        client.send_message(call.message.chat.id,
                            'Немного информации про инсомнию: инсомния, или же бессонница, - трудность засыпания и/или поддержания сна.')
        client.send_message(call.message.chat.id,
                            'Симптомы инсомнии: на засыпание уходит более 30 минут, ночные и ранние утренние пробуждения, после которых на засыпание требуется более 30 минут.')
        client.send_message(call.message.chat.id,
                            'Важно помнить, что только врач может поставить вам точный диагноз. Только врач может назначить вам необходимые обследования')
        client.send_message(call.message.chat.id,
                            'Если вы подозревает, что у вас инсомния, то обратитесь к врачу ')
    elif call.data == 'ritm':
        client.send_message(call.message.chat.id, '*Циркадианные нарушения ритма сна-бодорствования*',
                            parse_mode='Markdown')
        client.send_message(call.message.chat.id,
                            'Немного информации про циркадианные нарушения ритма сна-бодрствования: невозможность заснуть в социально-приемлемое время из-за смещения ритмов сна-бодрствования.')
        client.send_message(call.message.chat.id,
                            'Симптомы: трудности засыпания в социально-приемлемое время, более чем на два часа отличающееся от *фактического.')
        client.send_message(call.message.chat.id,
                            'Важно помнить, что только врач может поставить вам точный диагноз. Только врач может назначить вам необходимые обследования')
        client.send_message(call.message.chat.id,
                            'Циркадианные нарушения ритма сна-бодрствования разделяют в зависимости от причин на две категории:')
        client.send_message(call.message.chat.id,
                            'Эндогенные (внутренние причины):\nсиндром задержки ритма сна-бодрствования;\n \nсиндром опережения ритма сна-бодрствования;\n \nнерегулярный ритм сна-бодрствования.')
        client.send_message(call.message.chat.id,
                            'Экзогенные (внешние причины):\n \nинсомния при сменной работе;\n \nджет-лаг (расстройство сна при смене часовых поясов).')
        client.send_message(call.message.chat.id,
                            '_* -> 22:00 - 23:00, в это время снижается уровень гормона стресса кортизола, а уровень мелатонина (гормона сна) наоборот начинает расти_',
                            parse_mode='Markdown')
    # elif call.data == 'giper':


client.polling(non_stop=True, interval=0)