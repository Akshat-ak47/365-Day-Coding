# Removing Stars From a String

# You are given a string s, which contains stars *.
# In one operation, you can:
# Choose a star in s.
# Remove the closest non-star character to its left, as well as remove the star itself.
# Return the string after all stars have been removed.

# Note:
# The input will be generated such that the operation is always possible.
# It can be shown that the resulting string will always be unique.

class Solution:
    def removeStars(self, s: str) -> str:
        n = len(s)
        result = []
        if n<=0:
            return ''
        else:
            for char in s:
                if char == "*":
                    if result:
                        result.pop()
                else:
                    result.append(char)
        
        return ''.join(result)
    
solution = Solution()
s = "abc*d*e*f*g*h*i*j"
result = solution.removeStars(s)
print(result)