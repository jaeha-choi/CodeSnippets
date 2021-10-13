class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        curr = head
        curr1 = l1
        curr2 = l2
        val = 0
        while curr1 is not None or curr2 is not None:
            if curr1 is None:
                val1 = 0
            else:
                val1 = curr1.val
            if curr2 is None:
                val2 = 0
            else:
                val2 = curr2.val

            val += val1 + val2
            val = str(val)
            curr.val = int(val[-1])
            if len(val[:-1]) == 0:
                val = 0
            else:
                val = int(val[:-1])

            if curr1 is not None:
                curr1 = curr1.next
            if curr2 is not None:
                curr2 = curr2.next
            if not (curr1 is None and curr2 is None):
                curr.next = ListNode()
                curr = curr.next

        if val != 0:
            curr.next = ListNode(val)
        return head
