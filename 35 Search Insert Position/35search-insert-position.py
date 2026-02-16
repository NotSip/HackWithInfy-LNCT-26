class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        lb = n
        high = n-1
        low = 0

        while low <= high:
            mid = (low + high)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                low = mid + 1
            if nums[mid] > target:
                high = mid - 1
                lb = mid

        return lb
        