# from tkinter import *
# import requests
#
# def get_weather():
#     city = cityField.get().strip()
#     if not city:
#         info['text'] = 'Введите город!'
#         return
#
#     key = '3b971be31c6f4aa3963571abec37995d'
#     url = 'http://api.openweathermap.org/data/2.5/weather'
#     params = {'APPID': key, 'q': city, 'units': 'metric'}
#
#     try:
#         result = requests.get(url, params=params, timeout=5)
#         weather = result.json()
#
#
#         print("Ответ сервера:", weather)
#
#         if weather.get('cod') != 200:
#             code = weather.get('cod')
#             msg = weather.get('message', '')
#
#             if 'http' in msg:
#                 msg = 'Неверный API-ключ (проверьте активацию)'
#             info['text'] = f'Ошибка {code}: {msg}'
#             return
#
#         city_name = weather['name']
#         temp = weather['main']['temp']
#         info['text'] = f'{city_name}: {temp}°C'
#
#     except requests.exceptions.RequestException:
#         info['text'] = 'Ошибка соединения с сервером'
#     except Exception as e:
#         info['text'] = f'Ошибка: {e}'
#
#
# root = Tk()
# root['bg'] = '#fafafa'
# root.title('Погодное приложение')
# root.geometry('300x250')
# root.resizable(width=False, height=False)
#
# frame_top = Frame(root, bg='#ffb700', bd=5)
# frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.25)
#
# cityField = Entry(frame_top, bg='white', font=30)
# cityField.pack()
#
# btn = Button(frame_top, text='Посмотреть погоду', command=get_weather)
# btn.pack()
#
# frame_bottom = Frame(root, bg='#ffb700', bd=5)
# frame_bottom.place(relx=0.15, rely=0.55, relwidth=0.7, relheight=0.1)
#
# info = Label(frame_bottom, text='Погода в городе', bg='#ffb700', font=40)
# info.pack()
#
#2
import tkinter as tk
from tkinter import messagebox
import wikipediaapi
wiki_wiki = wikipediaapi.Wikipedia(
    language='ru',
    user_agent='MyCityFactsApp/1.0 (myemail@example.com)'
)

def get_city_facts():
    city = city_entry.get().strip()
    if not city:
        messagebox.showwarning("Ошибка", "Введите название города")
        return

    try:
        page = wiki_wiki.page(city)
        if not page.exists():
            info_label.config(text="Город '" + city + "' не найден в Wikipedia")
            return


        text = page.text
        sentences = text.split('. ')
        keywords = [
            'достопримечательность', 'музей', 'собор', 'крепость', 'парк',
            'памятник', 'театр', 'дворец', 'основан', 'известен'
        ]
        facts = []
        for sentence in sentences:
            for keyword in keywords:
                if keyword.lower() in sentence.lower():
                    if not sentence.endswith('.'):
                        sentence += '.'
                    facts.append(sentence.strip())
                    break
            if len(facts) >= 2:
                break

        if len(facts) < 2:

            facts = sentences[:2]


        result_text = city + ":\n\n"
        for i, fact in enumerate(facts[:2], 1):
            result_text += str(i) + ". " + fact + "\n\n"

        info_label.config(text=result_text)

    except Exception as e:
        messagebox.showerror("Ошибка", "Произошла ошибка:\n" + str(e))



root = tk.Tk()
root.title('Исторические факты о городе')
root.geometry('600x400')
root.resizable(width=False, height=True)
root.configure(bg='#f0f4f8')


title_label = tk.Label(
    root,
    text='Исторические факты о городе',
    font=('Arial', 16, 'bold'),
    bg='#f0f4f8',
    fg='#2c3e50'
)
title_label.pack(pady=15)


input_frame = tk.Frame(root, bg='#f0f4f8')
input_frame.pack(pady=10)

city_entry = tk.Entry(
    input_frame,
    width=30,
    font=('Arial', 12),
    relief=tk.GROOVE,
    bd=2
)
city_entry.pack(side=tk.LEFT, padx=5)

search_btn = tk.Button(
    input_frame,
    text='Найти факты',
    command=get_city_facts,
    font=('Arial', 12),
    bg='#4a90e2',
    fg='white',
    relief=tk.RAISED,
    bd=3,
    padx=15,
    pady=5
)
search_btn.pack(side=tk.LEFT, padx=5)


result_frame = tk.Frame(root, bg='white', relief=tk.GROOVE, bd=2)
result_frame.pack(pady=15, padx=20, fill=tk.BOTH, expand=True)

info_label = tk.Label(
    result_frame,
    text='Введите город и нажмите "Найти факты"',
    font=('Arial', 11),
    bg='white',
    fg='#555',
    justify=tk.LEFT,
    wraplength=550,
    anchor='nw'
)
info_label.pack(pady=15, padx=15, fill=tk.BOTH, expand=True)


hint_label = tk.Label(
    root,
    text='Примеры: Москва, Санкт-Петербург, Париж, Лондон, Рим',
    font=('Arial', 9),
    bg='#f0f4f8',
    fg='#888'
)
hint_label.pack(pady=5)

root.mainloop()