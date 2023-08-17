"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        que = deque()
        head = node
        if (node == None or node.neighbors == None):
            return node
        que.appendleft(node)
        cloneNodeList = {}
        visited = set()
        # mySet.append(node.val)
        while(len(que) > 0):
            node = que.popleft()
            if (node.val in visited):
                continue
            if (cloneNodeList.get(node.val)):
                newNode = cloneNodeList.get(node.val)
            else:
                newNode = Node(node.val)
            cloneNodeList[node.val] = newNode
            visited.add(node.val)
            for curNode in node.neighbors:
                if(cloneNodeList.get(curNode.val)):
                    newNode.neighbors.append(cloneNodeList.get(curNode.val))

                else:
                    newCurNode = Node(curNode.val)
                    cloneNodeList[curNode.val] = newCurNode
                    newNode.neighbors.append(newCurNode)
                que.appendleft(curNode)

        print(head.val)
        print(cloneNodeList)
        print(cloneNodeList.get(head.val).val)
        return cloneNodeList.get(head.val)