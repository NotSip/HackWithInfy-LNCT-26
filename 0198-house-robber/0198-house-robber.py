class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        dp = [-1]*(n+1)

        def chori(dp,n):
            if n == 0:
                return nums[n]
            if n < 0:
                return 0

            if dp[n]!=-1:
                return dp[n]

            pick = nums[n]+chori(dp,n-2)
            not_pick = chori(dp,n-1)
            dp[n] = max(pick,not_pick)
            return dp[n]
        return chori(dp,n-1)

        # Memoization