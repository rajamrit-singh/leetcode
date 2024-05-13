class Node:
    def __init__(self):
        self.val = None
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node()
        self.head.val = homepage

    def visit(self, url: str) -> None:
        newNode = Node()
        newNode.val = url
        self.head.next = newNode
        newNode.prev = self.head
        self.head = self.head.next

    def back(self, steps: int) -> str:
        count = 0
        while (self.head.prev and count < steps):
            self.head = self.head.prev
            count += 1
        return self.head.val

    def forward(self, steps: int) -> str:
        count = 0
        while (self.head.next and count < steps):
            self.head = self.head.next
            count += 1
        return self.head.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)