# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if (head.next == None):
            return head
        i = self.getLength(head) - k + 1
        count = 1
        node = head
        while (count < k):
            node = node.next
            count += 1
        l1 = node
        node = head
        count = 1
        while (count < i):
            node = node.next
            count += 1
        l2 = node
        [l1.val, l2.val] = [l2.val, l1.val]
        return head
        
        
    def getLength(self, node):
        count = 0
        while (node != None):
            count += 1
            node = node.next
        return count