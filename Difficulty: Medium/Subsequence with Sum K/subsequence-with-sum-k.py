class Solution:
    def checkSubsequenceSum(self, arr, k):
        result = []
        subset = []
        def backtracking(idx,total,result,subset):
            if total == k:
                #result.append(subset.copy())
                return True
            elif total>k:
                return False
            if idx >= len(arr):
                return False
            
            subset.append(arr[idx])
            if backtracking(idx+1,total+arr[idx],result,subset):
                return True
            subset.pop()
            if backtracking(idx+1,total,result,subset):
                return True
        
        e = backtracking(0,0,result,subset)
                
        return e
        