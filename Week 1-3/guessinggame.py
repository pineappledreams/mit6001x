#The point of this game is for the computer to guess the user's number
#using bisection search. It should go something like this

high = 100
low = 0
guess = (high + low)//2  

print("Please think of a number between 0 and 100!")
print("Is your secret number " + str(guess) +"?")

guessing = True
while guessing:
    userInput = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. " + 
    "Enter 'c' to indicate I guessed correctly.")
    if userInput == "h":
        high = guess
        guess = (low + guess)//2
        print("Is your secret number " + str(guess) +"?")
    elif userInput == "l":
        low = guess
        guess = (high + guess)//2
        print("Is your secret number " + str(guess) +"?")
    elif userInput == "c":
        print("Game over. Your secret number was: " + str(guess))
        break
    else:
        print("Sorry, I did not understand your input.")
        print("Is your secret number " + str(guess) +"?")
