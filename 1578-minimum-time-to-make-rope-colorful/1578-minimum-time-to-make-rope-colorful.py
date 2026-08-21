class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total_cost = 0
        current_time = 0
        for i in range(len(colors)):

            if i > 0 and colors[i] != colors[i-1]:
                current_time = 0

            total_cost += min(current_time,neededTime[i])
            current_time = max(current_time,neededTime[i])
        return total_cost

            