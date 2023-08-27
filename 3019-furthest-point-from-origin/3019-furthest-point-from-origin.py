class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        """
        :type moves: str
        :rtype: int
        """
        count_L = 0
        count_R = 0
        count = 0
        for move in moves:
            # print(move)
            if (move == 'L'):
                count_L += 1
            if (move == 'R'):
                count_R += 1
            if (move == '_'):
                count += 1
        # print(count)
        # print(count_L)
        # print(count_R)
        return count + abs(count_L - count_R)