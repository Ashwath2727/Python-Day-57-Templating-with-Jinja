import datetime
import random

from age_calculator import AgeCalculator
from blogs import Blogs
from gender import Gender

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    my_name = "Ashwath"
    return render_template("index.html", num=random_number, year=current_year, name=my_name)


@app.route("/guess/<name>")
def guess(name):
    gender = Gender(name)
    gender_reveal = gender.get_gender()

    age_calculator = AgeCalculator(gender_reveal)
    age = age_calculator.get_age()

    return render_template("guess.html", name=name.title(), gender=gender_reveal, age=age)

@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blogs = Blogs()
    all_posts = blogs.get_posts()

    return render_template("blog.html", posts=all_posts)


if __name__ == '__main__':
    app.run(debug=True)