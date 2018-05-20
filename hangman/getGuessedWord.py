def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
    what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...

    #First off if we will have the secret word in a list
    #We should be able to clone the list as secretHidden
    #which will reveal a letter every time it gets added (or not added)
    #to the lettersGuessed.

    secretHidden = list(secretWord)
    for char in secretHidden:
        if char in lettersGuessed:
            #something
        else:
            return False