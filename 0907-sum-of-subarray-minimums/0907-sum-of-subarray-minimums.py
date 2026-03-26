class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        MOD = 10**9+7
        pse = [-1]*n
        nse = [n]*n

        #Previous smaller element
        stack =[]
        for i in range(n):
            curr = arr[i]

            while stack and arr[stack[-1]] > curr:
                stack.pop()

            if stack:
                pse[i] = stack[-1]
            stack.append(i)

        #Next smaller element
        stack =[]
        for i in range(n-1,-1,-1):
            curr = arr[i]

            while stack and arr[stack[-1]] >= curr:
                stack.pop()

            if stack:
                nse[i] = stack[-1]
            stack.append(i)

        #Total sum
        total_sum = 0
        for i in range(n):
            left_dist = i - pse[i]
            right_dist = nse[i] - i

            contribution = (arr[i]*left_dist*right_dist)
            total_sum = (total_sum+contribution)%MOD

        return total_sum



        