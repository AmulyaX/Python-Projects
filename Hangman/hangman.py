import random
import hangman_words
import hangman_art

end_of_game = False
chosen_word = random.choice(hangman_words.word_list)
len_chosen_word = len(chosen_word)

lives = 6
lives_used = 0

print(hangman_art.logo)

display = []
for letter in chosen_word:
    display.append("_")

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print("You have already guessed this letter:", guess)

    found_guess = False

    for position in range(len_chosen_word):
        letter = chosen_word[position]
        if letter == guess:
            found_guess = True
            display[position] = letter

    if not found_guess:
        print(f"Letter chosen by you '{guess}' is not in the word.")
        lives_used += 1
        if lives_used == lives:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")
    print("Lives Remaining: ", lives - lives_used)
    print(hangman_art.stages[lives_used])