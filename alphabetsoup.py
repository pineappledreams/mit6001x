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

alphabet = "abcdefghikjlmnopqrstuvwxyz"
#Now we would need to declare a string we would know it would work.
test1 = "loabcdeloiman" #positive - abcdelo = 7 combo!!



longestStreak = 0

for i in range(0, len(test1), 1):
    

