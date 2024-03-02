'''
PRIME SUM

Given an even number ( greater than 2 ), return two prime numbers whose sum will be equal to the given number.
If there is more than one solution possible, return the lexicographically smaller solution i.e.
If [a, b] is one solution with a <= b,
and [c,d] is another solution with c <= d, then

[a, b] < [c, d] 
If a < c OR ( a == c AND b < d ).
NOTE: A solution will always exist. read Goldbach's conjecture

Problem Constraints
1 <= A <= 2 * 107

Input Format
The first argument is an integer A.

Output Format
Return an array of integers.

Example Input
4

Example Output
[2, 2]
'''
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n%2 == 0 or n%3 == 0:
        return False
    
    i = 5
    while i*i <= n:
        if n%i == 0 or n%(i+2) == 0:
            return False
        i += 6
    return True
    
def primesum(A):
    for i in range(2, A // 2 +1):
        if is_prime(i) and is_prime(A-i):
            return [i, A-i]

A = 10
result = primesum(A)
print(result)  # Output: [3, 7]
