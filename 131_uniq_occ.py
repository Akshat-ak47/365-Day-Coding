from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        n = len(arr)
        count = {}
        for num in arr:
            count[num] = count.get(num, 0) + 1
        
        occurence = list(count.values())

        return len(count) == len(set(occurence))
            