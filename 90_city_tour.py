'''
City Tour

Problem Description

There are A cities numbered from 1 to A. You have already visited M cities, the indices of which are given in an array B of M integers.
If a city with index i is visited, you can visit either the city with index i-1 (i >= 2) or the city with index i+1 (i < A) if they are not already visited. Eg: if N = 5 and array M consists of [3, 4], then in the first level of moves, you can either visit 2 or 5.
You keep visiting cities in this fashion until all the cities are not visited. Find the number of ways in which you can visit all the cities modulo 10^9+7. 

Example Input
A = 5
B = [2, 5]

Example Output
6
'''
class Solution:
    MOD = 10**9 + 7

    def power(self, x, y):
        res = 1
        while y:
            if y & 1:
                res = (res * x) % self.MOD
            y >>= 1
            x = (x * x) % self.MOD
        return res
    
    def solve(self, A, B):
        B.sort()
        un_vis = []
        i = 1
        un_vis.append(B[0] - 1)
        while i < len(B):
            un_vis.append(B[i] - B[i - 1] - 1)
            i += 1
        un_vis.append(A - B[i - 1])
        n = len(un_vis)
        fact = [1] * 100000
        for f in range(1, 100000):
            fact[f] = (f * fact[f - 1]) % self.MOD
        ans = 1
        x = A - len(B)
        p = 1
        i = 0
        while i < n:
            if not un_vis[i]:
                i += 1
                continue
            if i != 0 and i != n - 1:
                ans = (ans * self.power(2, un_vis[i] - 1)) % self.MOD
            p = (p * fact[un_vis[i]]) % self.MOD
            i += 1
        ans = (ans * fact[x]) % self.MOD
        ans = (ans * self.power(p, self.MOD - 2)) % self.MOD
        return ans


sol = Solution()
A = 3
B = [1]
print(sol.solve(A, B))
