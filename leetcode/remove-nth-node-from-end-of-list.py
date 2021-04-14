# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # # o(n) solution
    # def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    #     nodes = []
    #     curr = head
    #     while curr is not None:
    #         nodes.append(curr)
    #         curr = curr.next
    #     if len(nodes) -  n -1 < 0:
    #         if len(nodes) == 1:
    #             return None
    #         prev_node = None
    #         return nodes[len(nodes) -  n +1]
    #     prev_node = nodes[len(nodes) -  n -1]
    #     node_to_del = prev_node.next
    #     if node_to_del.next is not None:
    #         next_node = node_to_del.next
    #     else:
    #         next_node = None
    #     prev_node.next = next_node
    #     return head

    # o(n) in-place solution
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        n_last_idx = 0
        curr_idx = 0
        curr = head
        n_last = curr
        while curr is not None:
            curr = curr.next
            curr_idx += 1
            if curr_idx - n_last_idx == n + 2:
                n_last = n_last.next
                n_last_idx += 1
        if curr_idx == 1 and n == 1:
            return None
        elif curr_idx == n:
            return head.next
        else:
            n_last.next = n_last.next.next
            return head
