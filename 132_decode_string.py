class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_num = 0
        result = ""

        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char == "[":
                stack.append((current_num, result))
                current_num = 0
                result = ""
            elif char == "]":
                prev_num, prev_str = stack.pop()
                result = prev_str + prev_num * result
            else:
                result += char    
        
        return result

sol = Solution()
print(sol.decodeString("3[a]2[bc]"))  # Output: "aaabcbc"
print(sol.decodeString("3[a2[c]]"))   # Output: "accaccacc"
print(sol.decodeString("2[abc]3[cd]ef"))  # Output: "abcabccdcdcdef"