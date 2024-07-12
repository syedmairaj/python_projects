import random

def number_guesser(difficulty):
    if difficulty == "normal":
        print("You have chosen normal difficulty. Guess a number between 1 and 10.")
        number_to_guess = random.randint(1, 10)
        chances = 5
    elif difficulty == "hard":
        print("You have chosen hard difficulty. Guess a number between 1 and 20.")
        number_to_guess = random.randint(1, 20)
        chances = 3
    else:
        print("Invalid difficulty level. Please choose 'normal' or 'hard'.")
        return
    
    while chances > 0:
        print(f"You have {chances} chances left.")
        guess = int(input("Enter your guess: "))
        
        if guess == number_to_guess:
            print(f"Congratulations! You guessed the number {number_to_guess} correctly.")
            return
        else:
            print("Incorrect guess. Try again.")
        
        chances -= 1
    
    print(f"Game over! The number to guess was {number_to_guess}.")

print("Welcome to the Number Guesser game!")
difficulty = input("Choose difficulty level (normal/hard): ").lower()

number_guesser(difficulty)
