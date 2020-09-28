# python main.py
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)