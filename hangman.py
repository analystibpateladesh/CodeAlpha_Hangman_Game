import random

def hangman():
    words = ["python", "programming", "hangman", "developer", "internship", "project", "challenge", "codealpha"]

    word_to_guess = random.choice(words).lower()
    guessed_word = ["_" for _ in word_to_guess]
    guessed_letters = set()
    max_attempts = 6
    attempts_left = max_attempts

    print("\nWelcome to Hangman! Let's start the game.")
    print(f"The word has {len(word_to_guess)} letters: {' '.join(guessed_word)}")

    while attempts_left > 0 and "_" in guessed_word:
        print(f"\nAttempts left: {attempts_left}")
        print("Guessed so far: ", " ".join(guessed_word))
        guess = input("Guess a letter: ").lower()

        if not guess.strip():
            print("Please enter a letter.")
            continue

        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Please enter a single alphabetical character.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.add(guess)

        if guess in word_to_guess:
            print(f"Good job! '{guess}' is in the word.")
            for i, letter in enumerate(word_to_guess):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            attempts_left -= 1
            print(f"Oops! '{guess}' is not in the word.")

    if "_" not in guessed_word:
        print(f"\nCongratulations! You guessed the word '{word_to_guess}' correctly!")
    else:
        print(f"\nGame over! The word was '{word_to_guess}'. Better luck next time.")

if __name__ == "__main__":
    hangman()
