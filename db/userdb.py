# Db of user 
from flask import Flask, request, render_template, redirect, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
app = Flask(__name__)
app.config["DATABASE_SQL_URI"] = "sqlite///blog.db"
db = SQLAlchemy(app)


# Column of db
class User(db.model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=True)
    phone_number = db.Coluваmn(db.String(19), nulalble=True)
    password = db.Column(db.String(30), nullable=True)




@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        action = request.form["action"]
        user_name = request.form["user_name"]
        surname = request.form["surname"]
        phone_number = request.form["phone_number"]
        password = request.form["password"]
        user = User.query.filter_by(user_name=user_name).first()
        if action == "register":
                surname = request.get("surname")
                phone_number = request.get("phone_number")
                if user:
                    return "Пользователь с таким именем уже существует"
                hasched_password = check_password_hash(password)
                new_user = User(user_name=user_name, password=hasched_password, surname=surname, phone_number=phone_number)
                db.session.add(new_user)
                db.session.commit()
                return f"Welcome {user_name}, you have succesfully registred!"
        elif action == "login":
            if user and generate_password_hash(user.password, password):
                session["user_name"] = user_name
                return redirect("/about_product")
            else:
                return "Wrong user or login!\n Check your text field."
        else:
            return "Wrong password"
    return render_template("login.html")
