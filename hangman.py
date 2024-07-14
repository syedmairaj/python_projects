import random

# Dictionary of genres with corresponding word lists
genres = {
    "animals": ["dog", "cat", "elephant", "giraffe", "rabbit", "monkey", "lion"],
    "countries": ["canada", "brazil", "india", "china", "france", "japan", "russia"],
    "colors": ["red", "blue", "green", "yellow", "purple", "orange", "black", "white"]
}

def choose_word(genre):
    """Choose a random word from the selected genre"""
    word_list = genres.get(genre)
    if word_list:
        return random.choice(word_list)
    else:
        return None

def display_word(word, guessed_letters):
    """Display the word with guessed letters and placeholders"""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def hangman():
    print("Welcome to Hangman!")
    print("Choose a genre:")
    for genre in genres.keys():
        print("- " + genre.capitalize())

    genre_choice = input("Enter the genre you want to play: ").lower()

    # Check if genre choice is valid
    while genre_choice not in genres.keys():
        print("Invalid genre. Please choose from the available genres.")
        genre_choice = input("Enter the genre you want to play: ").lower()

    secret_word = choose_word(genre_choice)
    if not secret_word:
        print("Error: Could not find word for selected genre.")
        return

    guessed_letters = []
    attempts_left = 6 

    while True:
        print("\nAttempts left:", attempts_left)
        print(display_word(secret_word, guessed_letters))

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            attempts_left -= 1
            print("Incorrect!")

        if "_" not in display_word(secret_word, guessed_letters):
            print("\nCongratulations! You guessed the word:", secret_word)
            break

        if attempts_left == 0:
            print("\nGame over! The word was:", secret_word)
            break

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        hangman()
    else:
        print("Thank you for playing!")

# Start the game
hangman()
