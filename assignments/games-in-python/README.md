# 📘 Assignment: Games in Python - Hangman

## 🎯 Objective

Build a playable Hangman game in Python using loops, conditionals, strings, and user input. By the end of this assignment, you will practice managing game state and implementing clear game rules.

## 📝 Tasks

### 🛠️ Hangman Game Setup

#### Description
Create the basic game structure for Hangman. Define a list of possible words, select one word for the current game, and show the hidden word as underscores.

#### Requirements
Completed program should:

- Store at least 5 possible words in a list.
- Select one word for the current round.
- Display the hidden word using underscores separated by spaces (for example: `_ _ _ _`).
- Set a fixed number of incorrect guesses allowed.

### 🛠️ Gameplay Loop and Win/Lose Conditions

#### Description
Implement the interactive game loop where the player enters one letter at a time. Update the displayed word when guesses are correct, reduce remaining attempts when guesses are incorrect, and end the game with a clear result message.

#### Requirements
Completed program should:

- Accept one-letter guesses from the player.
- Reveal correctly guessed letters in all matching positions.
- Track and display the number of incorrect guesses remaining.
- End with a win message when the full word is revealed.
- End with a lose message when attempts reach zero and display the correct word.
