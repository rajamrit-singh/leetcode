# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if (head.next.next == None):
            return head.val + head.next.val
        slowPtr = head
        fastPtr = head
        maxSum = 0
        while (fastPtr.next and fastPtr.next.next):
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next
        l2 = self.reverseLinkedList(slowPtr.next)
        slowPtr.next = None
        l1 = head
        while (l1 and l2):
            maxSum = max(maxSum, l1.val + l2.val)
            l1 = l1.next
            l2 = l2.next
        return maxSum

    def reverseLinkedList(self, node):
        if (node == None or node.next == None):
            return node
        newhead = self.reverseLinkedList(node.next)
        nextnode = node.next
        nextnode.next = node
        node.next = None
        return newhead