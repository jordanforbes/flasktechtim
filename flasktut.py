from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>HELLO</h1> <a href=\'/ShonenFlop\'>Shonen Flop</a>"

@app.route("/ShonenFlop")
def shonenFlop():
    return redirect("https://shonenflop.com")

@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

@app.route("/backhome") #redirects home
def backHome():
    return redirect(url_for("home")) #name of method not name of route

@app.route("/admin/")
def admin():
    return redirect(url_for("user",name="Admin"))

if __name__== '__main__':
    app.run()