import string

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
    yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...

    allLetters = list(string.ascii_lowercase)
    availableLetters = ""

    for char in allLetters:
        if char not in lettersGuessed:
            availableLetters += char
    print (availableLetters)