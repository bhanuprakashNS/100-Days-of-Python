# .............................. Jinja in Flask ................................ #
# ............. Created and modified by N.S.Bhanuprakash on 17-05-2022 .....#

from flask import Flask, render_template
from random import randint
import datetime as dt
import requests

app = Flask(__name__)
age_url = "https://api.agify.io?name="
gender_url = "https://api.genderize.io?name="
blog_url = "https://api.npoint.io/c790b4d5cab58020d391"


@app.route("/")
def hello():
    random_number = randint(1, 10)
    year = dt.date.today().year
    return render_template("/index.html", num=random_number, year=year)


@app.route("/guess/<name>")
def age_gender(name):
    age_response = requests.get(url=f"{age_url}{name}")
    age = age_response.json()["age"]
    gender_response = requests.get(url=f"{gender_url}{name}")
    gender = gender_response.json()["gender"]
    return render_template("/index.html", person_name=name, person_age=age, person_gender=gender)


@app.route("/blog")
def blog():
    blog_response = requests.get(url=blog_url)
    blog_data = blog_response.json()
    return render_template("/blog.html", all_posts=blog_data)


if __name__ == "__main__":
    app.run(debug=True)
