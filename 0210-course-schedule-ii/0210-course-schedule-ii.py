class Solution(object):

    def __init__(self):
        self.loopFound = False
    def findOrder(self, numCourses, prerequisites):
        result = []
        resultSet = set()
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        done = set()
        prereq = {i : [] for i in range(0, numCourses)}
        for [course, pre] in prerequisites:
            prereq[course].append(pre)
        print(prereq)
        def dfs(course):
            if (len(prereq[course]) == 0):
                if (course not in resultSet):
                    result.append(course)
                    resultSet.add(course)
                return

            if (course in done):
                self.loopFound = True
                return

            done.add(course)
            for i in prereq[course]:
                dfs(i)
            prereq[course] = []
            if (course not in resultSet):
                result.append(course)
                resultSet.add(course)
        
        for i in range(0, numCourses):
            dfs(i)
        if (self.loopFound):
            return []
        print(result)
        return result