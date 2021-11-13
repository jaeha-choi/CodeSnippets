# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # My attempt
    # def hasCycle(self, head: Optional[ListNode]) -> bool:
    #     node = head
    #     while node:
    #         node.val = None
    #         node = node.next
    #         if node and node.val is None:
    #             return True
    #     return False

    # Attempt after looking at the ans
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        fast = slow = head
        try:
            while slow and fast:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    return True
        except:
            return False
