class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        count_p = 0
        count_n=0
        max_ = 0

        for i in nums:
            if i > 0 :
                count_p+=1
            if i < 0 :
                count_n+=1

        max_ = max(count_p,count_n)

        return max_
        