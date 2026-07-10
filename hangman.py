import random

# Hangman stages
HANGMAN_PICS = [
'''
  +---+
  |   |
      |
      |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
'''
]

# List of words
words = [
    "python", "computer", "program", "keyboard", "internet",
    "developer", "hangman", "science", "network", "college"
]

# Select random word
word = random.choice(words).upper()

guessed_letters = []
wrong_guesses = 0
max_wrong = len(HANGMAN_PICS) - 1

print("=" * 35)
print("        HANGMAN GAME")
print("=" * 35)

while True:
    print(HANGMAN_PICS[wrong_guesses])

    # Display guessed word
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("Word:", display)
    print("Wrong guesses left:", max_wrong - wrong_guesses)

    # Win check
    if "_" not in display:
        print("\n🎉 Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").upper()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct!\n")
    else:
        print("Wrong!\n")
        wrong_guesses += 1

    if wrong_guesses == max_wrong:
        print(HANGMAN_PICS[wrong_guesses])
        print("Game Over!")
        print("The correct word was:", word)
        break