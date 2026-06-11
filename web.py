from flask import Flask, render_template, request, redirect, session
from core import HangmanCore

app = Flask(__name__)
app.secret_key = "secret"

game = HangmanCore()

@app.route("/", methods=["GET", "POST"])
def index():
    global game

    if request.method == "POST":
        letter = request.form.get("letter", "").lower()

        if letter:
            game.guess(letter)

    return render_template(
        "index.html",
        word=" ".join(game.display),
        lives=game.lives
    )

if __name__ == "__main__":
    app.run(debug=True)