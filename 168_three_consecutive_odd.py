# Three Consecutive Odds

# Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.

# Example 1:
# Input: arr = [2,6,4,1]
# Output: false
# Explanation: There are no three consecutive odds.

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0
        
        for num in arr:
            if ((num % 2) != 0):
                count += 1
                if count == 3:
                    return True
            else:
                count = 0
        
        return False