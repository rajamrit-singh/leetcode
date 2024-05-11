# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return True
        
        # Find the middle of the linked list
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse the second half of the linked list
        second_half = self.reverseLinkedList(slow.next)
        
        # Compare the first and second halves
        while second_half:
            if head.val != second_half.val:
                return False
            head = head.next
            second_half = second_half.next
        
        return True
    
    def reverseLinkedList(self, node):
        prev = None
        current = node
        
        while current:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
        
        return prev
