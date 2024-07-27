# Sqrt(x)
# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.

# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

# Example 1:

# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.

import math

def sqroot(x, tolerance=1e-10):
    if x == 0:
        return 0
    
    guess = x/2
    while True:
        new_guess = (guess + (x/guess))/2
        if abs(new_guess - guess) < tolerance:
            return new_guess
        else:
            guess = new_guess

x = 4
print(sqroot(x))

x = 8
sqroot(x)
print(sqroot(x))
x = 16
sqroot(x)
print(sqroot(x))
x = 16

print(math.sqrt(x))
