class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        import copy
        arr.sort()
        n=len(arr)
        result = []
        min_diff=float('inf')
        for i in range(1,n):
            min_diff = min(min_diff,arr[i]-arr[i-1])
        
        for i in range(1,n):
            if arr[i]-arr[i-1]==min_diff:
                result.append([arr[i-1],arr[i]])

        return result
            
            