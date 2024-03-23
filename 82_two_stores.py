'''
Two Stores

Problem Description

You want to buy A candies, there are two candy stores in your town.
The stores sell candies in packets, first store sells B candies for C rupees and the other store sells D candies for E rupees.
Find the minimum cost to buy exactly A candies if you can buy any amount of packets from both stores.
If it is not possible to do so return -1.

'''

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @param E : integer
    # @return an integer
    def solve(self, A, B, C, D, E):
        min_cost = float('inf')
        
        for first_store in range(0, A // B + 1):
            candies_left = A - first_store*B
            second_store = candies_left // D
            total_cost = first_store * C + second_store * E
            
            if candies_left % D == 0 and total_cost < min_cost:
                min_cost = total_cost
        
        if min_cost == float('inf'):
            return -1
        else:
            return min_cost

solution = Solution()
A = 7
B = 1
C = 1
D = 3
E = 2
print(solution.solve(A, B, C, D, E))