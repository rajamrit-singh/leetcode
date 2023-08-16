class Solution:

    def __init__(self):
        self.count = 0
        self.hashTable = {}

    def numDecodings(self, s: str) -> int:
        leftPtr = 0
        rightPtr = 0
        if(s[0] == '0'):
            return 0
        if(len(s) == 1):
            return 1
        self.dfs(s)
        return self.hashTable[s]

    def dfs(self, string):
        if (self.hashTable.get(string)):
            return self.hashTable[string]
        if(string == ""):
            self.count += 1
            return 1
        if(string[0] == '0'):
            return 0
        else:
            count1 = self.dfs(string[1::])
        if (len(string) > 1 and self.isValid(string[0:2])):
            count2 = self.dfs(string[2::])
        else:
            count2 = 0
        self.hashTable[string] = count1 + count2
        return count1 + count2

    def isValid(self, string):
        if(string[0] and string[0] == '0'):
            return False
        num = int(string)
        if (num > 0 and num <=26):
            return True
        return False