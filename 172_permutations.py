# Permutations
# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def heap_permute(n, arr):
            if n == 1:
                result.append(arr[:])
                return
        
            for i in range(n):
                heap_permute(n-1, arr)
                if n % 2 == 0:
                    arr[i], arr[n-1] = arr[n-1], arr[i]
                else:
                    arr[0], arr[n-1] = arr[n-1], arr[0]

        result = []
        heap_permute(len(nums), nums)
        return result