import numpy as np
import pandas as pd

class Hangman():
    def __init__(self):
        self.json = pd.read_json("data/word.json")
        self.rnd = np.random.randint(low = 0, high = 99)
        self.word = pd.DataFrame()
        self.correct_word = list()

    def get_rnd_word(self):
        self.word = self.json["word"].iloc[self.rnd]
        self.split = [char for char in self.word]
    
    def hidden_word(self):
        self.hidden_word = "_ "*len(self.split)

    def print_hidden_word(self):
        print("The word is: " + self.hidden_word)
        


        


hangman = Hangman()
hangman.get_rnd_word()
hangman.hidden_word()
hangman.print_hidden_word()

