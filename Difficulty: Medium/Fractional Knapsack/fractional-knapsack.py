class Solution:
    def fractionalKnapsack(self, val, wt, capacity):
        ratio = []
        n = len(val)
        cost = 0.0
        
        for i in range(n):
            ratio.append((val[i],wt[i],val[i]/wt[i]))
            
        ratio.sort(key= lambda x: x[2],reverse = True)
        
        for r in ratio:
            price = r[0]
            weight = r[1]
            per_gram =r[2] 
            if weight <= capacity:
                capacity = capacity - weight
                cost += price
                
            else:
                rat = capacity/weight
                cost += (rat*price)
                capacity = 0
                
                
        return cost