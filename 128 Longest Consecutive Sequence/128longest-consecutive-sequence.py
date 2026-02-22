class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        my_set=set(nums)
        max_length=float("-inf")
        
        for i in my_set:
            if i-1 not in my_set:
                curr = i
                length = 1
                
                while curr+1 in my_set:
                    curr+=1
                    length+=1

                max_length=max(length,max_length)
        return max_length