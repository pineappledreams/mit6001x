def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

#The one thing that I do struggle is with recursive functions.
#I get the idea that we gotta call the function, but to make it so that it wont loop forever...
#Git gud is how it goes I guess!