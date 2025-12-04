import datetime
import random

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    my_name = "Ashwath"
    return render_template("index.html", num=random_number, year=current_year, name=my_name)

if __name__ == '__main__':
    app.run(debug=True)