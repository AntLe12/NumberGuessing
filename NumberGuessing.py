import random
computerNum = random.randint(1, 100) # Random number generator from 1 to 100
initialGuess = input("Enter a number: ") # Asks the user for a number
currentGuess = int(initialGuess) # Sets the new guess equal to the first guess as an int
if currentGuess > computerNum:  # Checks if the currentGuess is bigger than the computer's number right off the bat
    print("Your guess is bigger")
else:
    print("Your guess is smaller")
while currentGuess != computerNum: # checks for if the current guess is
    print("Guess again: ")
    currentGuess = int(input()) # Converts the string input into an integer
    if currentGuess > computerNum: # Checks if the currentGuess is bigger than the computer's number
        print("Your guess is bigger")
    else:
        print("Your guess is smaller")
convertedNumToString = str(currentGuess) # Changes the final answer into a readable string
print("The number was: " + convertedNumToString)