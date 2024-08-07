# Grumpy Bookstore Owner

# There is a bookstore owner that has a store open for n minutes. Every minute, some number of customers enter the store. You are given an integer array customers of length n where customers[i] is the number of the customer that enters the store at the start of the ith minute and all those customers leave after the end of that minute.
# On some minutes, the bookstore owner is grumpy. You are given a binary array grumpy where grumpy[i] is 1 if the bookstore owner is grumpy during the ith minute, and is 0 otherwise.
# When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise, they are satisfied.
# The bookstore owner knows a secret technique to keep themselves not grumpy for minutes consecutive minutes, but can only use it once.
# Return the maximum number of customers that can be satisfied throughout the day.

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        satisfied = 0
        
        for i in range(len(customers)):
            if grumpy[i] == 0:
                satisfied += customers[i]
        
        extra_satisfied = 0
        max_extra_satisfied = 0

        for i in range(len(customers)):
            if i < minutes:
                extra_satisfied += customers[i] * grumpy[i]
            else:
                extra_satisfied += customers[i] * grumpy[i] - customers[i - minutes] * grumpy[i - minutes]
            max_extra_satisfied = max(extra_satisfied, max_extra_satisfied)
        
        return satisfied + max_extra_satisfied