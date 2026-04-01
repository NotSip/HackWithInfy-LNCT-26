class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        lb = -1
        ub = -1
        low = 0
        high = n-1
        res=[]

        def first_pos(nums,lb,low,high,target):
            while low<=high:
                mid = (low+high)//2
                if nums[mid]==target:
                    lb = mid
                    high = mid-1
                elif nums[mid]>target:
                    high = mid-1
                else:
                    low = mid+1
            return lb
        def last_pos(nums,ub,low,high,target):
            while low<=high:
                mid = (low+high)//2
                if nums[mid] > target:
                    high = mid-1
                elif nums[mid] == target:
                    ub = mid
                    low = mid+1
                else:
                    low = mid+1
            return ub
        res.append(first_pos(nums,lb,low,high,target))
        res.append(last_pos(nums,ub,low,high,target))

        return res

        