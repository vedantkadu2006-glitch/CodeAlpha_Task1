import random
# List of words
words = ["python", "computer", "school", "programming", "science"]
# Randomly select a word
word = random.choice(words)
guessed_letters = []
attempts = 6
print("=== Welcome to Hangman ===")
while attempts > 0:
    display_word = ""

    # Display guessed letters and underscores
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if word is completely guessed
    if "_" not in display_word:
        print("Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct Guess!")
    else:
        attempts -= 1
        print("Wrong Guess!")
        print("Attempts Left:", attempts)

# If player loses
if attempts == 0:
    print("\nGame Over!")
    print("The word was:", word)