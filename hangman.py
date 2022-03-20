import re
import numpy as np
import pandas as pd

class Hangman():
    def __init__(self):
        self.json = pd.read_json("data/word.json")
        self.rnd = np.random.randint(low = 0, high = 99)
        self.word = pd.DataFrame()
        self.count = 0

    def get_rnd_word(self):
        self.word = self.json["word"].iloc[self.rnd]
        self.split = [char for char in self.word]
    
    def hidden_word(self):
        self.hidden_word = "_"*len(self.split)
        self.hidden_word = [char for char in self.hidden_word]

    def print_hidden_word(self):
        print("The word is: ", "".join(self.hidden_word))
    
    def update_hidden_word(self, inp):
        inp = inp.lower()
        if len(inp) == 1:
            if inp in self.word:
                self.idx = [_.start() for _ in re.finditer(inp, self.word)]
                if len(self.idx) > 1:
                    for idx in self.idx:
                        self.hidden_word[idx] = inp
                    self.print_hidden_word()
                else:
                    self.hidden_word[self.idx[0]] = inp
                    self.print_hidden_word()
            else:
                self.count = self.count + 1
        else:
            print("Guess one character a-z")

        if inp.lower() not in self.word:
            print(f"{inp} is not in the word")
        self.check_word()
        self.check_count()

    def check_word(self):
        if "".join(self.hidden_word) == self.word:
            print("YOU WON!")
    def check_count(self):
        if self.count == 5:
            print("YOU LOST! the word was: ", self.word)

print("\n")
print("This is Hang-man!")
print("You are supposed to guess the letter in the word")
print("if you can't make it will the man hang! :)\n")
hangman = Hangman()
hangman.get_rnd_word()
hangman.hidden_word()
hangman.print_hidden_word()

while hangman.count < 5 and "".join(hangman.hidden_word) != hangman.word:
    inp = input()
    hangman.update_hidden_word(inp)
    print("\n")