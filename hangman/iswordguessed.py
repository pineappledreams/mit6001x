
def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...

#What we need to do:
# 1. have the word, the letters guessed, run the list hrough the listed string and see if it
# has all the required letters in the guessed. Wait a minute....
    goodGuess = 0
    secretList = list(secretWord)
    for char in secretList:
      if char in lettersGuessed:
        goodGuess += 1
      else:
        print ("TRY AGAIN!!!")
        return False
      if goodGuess == len(secretWord):
        print ("YOU DONE IT BRO!")
        return True

isWordGuessed("feel", ["f", "l", "e"])


