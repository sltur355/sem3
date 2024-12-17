import requests
import datetime
from config import tg_bot_token, open_weather_token
import telebot

bot = telebot.TeleBot(tg_bot_token)

@bot.message_handler(commands=["start"])
def start_command(message):
    bot.reply_to(message, "Привет! Напиши мне название города и я расскажу тебе о погоде!")

@bot.message_handler(func=lambda message: True)
def get_weather(message):
    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"
    }

    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric"
        )
        data = r.json()

        if data.get("cod") != 200:
            bot.reply_to(message, "\U00002620 Проверьте название города \U00002620")
            return

        city = data["name"]
        cur_weather = data["main"]["temp"]

        weather_description = data["weather"][0]["main"]
        wd = code_to_smile.get(weather_description, "Посмотри в окно, не пойму что там за погода!")

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = sunset_timestamp - sunrise_timestamp

        bot.reply_to(message, f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
                              f"Погода в городе: {city}\nТемпература: {cur_weather}C° {wd}\n"
                              f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/с\n"
                              f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\n"
                              f"Продолжительность дня: {length_of_the_day}\n"
                              f"***Хорошего дня!***"
                              )

    except Exception as e:
        bot.reply_to(message, "U00002620 Произошла ошибка, попробуйте еще раз. U00002620")

if __name__ == '__main__':
    bot.polling(none_stop=True, timeout=30)