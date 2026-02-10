class Solution:
    from collections import deque
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res=collections.deque()

        l=0
        r=(len(nums)-1)

        left_value=0
        right_value=0

        while l<=r:
            left_value=abs(nums[l])
            right_value=abs(nums[r])
            if left_value > right_value:
                res.appendleft(left_value*left_value)
                l+=1
            else:
                res.appendleft(right_value*right_value)
                r-=1
        return list(res)


