# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        count = 0

        while current is not None:
            count += 1
            current = current.next

        mid = count // 2

        if mid == 0:
            return head.next
        elif mid == 1:
            head.next = head.next.next
            return head
        
        current = head
        prev = None
        index = 0
        
        while index < mid:
            prev = current
            current = current.next
            index += 1
        
        prev.next = current.next

        return head
        