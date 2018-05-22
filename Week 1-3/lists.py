""" 
Lists: Ordered sequence, square brackets, 
elements, MUTABLE!
"""

L = [0, 1, 2, 3]

total = 0
for i in range(len(L)):
    total += L[i]
print (total)

#or

total = 0
for i in L:
    total += i
print (total)

# You can also do FUN THINGS.

L.append[5] - adds thing.

#Everything's an object in Python, so
#objects have data
#objects also have methods and functions!
#It's accessed by objectName.dosomething() .method

L3 = L1 + L2
#OR
L1.extend([2,3])

#Deletion

del(L[2])
L.pop(), returns removed element.
L.remove(3) - removes first instance of 3 OR gives error.

#Converting strings into lists.
s = "abc"
list(s)
#returns ["a", "b", "c"]

#things with lists.
s = "I <3 CS"
list(s)
s.split("<") returns ["I ", "<3 CS"]
L = ["a", "b", "c"]
"".join(L) returns "abc"
"_".join(L) returns "a_b_c"

"""
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

list = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range (z+1) if i + j + k != n]
print (list)

"""

#HOW TO CLONE?
cool = ['grey', 'blue']
chill = cool[:]

#If we wouldve just chill = cool, it wouldve caused an alias. NG, man!

#sort vs. sorted
#Sort mutates the list, but doesnt return values.  sorted does not mutate, but just returns the list.
#There are gonna be gotchas, like if you alias but not clone something then when you mutate the list 1
#then anything that relies on the list WILL get absolutely nuts. So be careful!



