'''
Salutes

Problem Description
 
 
In a long hallway some soldiers are walking from left to right and some from right to left all at the same speed.

Every time while walking they cross through another soldier they salute and move ahead.

Given a string A of length N showing the soldiers' direction they are walking. 
'<' denotes a soldier is walking from right to left, and '>' denotes a soldier is walking from left to right. 
Return the number of Salutes done.

'''

class Solution:
    def countSalutes(self, A):
        rtl = 0
        salutes = 0
        
        for i in A:
            if i == ">":
                rtl += 1
            elif i == "<":
                salutes += rtl
        
        return salutes

solution = Solution()
print(solution.countSalutes(">><"))