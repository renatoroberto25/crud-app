from flask import Flask, render_template
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy

#My App
app =  Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)

@app.route("/healtcheck")
def healtcheck():
    return render_template("healtcheck.html")

@app.route("/")
def index():
    return render_template("index.html") 


if __name__ in "__main__":
    app.run(debug=True)