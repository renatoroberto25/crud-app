from flask import Flask
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy

#My App
app =  Flask(__name__)

@app.route("/healthcheck")
def index():
    return "Site OK!"

if __name__ in "__main__":
    app.run(debug=True)

