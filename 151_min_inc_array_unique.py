# Minimum Increment to Make Array Unique

# You are given an integer array nums. In one move, you can pick an index i where 0 <= i < nums.length and increment nums[i] by 1.
# Return the minimum number of moves to make every value in nums unique.
# The test cases are generated so that the answer fits in a 32-bit integer.

# Example 1:
# Input: nums = [1,2,2]
# Output: 1
# Explanation: After 1 move, the array could be [1, 2, 3].

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums = sorted(nums)
        count = 0

        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                increment = nums[i-1] - nums[i]+1
            
                count += increment
                nums[i] += increment
        
        return count