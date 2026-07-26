class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        if sum(nums) < target:
            return 0
        l = 0
        minimum = float("inf")
        curr_sum = 0

        for  r in range(len(nums)):
            curr_sum += nums[r]

            while curr_sum >= target:
                minimum = min(minimum,r-l+1)
                curr_sum -= nums[l]
                l+=1 

                      
        if minimum == float("inf"):
            return 0
        else:
            return minimum
            

        