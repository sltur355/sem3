import requests
from pprint import pprint
from config import open_weather_token
import datetime

def get_weather(city, open_weather_token):

    code_to_smile = {
        'Clear': 'Ясно \U00002600',
        'Clouds': 'Облачно \U00002601',
        'Rain': "Дождь \U00002614",
        'Drizzle': 'Дождь \U00002614',
        'Thunderstorm': "Гроза \U000026A1",
        'Snow': "Снег \U0001F328",
        'Mist': "Туман \U0001F32B"
    }
    try:
        r=requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data=r.json()
        pprint(data)

        city= data["name"]                 #город
        cur_weather= data["main"]["temp"] #погода в градусах
        weather_description=data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd=code_to_smile[weather_description]
        else:
            wd= "Что у тебя там за окном? Понять не могу.."
        humidity= data['main']['humidity'] #влажность
        pressure = data["main"]["pressure"]  #давление
        wind=data['wind']['speed']
        sunrise_timestamp= datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_timestamp=datetime.datetime.fromtimestamp(data['sys']['sunset'])
        print(f"---{datetime.datetime.now().strftime('%d.%m.%Y %H:%M')}---\n"
            f"Погода в городе: {city}\nТемпература: {cur_weather} С° {wd}\n"
              f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст.\nВетер: {wind} м/с\n"
              f"Восход солнца: {sunrise_timestamp}\nЗакат cолнца: {sunset_timestamp}\nХорошего дня!"
              )

    except Exception as ex:
        print(ex)
        print("Проверьте название города")



def main():
    city=input("Введите город: ")
    get_weather(city, open_weather_token)

if __name__ == "__main__":
    main()