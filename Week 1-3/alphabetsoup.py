#Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 
# For example, if s = 'azcbobobegghakl', then your program should print
# Longest substring in alphabetical order is: beggh
#In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
#Longest substring in alphabetical order is: abc

#Now how do we go through it. 

#This is my PSUEDOCODE -
#0. Declare alphabet. This will be our key to solve the mystery.
#1. Get string. Compare first letter of letter. Let's say it's S. Add one to counter by default, as shortest combo can be 1.
#2. Compare next letter. Is it STUVWXYZ or any letter following and including S? Yes - Add one to counter. If not, reset to alphabet.
#3. Every time it does a check. Let's say next letter was P. It will look for PQRSTUVWXYZ next time. 
#4. Each time its the following letter the key will get shorter while we are adding to the counter.
#Summary: Get string. Loop - Compare to alphabet -> Add a counter-and-shorten-alphabet or reset.
#Finally display counter score and longest streak.

#First we need to declare an alphabet.

alphabet = "abcdefghijklmnopqrstuvwxyz"
#Now we would need to declare a string we would know it would work.
s = "abcdeloiman" #positive - abcdelo = 7 combo!!

longestCombo = 1
i = 0
maxi = 0

while i < len(s):
    if (len(s) - i <= longestCombo):
        print("DONE")
        break
    starti = i
    tempCombo = 1
    
    while (i + 1 < len(s) and s[i] <=  s[i+1]):
        tempCombo += 1
        i += 1
    
    if tempCombo > longestCombo:
        longestCombo = tempCombo
        maxi = starti
    
    i += 1

longestWord = s[maxi:maxi+longestCombo]
print ('Longest substring in alphabetical order is: ' + str(longestWord))
print(len(longestWord))