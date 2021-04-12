# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # # Iterative Solution
    # def reverseList(self, head: ListNode) -> ListNode:
    #     curr = head
    #     prev = None
    #     if head is None:
    #         return head
    #     while curr.next is not None:
    #         head = curr.next
    #         curr.next = prev
    #         prev = curr
    #         curr = head
    #     curr.next = prev
    #     return head

    # # Recursive Solution
    def helper(self, prev: ListNode, curr: ListNode) -> ListNode:
        if curr.next is not None:
            head = self.helper(curr, curr.next)
            curr.next = prev
            return head
        else:
            curr.next = prev
            return curr

    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        return self.helper(None, head)
