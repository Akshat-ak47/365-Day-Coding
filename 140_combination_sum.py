# Combination Sum

# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
# frequency
#  of at least one of the chosen numbers is different.
# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(remaining, combo, start):
            if remaining == 0:
                result.append(list(combo))
                return
            for i in range(start, len(candidates)):
                candidate = candidates[i]
                if candidate > remaining:
                    break
                
                combo.append(candidate)
                backtrack(remaining-candidate, combo, i)
                combo.pop()
        
        candidates.sort()
        result = []
        backtrack(target, [], 0)
        return result
