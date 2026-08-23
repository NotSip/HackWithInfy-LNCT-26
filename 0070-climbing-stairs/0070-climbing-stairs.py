class Solution:
    def climbStairs(self, n: int) -> int:

        dp = [-1]*(n+1)

        def ways(n,dp):
            if n == 0 or n == 1:
                return 1

            if dp[n] != -1:
                return dp[n]
            dp[n]= ways(n-1,dp) + ways(n-2,dp)
            return dp[n]
        return ways(n,dp)

# Memoization