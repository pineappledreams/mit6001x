def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if a > b:
        test = b
        while test >= 1:
            if (a % test == 0 and b % test == 0):
                gcd = test
                print(str(gcd))
                return gcd
            else:
                test -= 1
    else:
        test = a
        while test >= 1:
            if (a % test == 0 and b % test == 0):
                gcd = test
                print(str(gcd))
                return gcd
            else:
                test -= 1     

gcdIter(999, 333)