#Import random library
import random

#Initialize ANSWER var and assign value
intAnswer = random.randint(1,99999)
#initialize GUESS var and assign value
intGuess = 1
intCount = 0

#Start WHILE loop
while intGuess != 0:

    # get the input from user and assign to variable
    intGuess = int(input("Enter Your Guess or 0 to Exit:"))
    intCount += 1

    print("Guess:", intCount, "of 10")

    # print("Answer = ", intAnswer)
    # print("Guess = ", intGuess)


    if intCount <= 10:
        if intGuess == 0:
            print("See you next time :]")
            break
        elif intAnswer < intGuess:
            print("Your guess", intGuess, "TOO HIGH :[ Please try again.")
        elif intAnswer > intGuess:
            print("Your guess", intGuess, "TOO LOW :[ Please try again.")
        else:
            print("Your guess", intGuess, "Is CORRECT! .;,,,,;.")
            break
    else:
        print("You have run out of guesses! Goodbye!")
        break



