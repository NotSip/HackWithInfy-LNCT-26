class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n = len(asteroids)
        stack = []
        for curr in asteroids:
            destroyed = False
            while stack and curr<0<stack[-1]:
                if abs(curr) > stack[-1]:
                    stack.pop()
                    continue
                elif abs(curr) == stack[-1]:
                    stack.pop()
                    destroyed = True
                else:
                    destroyed = True
                break
            if not destroyed:
                stack.append(curr)

        return stack
            

                

        