class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        #hashmap for course and its dependencies
        depCrs = {i: [] for i in range(0, numCourses)}
        #visited set to keep track of loops
        visited = set()
        for crs, pre in prerequisites:
            depCrs[crs].append(pre)
        
        def dfs(crs):

            # If the course doesn't have any dependency, then we can complete
            # that course
            if (len(depCrs[crs]) == 0):
                return True
            # if we already visited the node, that means there's a loop so
            # not possible to complete courses
            if crs in visited:
                # print('here')
                return False
            visited.add(crs)
            for course in depCrs[crs]:
                # print(course)
                # print(depCrs)
                if (not dfs(course)):
                    return False
                # dfs(course)
            depCrs[crs] = []
            return True
        
        for c in range(0, numCourses):
            if (dfs(c) == False):
                return False
        return True