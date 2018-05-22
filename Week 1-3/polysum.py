
"""
Written 2018/05/08 by pineappledreams

Write a function called polysum that takes 2 arguments, n and s. 
This function should sum the area and square of the perimeter of the regular polygon. 
The function returns the sum, rounded to 4 decimal places.
"""

# n is the number of sides
# s is the length of the side.
# The formula to the area of a polygon is 
# 0.25 times n times s squared divided by tangent (pi divided by n)
# Perimeter length is computed by simply adding all the sides together - n times s.
# The program will give out the area of the polygon plus perimeter length squared
# Also is requested that answer would be rounded to 4 decimal points.
# Thus code:

import math

def polysum (n, s):
    area = (0.25*n*(s**2))/math.tan(math.pi/n)
    perimeter = n * s

    return round((area + perimeter**2), 4)

print (polysum (78, 19))

# Answer should be and is 2371007.3908
# Passes all tests.