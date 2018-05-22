#This is the another exercise we did in mit6001. It's about finding a string inside a string.
#I wrote a program which would just crawl through the string 3 letters at a time and find the string - "bob" we need.
#We could use the same logic and find any kind of string we need later on by turning the i+3 into  i+len(string)
# and == "bob" into whatever thing you need. LIKE THIS!

s = str(input("enter string you want to search in: "))
showBobs = 0
myString = str(input("enter substring: "))

for i in range(0, len(s), 1):
    if s[i:i+len(myString)] == myString:
        showBobs += 1

print ("You searched for" + myString + " in " + s + "!")
print ("Number of times " + myString + " occurs is: " + str(showBobs))

#Also please no bully - only lower chars !!!