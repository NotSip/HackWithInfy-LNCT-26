class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=len(nums)
        l=0
        r=n-1
        while l < r:
            if nums[r] == val:
                r-=1
            elif nums[l] == val:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
            elif nums[l] != val:
                l+=1
        k=0
        for i in nums:
            if i != val:
                k+=1
        return k


        


        