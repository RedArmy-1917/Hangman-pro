import tkinter as tk
from core import HangmanCore

game = HangmanCore()

def update_ui():
    word_label.config(text=" ".join(game.display))
    lives_label.config(text=f"Lives: {game.lives}")

def guess_letter():
    letter = entry.get().lower()
    entry.delete(0, tk.END)

    result = game.guess(letter)

    if result == "already":
        status_label.config(text="Already guessed!")
    elif result == "correct":
        status_label.config(text="Correct!")
    else:
        status_label.config(text="Wrong!")

    update_ui()

    if game.is_won():
        status_label.config(text="You Won! 🎉")
    elif game.is_lost():
        status_label.config(text=f"You Lost 💀 Word: {game.word}")

root = tk.Tk()
root.title("Hangman Pro GUI")

word_label = tk.Label(root, text=" ".join(game.display), font=("Arial", 20))
word_label.pack()

lives_label = tk.Label(root, text=f"Lives: {game.lives}")
lives_label.pack()

entry = tk.Entry(root)
entry.pack()

btn = tk.Button(root, text="Guess", command=guess_letter)
btn.pack()

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()