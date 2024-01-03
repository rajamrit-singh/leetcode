class Solution:
    def reverseBits(self, n: int) -> int:
        res = ""
        for i in range(0, 32):
            bit = (n & 1)
            res += str(bit)
            n = n >> 1
        print(res)
        return int(res, 2)