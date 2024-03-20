'''
MATH_BUG01

Following code tries to figure out if a number is prime ( Wiki )
However, it has a bug in it.
Please correct the bug and then submit the code.

class Solution:
    # @param A : integer
    # @return an integer
    def isPrime(self, A):
	upperLimit = int(A**0.5)
	for i in xrange(2, upperLimit + 1):
		if i < A and A % i == 0:
			return 0
	return 1


'''
class Solution:
    def isPrime(self, A):
        if A < 2:
            return 0
        upperLimit = int(A**0.5)
        for i in range(2, upperLimit + 1):
            if A % i == 0:
                return 0
        return 1

solution = Solution()
A = 5
print(solution.isPrime(A)) 