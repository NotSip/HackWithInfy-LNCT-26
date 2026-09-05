class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        subset = []
        nums = []

        for i in range(1,10):
            nums.append(i)


        def backtracking(idx,total):
            if len(subset) == k and total == n:
                res.append(subset.copy())
                return
            if idx >= len(nums):
                return
            if len(subset) > k or total > n:
                return
            
            subset.append(nums[idx])
            backtracking(idx+1,total+nums[idx])
            subset.pop()
            backtracking(idx+1,total)
           

        backtracking(0,0)
        return res  
            

            

        
        