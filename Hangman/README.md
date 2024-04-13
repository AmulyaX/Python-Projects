## Hangman Game

This classic Hangman game, written in Python, challenges you to guess the secret word letter by letter before you run out of lives! 

**Features:**

- **Randomly chosen words:** The game keeps it exciting by selecting a secret word from a built-in list.
- **Visual hangman stages:** Witness the hangman come to life (or lose his life) as you make incorrect guesses.
- **User-friendly interface:** Clear messages guide you through the game and update you on your progress.

**How to Play:**

1. **Run the Script:**
   - Ensure you have Python 3 installed.
   - Navigate to the directory containing the game files (`hangman.py`, `hangman_words.py`, and `hangman_art.py`).
   - Run the script using the following command:

     ```bash
     python hangman.py
     ```

2. **Guessing Letters:**
   - The game will display the hangman and a series of underscores representing the secret word.
   - Enter a lowercase letter (e.g., "a", "b", "c") as your guess and press enter.

3. **Revealing Letters:**
   - The program will check your guess. If the letter exists in the secret word, it will be revealed in the corresponding positions.

4. **Losing Lives:**
   - If your guess is incorrect, you'll lose a life, and the hangman will progress towards his demise. The number of remaining lives will be displayed.

5. **Winning or Losing:**
   - **Win:** You win the game by correctly guessing all the letters in the secret word before running out of lives.
   - **Lose:** You lose the game if you exhaust all your lives by guessing incorrect letters.

**Happy Guessing!**
