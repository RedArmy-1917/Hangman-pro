import random

class HangmanCore:
    def __init__(self):
        self.words = ["python", "database", "network", "algorithm", "germany"]
        self.reset()

    def reset(self):
        self.word = random.choice(self.words)
        self.guessed = set()
        self.lives = 6
        self.display = ["_"] * len(self.word)

    def guess(self, letter):
        if letter in self.guessed:
            return "already"

        self.guessed.add(letter)

        if letter in self.word:
            for i, ch in enumerate(self.word):
                if ch == letter:
                    self.display[i] = letter
            return "correct"
        else:
            self.lives -= 1
            return "wrong"

    def is_won(self):
        return "_" not in self.display

    def is_lost(self):
        return self.lives <= 0