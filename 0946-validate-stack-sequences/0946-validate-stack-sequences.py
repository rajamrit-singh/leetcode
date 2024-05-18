class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        k = 0
        for el in pushed:
            stack.append(el)
            while(len(stack) > 0 and len(popped) > 0 and stack[-1] == popped[k]):
                stack.pop()
                k += 1
        return len(stack) == 0
                