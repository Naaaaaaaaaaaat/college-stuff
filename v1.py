# create the answer
intAnswer = 12345

#get input from user and assign to variable
intGuess = int(input("Enter Your Guess:"))

#print("Answer = ", intAnswer)
#print("Guess = ", intGuess)

if intAnswer == intGuess:
    print("Your guess", intGuess, "is correct! .;,,,;.")
else:
    print("Your guess", intGuess, "is wrong. :[ Please try again.")
