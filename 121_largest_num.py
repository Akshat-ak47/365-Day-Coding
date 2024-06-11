# Largest Number
# Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.
# Since the result may be very large, so you need to return a string instead of an integer.


# Example 1:
# Input: nums = [10,2]
# Output: "210"

# Example 2:
# Input: nums = [3,30,34,5,9]
# Output: "9534330"

from typing import List

class Solution:
    def swap(self, arr: List[int], i: int, j: int):
        arr[i], arr[j] = arr[j], arr[i]

    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                check_1 = str(nums[i]) + str(nums[j])
                check_2 = str(nums[j]) + str(nums[i])
                if check_1 < check_2:
                    self.swap(nums, i, j)

        largest_num = ''.join(map(str, nums))
        largest_num = largest_num.lstrip('0')
        if not largest_num:
            return "0"
        else:
            return largest_num

nums1 = [10, 2]
sol = Solution()
print(sol.largestNumber(nums1))

nums2 = [3, 30, 34, 5, 9]
print(sol.largestNumber(nums2))