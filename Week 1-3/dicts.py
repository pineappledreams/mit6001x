"""
Functions are first class objects.
They have types, can be elements of data structures and can appear in expressions.
We can use functions as arguments in lists, which will give us the power of
higher order programming.

Now we can do a lot of things.

seq[i] - ith element of sequence
len[seq] - length of sequence
seq1 + seq2 - concatenation of sequence
n * seq - sequence that repeats seq n times 
seq[start:end] - slice of sequence
e in seq - true if e contained in sequence
e not in seq - true if e contained in sequence
for e in seq - iterates over elements of sequence.

DICTIONARIES
have keys and values.

my_dict = {}
grades = ('ana':'b', 'john':'a')

grades['john']
Prints out a.

grades['Sylvan'] = 'a'

grades['sylvan']
returns 'a'

john in grades
returns true

daniel in grades
returns false

del{grades['ana']}
Boom, ana's gone.

dictionaries can have anything - immutable, mutable, functions, strings, ints, lists, dictionaries....
they can have duplicates

BUT
they need unique keys. 
key needs to be immutable - int, float, string, tuple, boolean.

lists are ordered - got indexes. look up by the index. 
index is an integer

DICTIONARIES however got matching keys and values,
look up a key to look up the value. 
No order, any type of data. 

"""

