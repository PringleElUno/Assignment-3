# Author: Luis Pringle
# GitHub username: PringleElUno
# Date: 10/15/2024
#A game where the user/someone else is asked to input an integer. If the player's guess is higher than the target
#the program should display too high integer. If the user's guess is lower than target integer, the program should
#should display to low.

# Enter the integer to start guessing game
print ("Enter the integer for the player to guess.")
user_guess = int(input())

guesses_took = 0

print ("Enter your guess.")

# Running the while loop infinitely
while True:
    guess = int(input())

    guesses_took +=1
# If guess is greater than the user guess will be "Too High"
    if guess > user_guess:
        print("Too high - try again:")
# If guess is lower than the user guess will be "Too Low"
    elif guess < user_guess:
        print("Too low - try again:")
# If guess is correct then breaks the loop
    else:
        break
# print the number of guesses user took
if guesses_took == 1:
    print("You guessed it in 1 try.")
else:
    print("You guessed it in", guesses_took, "tries.")

