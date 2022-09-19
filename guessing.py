# Importing the important modules

import random
import math

print("\nWelcome to the random number guessing game. Please enter your desired range for the randomizer""\n\t\t\t\t Good Luck !!")

# Prompting the user to enter their desired Range.

low = float(input("Enter the Lower Range Value: "))
up = float(input("Enter the Upper Range Value: "))

# Calculating the amount of tries needed to guess the random number, depending on the user’s inserted range.
# The math.log() method returns the natural logarithm of a number, or the logarithm of number to base. math.log(x, base). Since we chose base 2 we are checking binary logarithm.

prob = round(math.log(up - low + 1, 2))
print("\nIt takes about", prob, " tries in general to guess the correct number!\n")

# Initializing the count at 1.
count = 1

# Prompting the user to enter their guess.

num = float(input("Enter your Guess:  "))

# The round() function returns a floating point number that is a rounded version of the specified number, with the specified number of decimals.
# The uniform() method returns a random floating number between the two specified numbers (both included).

x = round(random.uniform(low, up))
while num != x:
    count += 1
    if num < x:
        print("Your Guess was less than the Random number.")
    elif num > x:
        print("Your Guess was greater than the Random number.")
    retry = input("\nWould you like to Guess again? y / n :-  ")
    if retry == "y":
        num = float(input("Enter your Guess: "))
    elif retry == "n":
        print("Better Luck Next time. The Random number was", x)
        break
if num == x:
    print("Congratulation you guessed it","\n""It took you",count,"tries to guess the number")
