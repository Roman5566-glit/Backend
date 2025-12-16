from flask import Flask, render_template, request, redirect, url_for
import sqlite3, os, uuid
import requests
from typing import ClassVar
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






# EMAIL CONFIGURATION
SENDER_EMAIL: ClassVar[str] = 'someadress@gmail.com' # почта отправителя
SENDER_PASSWORD: ClassVar[str] = 'YOUR_SEC_PASSWORD'  # пароль приложения или обычный пароль от почты
RECEIVER_EMAIL: ClassVar[str] = 'receiverADRESS@example.com'  # почта получателя



#a class for sending username or phone_number to receiver email
class Email_receive:



    SENDER_EMAIL = SENDER_EMAIL
    SENDER_PASSWORD = SENDER_PASSWORD
    RECEIVER_EMAIL = RECEIVER_EMAIL



    # a function for logic of the class
    @staticmethod
    def send_data_to_email(username: str) -> bool:



        if not username:
            # checking if username is empty
            print("Ошибка: юзернэйм не может быть пустым")
            return False

        # preparing email content
        subject = f"Новая регистрация: {username}"
        contents = [
            f"<h2> Новые данные с сайта<h2>",
            f'<p style="font-size: 18px;">@{username}</p>',
            # some other info can be added here if needed
        ]
        


        try:
            # retrieving yagmail.SMTP object
            yag = yagmail.SMTP(
                user=Email_receive.SENDER_EMAIL, 
                password=Email_receive.SENDER_PASSWORD
            )
            
            # sending the email
            yag.send(
                to=Email_receive.RECEIVER_EMAIL,
                subject=subject,
                contents=contents,
            )
            
            # return success status
            print(f"Сообщение о юзернейме '{username}' успешно отправлено.")
            return True

        except Exception as e:
            # return failure status
            print(f"Ошибка при отправке почты: {e}")
            return False
        





if __name__ == '__main__':
    app.run(debug=True)