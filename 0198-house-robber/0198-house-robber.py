class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1]*n
        def chori(idx):
            if dp[idx] != -1:
                return dp[idx]

            if idx == 0:
                return nums[idx]
            if idx < 0:
                return 0
            adj1 = chori(idx-2)+nums[idx]
            adj2 = chori(idx-1)

            dp[idx] = max(adj1,adj2)
            return dp[idx]


        return chori(n-1)
        