# You can comment by putting # in front of a text.

#First off we will start off with the humble while loop.
#Now notice the syntax: first we declare our variable,
#while condition is followed with a colon,
#in order to concenate a string with a number
#we must turn it into a string as well.
#Finally don't forget the incremental counter which will allow us
#to actually exit the file!!!!

n = 0
while n <= 5:
    print ("While is now " + str(n))
    n = n+1

#Now we will move on to the for loop.
#range will give us a collection of numbers. For now, the old fella
#will explain the real things later on.
#range syntax: range(start, stop, step)

for n in range(5):
    print (n)

mySum = 1
for i in range(1, 12, 1):
    print("i is now " + str(i))
    if i == 11:
        print("Oh snap we are now over 11!")
        break
#Note that it will always stop one step before the stop value in the range.

#Also check this little loop out.
if type(varA) == str or type(varB) == str:
    print("string involved")
elif varA > varB:
    print("bigger")
elif varA == varB:
    print("equal")
else:
    print("smaller")
#Checkin types, elif statements, elses... What else do you need?