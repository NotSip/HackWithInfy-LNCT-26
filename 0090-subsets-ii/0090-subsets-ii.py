class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []
        nums.sort()
        def backtrack(idx):
            result.append(subset.copy())
            for i in range(idx,len(nums)):
                if i>idx and nums[i] == nums[i-1]:
                    continue

                subset.append(nums[i])
                backtrack(i+1)
                subset.pop()
            
        backtrack(0)
        return result