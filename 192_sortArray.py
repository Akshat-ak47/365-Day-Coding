# Sort an Array

# Given an array of integers nums, sort the array in ascending order and return it.
# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

# Example 1:

# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).

# Merge Sort - 
#     Time Complexity - O(nlogn)
#     Space Complexity - O(n)

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums
        
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        
        left_half = self.sortArray(left)
        right_half = self.sortArray(right)

        return merge(left_half, right_half)

    def merge(self, left, right):
        result = []
        i = j = 0

        while i<len(left) and j<len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1

        result.extend(left[i:])
        result.extend(right[j:])

        return result