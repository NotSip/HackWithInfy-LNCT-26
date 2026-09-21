class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        def helper(arr):
            k = len(arr)
            dp = [-1]*n
            def chori(idx):
                if dp[idx] != -1:
                    return dp[idx]

                if idx == 0:
                    return arr[idx]
                if idx < 0:
                    return 0
                adj1 = chori(idx-2)+arr[idx]
                adj2 = chori(idx-1)

                dp[idx] = max(adj1,adj2)
                return dp[idx]
            return chori(k-1)


        part_1 = helper(nums[:n-1])
        part_2 = helper(nums[1:])

        return max(part_1,part_2)
        