"""
Today we are gonna learn about tuples and what are the things that we can do about it.


A tuple is a ordered sequence of elements, can contain anything elements.
AKA. ARRAY? Immutable.

You can also go into the tuple by 

t = (2, 3, 4)
t + (6, 8)

t[1:2] 

You can reverse tuple swap variables.

(x, y) = (y, x)

"""

"""

Write a procedure called oddTuples, which takes a tuple as input, and returns a new tuple as output, 
where every other element of the input tuple is copied, starting with the first one. 
So if test is the tuple ('I', 'am', 'a', 'test', 'tuple'), then evaluating oddTuples on this input would 
return the tuple ('I', 'a', 'tuple').

"""



def oddTuples(aTup):
    rTup = ()
    index = 0
    while index < len(aTup):
        rTup += (aTup[index],)
        index += 2
    return rTup
