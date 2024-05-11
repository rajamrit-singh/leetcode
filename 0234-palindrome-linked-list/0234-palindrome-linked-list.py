# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if (head == None or head.next == None):
            return True

        slowPtr = head
        fastPtr = head
        while fastPtr.next and fastPtr.next.next:
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next
        slowPtr = slowPtr.next

        reversedLL = self.reverseLinkedList(slowPtr)
        while (reversedLL):
            if(reversedLL.val != head.val):
                return False
            reversedLL = reversedLL.next
            head = head.next
        return True
        
    

    
    def reverseLinkedList(self, node):
        prev = None
        current = node
        
        while(current != None):
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
        return prev