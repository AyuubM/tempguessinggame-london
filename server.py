from flask import Flask, render_template, request
import pandas
import random

app = Flask(__name__)

df = pandas.read_csv("london_temp.csv")
random_entry = random.randint(0, 389976)
random_year_info = df.loc[random_entry]
random_year_time = random_year_info["dt_iso"]
random_year_temp = random_year_info["temp"]
random_year = random_year_time[0:11]
random_time = random_year_time[11:20]

@app.route('/')
def home():
    return render_template("index.html", random_year=random_year, random_time=random_time)

@app.route('/', methods=['POST'])
def guess_temp():
    guess = request.form['user_guess']
    type_guess = round(int(guess))
    if request.method == "POST":
        with open("guesses.txt", "a") as g:
            g.write(f"User guessed: {guess}, the actual temperature was {round(random_year_temp)}\n")
    if type_guess == round(random_year_temp):
        return render_template("results.html", guess=guess, random_year_time_temp=round(random_year_temp))
    else:
        return render_template("incorrect.html", guess=guess, random_year_time_temp=round(random_year_temp))


if __name__ == "__main__":
    app.run(debug=True)