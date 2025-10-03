class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j in range (i+1,len(nums)):
            if nums[j] != nums[i]:
                i +=1
                nums[i],nums[j] = nums[j],nums[i]
        k = i+1
        return k



        