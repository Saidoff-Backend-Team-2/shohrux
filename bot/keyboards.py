from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from django.conf import settings

def get_languages():
    keyboard = InlineKeyboardMarkup(row_width=2)
    uz_keyboard = InlineKeyboardButton(text="Uz", callback_data="lang_uz")
    ru_keyboard = InlineKeyboardButton(text="Ru", callback_data="lang_ru")
    keyboard.add(uz_keyboard, ru_keyboard)
    return keyboard