class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        ptr_q = 0
        ptr_pat = 0
        result = [False for i in range(0, len(queries))]
        for index, string in enumerate(queries):
            ptr_pat = 0
            isValid = True

            for i in range(0, len(string)):

                print(ptr_pat)
                if(ptr_pat < len(pattern) and string[i] == pattern[ptr_pat]):
                    ptr_pat += 1
                elif ((string[i].isupper())):
                    isValid = False
                    break
            if (isValid and ptr_pat == len(pattern)):
                result[index] = True
            
        print(result)
        return result
