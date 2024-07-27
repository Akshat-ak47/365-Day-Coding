# Relative Sort Array
# Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.
# Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.

# Example 1:

# Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
# Output: [2,2,2,1,4,3,3,9,6,7,19]

from typing import List
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = {}
        for num in arr1:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        result = []
        for num in arr2:
            if num in count:
                result.extend([num] * count[num])
                del count[num]
        
        remaining = sorted(count.keys())
        for num in remaining:
            result.extend([num] * count[num])
        
        return result
