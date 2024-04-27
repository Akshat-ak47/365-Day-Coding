# Two out of Three

# Problem Description
# Given are Three arrays A, B and C.
# Return the sorted list of numbers that are present in atleast 2 out of the 3 arrays.

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return a list of integers
    def solve(self, A, B, C):
        setA = set(A)
        setB = set(B)
        setC = set(C)
        
        intersectionAB = setA.intersection(setB)
        intersectionBC = setB.intersection(setC)
        intersectionAC = setA.intersection(setC)
        
        result = intersectionAB.union(intersectionAC, intersectionBC)
        
        return sorted(list(result))

solution = Solution();
A = [1, 1, 2]
B = [2, 3]
C = [3]
print(solution.solve(A, B, C))