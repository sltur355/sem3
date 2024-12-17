import telebot
from telebot import types
from database import init_db, get_value, update_value, add_to_history, get_history

# Инициализация базы данных
init_db()


tg_bot_token = '7949443626:AAEJXtUyaWbcWkNQgxv1QxoO9MuM28Z_ERc'
bot = telebot.TeleBot(tg_bot_token)


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.reply_to(message, "Добро пожаловать! Используйте кнопки ниже для управления общим числом.")
    show_buttons(message.chat.id)


def show_buttons(chat_id):
    markup = types.InlineKeyboardMarkup()
    increase_button = types.InlineKeyboardButton("Увеличить на 2", callback_data='increase')
    decrease_button = types.InlineKeyboardButton("Уменьшить на 2", callback_data='decrease')
    history_button = types.InlineKeyboardButton("Показать историю", callback_data='history')

    markup.add(increase_button, decrease_button, history_button)

    bot.send_message(chat_id, f"Текущее число: {get_value()}", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    if call.data == 'increase':
        new_value = get_value() + 2
        update_value(new_value)
        add_to_history(call.from_user.id, 'increase')
        bot.answer_callback_query(call.id, "Число увеличено на 2.")

    elif call.data == 'decrease':
        new_value = get_value() - 2
        update_value(new_value)
        add_to_history(call.from_user.id, 'decrease')
        bot.answer_callback_query(call.id, "Число уменьшено на 2.")

    elif call.data == 'history':
        history = get_history()
        history_message = "История команд:\n"
        for user_id, command in history:
            history_message += f"Пользователь {user_id}: {command}\n"

        bot.send_message(call.message.chat.id, history_message)

    show_buttons(call.message.chat.id)


if __name__ == '__main__':
    bot.polling(none_stop=True)
