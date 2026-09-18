class Solution:
    def minCost(self, height: list[int]) -> int:
        if len(height)==0 or len(height)==1:
            return 0
        p1 = 0
        p2= abs(height[0]-height[1])
        
        for i in range(2,len(height)):
            cost = min((p1+abs(height[i]-height[i-2])),(p2+abs(height[i]-height[i-1])))
            
            p1=p2
            p2= cost
        
        return p2
            
            