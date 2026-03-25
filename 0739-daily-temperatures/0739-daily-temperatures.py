class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0]*n
        stack = []
        for i in range(n):
            curr = temperatures[i]
            while stack:
                if temperatures[i] > temperatures[stack[-1]]:
                    last_index = stack.pop()
                    ans[last_index] = i - last_index
                else:
                    break
            stack.append(i)
        return ans


        