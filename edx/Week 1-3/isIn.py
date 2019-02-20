def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    halfStr = len(aStr) // 2
    if len(aStr) == 0:
        return False
    if char == aStr[halfStr]:
        return True
    elif (len(aStr) == 1) and (char != aStr):
        return False
    if char > aStr[halfStr]:
        return isIn(char, aStr[halfStr:])
    else:
        return isIn(char, aStr[:halfStr])

    
        