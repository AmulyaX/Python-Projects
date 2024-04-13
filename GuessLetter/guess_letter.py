import random

word_list = ["random", "weird", "list"]

chosen_word = random.choice(word_list)

while True:
    guess = (input("Guess a letter: ")).lower()
    if len(guess) > 1:
        print("ERROR: Please enter only one character! Try again: ")
    else:
        print("You entered:", guess)
        break

isFound = False
for word in word_list:
    for letter in word:
        if letter == guess:
            isFound = True
            break

if isFound:
    print("You guessed it! YAY")
else:
    print("Sorry, you couldn't guess it!")