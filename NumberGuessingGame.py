import random

print("Welcome to the Number Guessing Game")

name = input("\nEnter the player's name : ")

print(f"\nHey {name}, before starting, let me tell you how to play this game.")

print("\nHOW TO PLAY :-\n1. The computer will choose a random number between 1 and 100.\n2. Your task is to guess the correct number.\n3. Enter your guess when prompted.\n4. The game will tell you whether your guess is too high or too low.\n5. Keep guessing until you find the correct number.\n6. Try to guess the number in the fewest attempts possible.\n7. Once you guess the correct number then you will WIN.")

key = input("\nPress 'Enter' to play: ")

secret_number = random.randint(1, 100)
attempt = 0

while True:
    try:
        num = int(input("\nEnter a number between 1 to 100: "))
        if(num > 100 or num < 1):
            print("Please enter a number between 1 and 100.")
            continue
        attempt += 1
        
        if(secret_number > num):
            print("Too low, Guess Again")
        elif(secret_number < num):
            print("Too high, Guess Again")
        else:
            print("\nCongratulations ! You Win.")
            print(f"You guessed it right in total {attempt} attempts.")
            break

    except ValueError:
        print("Invalid input. Please enter a number.")