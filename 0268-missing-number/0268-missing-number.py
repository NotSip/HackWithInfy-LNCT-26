class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n  = len(nums)
        compare =[]
        for i in range(n+1):
            compare.append(i)
        compare.extend(nums)
        res = 0
        for num in compare:
            res ^= num

        return res
