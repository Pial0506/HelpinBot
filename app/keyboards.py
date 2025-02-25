from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

contact = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Отправить контакт', request_contact=True)]
], resize_keyboard=True, input_field_placeholder='Нажмите кнопку ниже')


main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Записаться на услугу')],
    [KeyboardButton(text='Контакты/локация')]
], resize_keyboard=True)