class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i: i[0])
        print(intervals)
        myArr = [intervals[0]]
        for start, end in intervals[1::]:
            curEnd = myArr[-1][1]
            if (start <= curEnd):
                myArr[-1][1] = max(myArr[-1][1], end)
            else:
                myArr.append([start, end])
        return myArr