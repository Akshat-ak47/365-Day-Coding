'''
Add Two Numbers as Lists

You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)

Output: 7 -> 0 -> 8

    342 + 465 = 807
Make sure there are no trailing zeros in the output list

So, 7 -> 0 -> 8 -> 0 is not a valid response even though the value is still 807.

'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        while A or B or carry:
            sum_val = carry
            
            if A:
                sum_val += A.val
                A = A.next
            if B:
                sum_val += B.val
                B = B.next
            
            carry, remainder = divmod(sum_val, 10)
            current.next = ListNode(remainder)
            current = current.next
        
        return dummy.next
    

# Define the linked lists
A = ListNode(9)
A.next = ListNode(9)
A.next.next = ListNode(1)

B = ListNode(1)

# Create Solution object
solution = Solution()

# Call the function
result = solution.addTwoNumbers(A, B)

# Print the result
while result:
    print(result.val, end=" -> ")
    result = result.next