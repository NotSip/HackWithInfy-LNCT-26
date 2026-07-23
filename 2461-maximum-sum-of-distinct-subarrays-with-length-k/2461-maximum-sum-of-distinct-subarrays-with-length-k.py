class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        l = 0
        subarray = []
        maximum = 0
        sum_subarray = 0
        freq ={}
        for r in range(len(nums)):
            num = nums[r]
            sum_subarray += num
            freq[num] = freq.get(num,0)+1

            if (r-l+1) == k:
                if len(freq) == k:
                    maximum = max(sum_subarray,maximum)
                left_num = nums[l]
                sum_subarray -= left_num
                freq[left_num] -=1
                if freq[left_num] == 0:
                    del freq[left_num]
                l+=1 

            
            
        return maximum
