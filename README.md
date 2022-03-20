# Hangman application
## Description:
This application is written in Python where a json file is parsed and a random word is chosen from the json. The user then guesses letters that the word contains and if the user can't guess the word within n-number of times will the user loose.

## Code
Create a class called `Hangman()`. in `__init__` read the json file with the words and initiate serveral things including a random integer generator which choses a word at random from the json file with words in the method `get_rnd_word()`. 

Create a method `print_hidden_word()` which prints out something like the following:
```
The word is: __
```
for the word `is` 
