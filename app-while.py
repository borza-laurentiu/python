keyword = 'giraffe'
guess = ''
guessCount = 0
guessLimit = 3
out_of_guesses = False

while guess != keyword and not(out_of_guesses):   #not(out_of_guesses) is False (not True), because of the not in front

    if guessCount < guessLimit:
        guess = input("enter guess: ")
        guessCount += 1 #setting up a counter to allow for maximum of 3 tries
    else:
        out_of_guesses = True

if out_of_guesses:    #if out_of_guesses is True
    print("You Lost!")
else:
    print("You Won!")
    
