from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    user = {"name": "Alejandra", "grade": "10"}
    return render_template("index.html", user = user, title = "Homepage")

@app.route('/secret')
def secret():
    return render_template("secret.html")

    
@app.route("/sendBreakfast", methods = ["GET", "POST"])
def breakfast():
    if request.method == "GET":
        return "Please use the form."
    else:
        userdata = dict(request.form)
        print(userdata)
        nickname = userdata["nickname"]
        breakfast = userdata["breakfast"]
        breakfast = model.shout(breakfast)
        return render_template("breakfast.html", nickname = nickname, breakfast = breakfast)