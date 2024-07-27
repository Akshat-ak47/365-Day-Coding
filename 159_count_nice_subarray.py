# Count Number of Nice Subarrays

# Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.
# Return the number of nice sub-arrays.

# Example 1:
# Input: nums = [1,1,2,1,1], k = 3
# Output: 2
# Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        arr = []
        for i in range(n):
            arr.append(0)
        
        for i in range(n):
            if nums[i]%2 != 0:
                arr[i] = 1
            
        counts = {0:1}
        current_sum = 0
        subarray = 0

        for count in arr:
            current_sum += count
        
            if current_sum - k in counts:
                subarray += counts[current_sum - k]
            if current_sum in counts:
                counts[current_sum] += 1
            else:
                counts[current_sum] = 1

        return subarray

