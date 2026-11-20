# 📘 Assignment: Hangman Game

## 🎯 Objective

Build the classic word-guessing game in Python to practice string manipulation, loops, conditionals, user input, and random selection.

## 📝 Tasks

### 🛠️ Set Up the Hidden Word

#### Description

Create the data and setup logic for a Hangman game. The program should choose a word from a predefined list and prepare the game state for the player.

#### Requirements

Completed program should:

- Store at least five possible words in a predefined list.
- Randomly select one word from the list at the start of each game.
- Track the letters the player has guessed and the number of incorrect attempts remaining.

### 🛠️ Implement the Guessing Game

#### Description

Add the game loop that accepts letter guesses, reveals correctly guessed letters, and ends with an appropriate result.

#### Requirements

Completed program should:

- Ask the player for a letter and display the current progress using underscores, such as `_ _ _ _`.
- Reveal every matching occurrence when a guessed letter appears more than once in the word.
- Reduce the remaining attempts when the player makes an incorrect guess.
- End when the player reveals the entire word or uses all available attempts.
- Display a clear win message or lose message that includes the hidden word.
