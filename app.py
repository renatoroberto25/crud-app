from flask import Flask, render_template
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy

#My App
app =  Flask(__name__)

@app.route("/healtcheck")
def index():
    return render_template("healtcheck.html")

if __name__ in "__main__":
    app.run(debug=True)

