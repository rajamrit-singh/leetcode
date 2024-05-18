class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            if (asteroid > 0):
                stack.append(asteroid)
            else:
                negativeAsteroidDestroyed = False
                while (not negativeAsteroidDestroyed and len(stack) > 0 and stack[-1] > 0):
                    if (stack[-1] > abs(asteroid)):
                        negativeAsteroidDestroyed = True
                    elif (stack[-1] < abs(asteroid)):
                        stack.pop()
                    else:
                        stack.pop()
                        negativeAsteroidDestroyed = True
                if ((not negativeAsteroidDestroyed) and(len(stack) == 0 or stack[-1] < 0)):
                    stack.append(asteroid)
                    
        return stack