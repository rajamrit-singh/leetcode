# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        if (node == None or node.next == None):
            return node
        
        nextnode = node.next
        nodeToReturn = nextnode
        prev = node
        node = nextnode.next
        nextnode.next = prev
        while (node and node.next):
            nextnode = node.next
            prev.next = nextnode
            prev = node
            node = nextnode.next
            nextnode.next = prev
        if (node == None):
            prev.next = None
        else:
            prev.next = node
        return nodeToReturn