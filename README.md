# Hangman application
## Description:
This application is written in Python where a json file is parsed and a random word is chosen from the json. The user then guesses letters that the word contains and if the user can't guess the word within n-number of times will the user loose.

## Code explanation
Create a class called `Hangman()`. in `__init__` read the json file with the words and initiate serveral things including a random integer generator which choses a word at random from the json file with words in the method `get_rnd_word()`. 
 
Method `print_hidden_word()` prints out the attribute `.hidden_word` which is initialized from the json list of words together with the method `get_rnd_word()` and the `hidden_word()` method. The method `hidden_word()` uses the attribute `.split` and loops all characters from the word into a list attribute using listcomprension.

The method `update_hidden_word()` takes an input argument. This input is then checked if the character is in the random word that has been generated. If the character exists in the word will the index of where it is be saved and then looped into `.hidden_word` in the correct place, this also works for more than one occurance of the character. `update_hidden_word()` also calls the method `check_word()` after `.hidden_word` has been updated. In the `check_word()` and `check_count()` methods they check if the attribute `.hidden_word` is equal to the attribute `.word` and that the count limit not has been reached.

