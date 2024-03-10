import heapq

class Solution:
    def solve(self, A):
        heapq.heapify(A)
        cost = 0
        
        while len(A) > 1:
            min1 = heapq.heappop(A)
            min2 = heapq.heappop(A)
            
            new_len = min1 + min2
            cost += new_len
            
            heapq.heappush(A, new_len)
        
        return cost

# Test cases
A1 = [1, 2, 3, 4, 5]
A2 = [5, 17, 100, 11]

solution = Solution()
print(solution.solve(A1))  # Output: 33
print(solution.solve(A2))  # Output: 182
