import heapq
class Solution:
   def minCost(self, arr):
    heapq.heapify(arr)
    
    total_cost = 0
    
    while len(arr) > 1:
        first = heapq.heappop(arr)
        second = heapq.heappop(arr)
        
        current_cost = first+second
        total_cost += current_cost
        
        heapq.heappush(arr,current_cost)
        
    return total_cost