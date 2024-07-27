# Reverse Substrings Between Each Pair of Parentheses

# You are given a string s that consists of lower case English letters and brackets.
# Reverse the strings in each pair of matching parentheses, starting from the innermost one.
# Your result should not contain any brackets.

# Example 1:
# Input: s = "(abcd)"
# Output: "dcba"

# Example 2:
# Input: s = "(u(love)i)"
# Output: "iloveu"
# Explanation: The substring "love" is reversed first, then the whole string is reversed.

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        n = len(s)
        result = list(s)

        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                left = stack.pop()
                result[left+1:i] = reversed(result[left+1:i])
        
        return ''.join(c for c in result if c not in '()')