# Sort Colors

# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We wil use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# You must solve this problem without using the librarys sort function.
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = []
        white = []
        blue = []
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                red.append(nums[i])
            elif nums[i] == 1:
                white.append(nums[i])
            elif nums[i] == 2:
                blue.append(nums[i])
        nums[:] = red+white+blue
        return nums
            
solution = Solution()
nums = [2, 1, 0, 2, 0, 1, 2]
print(solution.sortColors(nums))