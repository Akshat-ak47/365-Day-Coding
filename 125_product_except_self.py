# Product of Array Except Self

# the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

from typing import List

class Solution:
    def multiply(self, nums):
        mult = 1
        n = len(nums)
        for i in range(n):
            mult *= nums[i]
        return mult
        
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = []

        total_product = self.multiply(nums)

        for i in range(n):
            if nums[i] == 0:
                # Calculate product except for the zero element
                product_except_zero = self.multiply(nums[:i] + nums[i+1:])
                answer.append(product_except_zero)
            else:
                ans = total_product / nums[i]
                answer.append(int(ans))
        
        return answer

solution = Solution()
print(solution.productExceptSelf([-1, 1, 0, -3, 3]))
