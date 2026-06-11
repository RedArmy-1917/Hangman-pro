import random

class HangmanCore:
    def __init__(self, category="Animals", difficulty="Medium"):
        self.words = {
            "Animals": ["lion", "tiger", "elephant", "dog", "cat"],
            "Programming": ["python", "flask", "algorithm", "database"],
            "Countries": ["germany", "france", "canada", "japan"]
        }

        self.difficulty_map = {
            "Easy": 8,
            "Medium": 6,
            "Hard": 4
        }

        self.category = category
        self.difficulty = difficulty
        self.reset()

    def reset(self):
        self.word = random.choice(self.words[self.category])
        self.guessed = set()
        self.lives = self.difficulty_map[self.difficulty]
        self.display = ["_"] * len(self.word)
        self.history = []

    def guess(self, letter):
        if letter in self.guessed:
            return "already"

        self.guessed.add(letter)
        self.history.append(letter)

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