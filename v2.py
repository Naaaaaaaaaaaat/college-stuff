#create answer
intAnswer = 1234
intGuess = 1

while intGuess != 0:

    # get the input from user and assign to variable
    intGuess = int(input("Enter Your Guess or 0 to Exit:"))

    # print("Answer = ", intAnswer)
    # print("Guess = ", intGuess)

    if intAnswer == intGuess:
        print("Your guess", intGuess, "is correct! .;,,,;.")
    else:
        print("Your guess", intGuess, "is wrong. :[ Please try again.")