from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/artsfirst')
def artsfirst():
    return render_template("artsfirst.html")

@app.route('/board')
def board():
    return render_template("board.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/eastside')
def eastside():
    return render_template("eastside.html")

@app.route('/openmic')
def openmic():
    return render_template("openmic.html")

@app.route('/productions')
def productions():
    return render_template("productions.html")

@app.route('/spotlight')
def spotlight():
    return render_template("spotlight.html")

@app.route('/eastside-character-description')
def characters():
    return render_template("characters.html")