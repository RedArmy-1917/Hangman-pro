import os
from flask import Flask, render_template, request, redirect
from core import HangmanCore

app = Flask(__name__)
app.secret_key = "secret"

game = HangmanCore()

@app.route("/", methods=["GET", "POST"])
def index():
    global game

    if request.method == "POST":
        letter = request.form.get("letter", "").lower()
        category = request.form.get("category")
        difficulty = request.form.get("difficulty")

        if category and difficulty:
            game = HangmanCore(category, difficulty)

        if letter:
            game.guess(letter)

    return render_template(
        "index.html",
        word=" ".join(game.display),
        lives=game.lives,
        history=game.history,
        won=game.is_won(),
        lost=game.is_lost()
    )

@app.route("/new_game", methods=["POST"])
def new_game():
    global game
    game = HangmanCore()
    return redirect("/")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)