class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        self.memo = {}
        ptr = 0
        is_s1_active = False
        s1_ptr = 0
        s2_ptr = 0
        self.isPossible = False
        def backTrack(ptr1, ptr2):
            if ((ptr1, ptr2) in self.memo):
                return self.memo[(ptr1, ptr2)]
            if (ptr1 == len(s1) and ptr2 == len(s2) and ptr1 + ptr2 == len(s3)):
                return True
            if (ptr1 > len(s1) or ptr2 > len(s2) or ptr1 + ptr2 >= len(s3)):
                return False
            if(ptr1 < len(s1) and s3[ptr1 + ptr2] == s1[ptr1] and ptr2 < len(s2) and s3[ptr1 + ptr2] == s2[ptr2]):
                res = backTrack(ptr1 + 1, ptr2) or backTrack(ptr1, ptr2 + 1)
            elif (ptr1 < len(s1) and s3[ptr1 + ptr2] == s1[ptr1]):
                res = backTrack(ptr1 + 1, ptr2)
            elif (ptr2 < len(s2) and s3[ptr1 + ptr2] == s2[ptr2]):
                res = backTrack(ptr1, ptr2 + 1)
            else:
                return False
            self.memo[(ptr1, ptr2)] = res
            return res
        a = backTrack(0, 0)
        return a
            