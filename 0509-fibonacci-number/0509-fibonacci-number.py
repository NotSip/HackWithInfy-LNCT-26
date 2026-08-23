class Solution:
    def fib(self, n: int) -> int:
        dp = [-1]*(n+1)
        def fibonacci(dp,n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            if dp[n]!=-1:
                return dp[n]
            dp[n]= fibonacci(dp,n-1)+fibonacci(dp,n-2)

            return dp[n]

        return fibonacci(dp,n)