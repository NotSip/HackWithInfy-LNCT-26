class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)

        prefix = [0]*n

        prefix[0] = nums[0]

        for i in range(1,n):
            prefix[i] = nums[i] + prefix [i-1]

        for i in range(n):
            left_sum = 0 if i == 0 else prefix[i-1]
            right_sum = prefix[n-1] - prefix[i]

            if left_sum == right_sum:
                return i

        return -1