#Problem statement:
#Write a program that will find all the vowels in the string and count them up.

s = "Somanybows!!!"
vowels = 0

for char in s:
    if char == 'a' or char == 'e' or char == 'i' \ 
       or char == 'o' or char == 'u':
       vowels += 1

#First time using \ as a newline!

print (s)
print ("Number of vowels:" + str(vowels))