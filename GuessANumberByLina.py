import random

def guess_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("Welcome to Guess A Number by Lina!")
    print("I have chosen a random number between 1 and 100.")
    print("Can you guess the number?")

    while True:
        user_guess = int(input("Enter your guess: "))
        attempts += 1

        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the number in", attempts, "attempts.")
            break

if __name__ == "__main__":
    guess_number()
