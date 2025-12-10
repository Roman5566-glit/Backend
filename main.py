from flask import Flask, render_template, request, redirect, url_for
import sqlite3, os, uuid
import requests
# import yagmail

app = Flask(__name__)

# Главная
@app.route('/')
def home():
    return render_template('about_product.html')

# Страницы
@app.route('/about_product')
def about_product():
    return render_template('about_product.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/drafts')
def drafts():
    return render_template('drafts.html')

@app.route('/plans')
def plans():
    return render_template('plans.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')



#почта отправителя
SENDER_EMAIL = ""

SENDER_PASSWORD = os.environ.get('' , 'пароль приложения для теста')

#почта получителя
RECEIVER_EMAIL = "bott76392@gmai.com"


#класс для получения юзернэйма или номера телефона (в зависимости от того что захотят отправить) на почту получителя
class Email_receive():
    def send_data_to_email(username: str) -> bool:
        if not username:
            print("Ошибка: юзернэйм не может быть пустым")
            return False
    subject = f"Новая регистрация: {username}"
    contents = [
        f"<h2> Новые данные с сайта<h2>",
        f"<p>Получен новый юзернейм</p>",
        f'<p style="font-size: 18px; color: #d9534f; font-weight: bold;">@{username}</p>',
        '<hr>',
        '<small>Отправлено с помощью Python и yagmail</small>'
    ]
    
        





if __name__ == '__main__':
    app.run(debug=True)
