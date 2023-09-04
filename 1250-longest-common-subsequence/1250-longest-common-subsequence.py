class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1 = len(text1)
        len2 = len(text2)
        dp = [[0] * (len2 + 1) for i in range(0, len1 + 1)]
        for i in range(len1 - 1, -1, -1):
            for j in range(len2 - 1, -1, -1):
                if(text1[i] == text2[j]):
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
        print(dp)
        return dp[0][0]
