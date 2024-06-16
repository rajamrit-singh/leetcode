class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char = {}
        i = 0
        j = 0
        curMax = 0
        while (j < len(s)):
            if (s[j] in char):
                char[s[j]] += 1
            else:
                char[s[j]] = 1
            while((j - i + 1) - max(char.values())>  k):
                char[s[i]] -= 1
                i += 1
            curMax = max(curMax, j - i + 1)
            j += 1
        return curMax
    