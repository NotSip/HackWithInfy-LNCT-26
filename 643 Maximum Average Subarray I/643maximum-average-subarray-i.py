class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        win_sum = 0
        max_sum = float("-inf")
        l = 0
        n = len(nums)

        for i in range(0, n):
            win_sum += nums[i]
            if i - l + 1 == k:
                max_sum = max(win_sum, max_sum)
                win_sum -= nums[l]
                l += 1
        return max_sum/k
            