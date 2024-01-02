class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myArr = []
        result = {}
        for string in strs:
            res = ''.join(sorted(string))
            myArr.append(res)
        for index, val in enumerate(myArr):
            if (result.get(val)):
                result[val].append(strs[index])
            else:
                result[val] = [strs[index]]
        return list(result.values())
