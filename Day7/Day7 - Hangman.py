import random 
from hangman_words_list import word_list

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
the_word = random.choice(word_list)
number_of_letters = len(the_word) 
list_of_letters = list(the_word)
print(list_of_letters)

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

display = []
for i in range(number_of_letters): 
    display.append("_")
print(display)
status = "Lose"

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

for i in range(6): 
    guess = input("Guess a letter: ").lower()
    for i in range(number_of_letters): 
        if list_of_letters[i] == guess: 
            display[i] = guess 
    print(display)
    if display[i] != "_": 
        status = "Win"
        break
print(status)