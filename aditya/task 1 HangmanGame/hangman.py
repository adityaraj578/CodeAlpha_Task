import random

# Step 1: Predefined list of words
word_list = ["apple", "brain", "plant", "house", "table"]

# Step 2: Choose a random word
secret_word = random.choice(word_list)
guessed_letters = []
attempts_left = 6

# Step 3: Game introduction
print("🎉 Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print(f"You have {attempts_left} incorrect guesses allowed.")

# Step 4: Main game loop
while attempts_left > 0:
    # Display current progress
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("\nWord:", display_word.strip())

    # Check if word is completely guessed
    if all(letter in guessed_letters for letter in secret_word):
        print("🎉 Congratulations! You guessed the word:", secret_word)
        break

    # Player input
    guess = input("Guess a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("❗ Please enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check guess
    if guess in secret_word:
        print("✅ Good guess!")
    else:
        attempts_left -= 1
        print(f"❌ Wrong guess! Attempts left: {attempts_left}")

# Step 5: Game over
if attempts_left == 0:
    print("\n💀 Game over! The word was:", secret_word)
