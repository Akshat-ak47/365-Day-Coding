'''
Bulls and Cows

Problem Description

You are playing the Bulls and Cows game with your friend.
You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:

The number of "bulls", which are digits in the guess that are in the correct position.
The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. 
Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls. 
Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.

Input 1:
secret = "1807", guess = "7810"

Ouput 1:
"1A3B"
'''

class Solution:
    def solve(self, A, B):
        x_bull = 0
        y_cow = 0
        freqA = [0] * 10
        freqB = [0] * 10
        
        for i in range(len(A)):
            if A[i] == B[i]:
                x_bull += 1
            else:
                freqA[int(A[i])] += 1
                freqB[int(B[i])] += 1
        
        for i in range(10):
            y_cow += min(freqA[i], freqB[i])
        
        return str(x_bull) + "A" + str(y_cow) + "B"

solution = Solution()
secret = "1807"
guess = "7810"
print(solution.solve(secret, guess))