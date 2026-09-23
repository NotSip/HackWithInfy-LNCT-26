class Solution:
    def maximumPoints(self, mat):
        n = len(mat)
        row = len(mat[0])
        col = len(mat)
        dp = [[-1 for _ in range(0,row+1)]for _ in range(0,col+1)]
        def func(idx,last):
            if idx == 0:
                maxi= 0
                for i in range(0,3):
                    if i!= last:
                        maxi = max(maxi,mat[idx][i])
                        dp[idx][i] = maxi
                return maxi
            if dp[idx][last]!=-1:
                return dp[idx][last]
            maxi = 0
            for i in range(0,3):
                if i!= last:
                    maxi = max(maxi,mat[idx][i]+func(idx-1,i))
    
            dp[idx][last] = maxi
            return dp[idx][last]        
        return func(n-1,3)