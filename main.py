from flask import Flask, render_template, request, redirect, url_for
import sqlite3, os, uuid
import requests

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

def drafts():
    return render_template('drafts.html')

@app.route('/plans')
def plans():
    return render_template('plans.html')

if __name__ == '__main__':
    app.run(debug=True)
