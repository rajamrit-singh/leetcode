class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        sol = []
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        if (digits == ""):
            return []
        def backTrack(i, cur):
            if (len(cur) == len(digits)):
                sol.append(cur)
                return
            for num in mapping[digits[i]]:
                backTrack(i + 1, cur + num)
        backTrack(0, "")
        return sol
