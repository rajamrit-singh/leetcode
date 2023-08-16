# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if(head.next == None):
            return head
        prev = head
        node = head.next
        while(node):
            gcp = self.getGcp(prev.val, node.val)
            newNode = ListNode(gcp)
            prev.next = newNode
            newNode.next = node
            prev = node
            node = node.next
        return head
            
    def getGcp(self, num1, num2):
        div = num1 if num1 < num2 else num2
        while(True):
            if(num1 % div == 0 and num2 % div == 0):
                return div
            div -= 1
        return 1