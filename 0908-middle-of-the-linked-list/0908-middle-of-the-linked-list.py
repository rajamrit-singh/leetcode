# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head == None or head.next == None):
            return head
        slowPtr = head
        fastPtr = head
        while (fastPtr.next and fastPtr.next.next):
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next
        if (fastPtr.next):
            slowPtr = slowPtr.next
        return slowPtr