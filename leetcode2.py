class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = ListNode()
        cursor = root
        carry = 0
        while l1 is not None or l2 is not None or carry > 0:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            sumVal = x + y + carry
            carry = sumVal // 10
            nextNode = ListNode(sumVal % 10)
            cursor.next = nextNode
            cursor = nextNode
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        return root.next
