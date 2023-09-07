class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if (len(s1) + len(s2) != len(s3)):
            return False
        dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
        dp[len(s1)][len(s2)] = True
        print(dp)
        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                print(i)
                print(j)
                print('****************')
                if(i < len(s1) and s3[i + j] == s1[i] and dp[i + 1][j]):
                    dp[i][j] = True
                # if (i == 1 and j == 0):
                #     print(s3[i+j])
                #     print(s2[j])
                #     print(dp[i][j+1])
                if (j < len(s2) and s3[i + j] == s2[j] and dp[i][j+1]):
                    dp[i][j] = True
        return dp[0][0]