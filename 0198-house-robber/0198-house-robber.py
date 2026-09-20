class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1]*n
        dp[0] = nums[0]

        for i in range(1,n):
            if i > 1:
                pick = nums[i] + dp[i-2]
            else:
                pick = nums[i]

            not_pick = dp[i-1]

            dp[i] = max(pick,not_pick)


        return dp[-1]
        