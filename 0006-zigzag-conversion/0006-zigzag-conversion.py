class Solution:
    def convert(self, s: str, numRows: int) -> str:
        length = len(s)
        if (numRows  == 1):
            return s
        if (numRows == 2):
            pass
        n = length
        crossColSize = numRows - 2
        cols = 0
        counter = 0
        while (n > 0):
            if (counter % 2 == 0):
                n -= numRows
                cols += 1
                counter += 1
            else:
                n -= crossColSize
                cols += crossColSize
                counter -= 1
        matrix = [[0] * cols for i in range(0, numRows)]
        reversed = False
        j = 0
        k = 0
        i = 0
        # print(length)
        while (k < length):
            # print(i)
            # print(j)
            # print('kkkkkkkkkkkkk')
            # print(k)
            matrix[i][j] = s[k]
            k += 1

            if (reversed):
                i -= 1
                j += 1
            else:
                i += 1
            if (i == numRows):
                reversed = True
                i -= 2
                j += 1
            if (i == 0):
                reversed = False
        answer = ""
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if (matrix[i][j] != 0):
                    answer += matrix[i][j]
        return answer