#Import random library
import random

#Initialize ANSWER var and assign value
intAnswer = random.randint(1,99999)
#initialize GUESS var and assign value
intGuess = 1

#Start WHILE loop
while intGuess != 0:

    # get the input from user and assign to variable
    intGuess = int(input("Enter Your Guess or 0 to Exit:"))

    # print("Answer = ", intAnswer)
    # print("Guess = ", intGuess)

    #Compare variable and select answer
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