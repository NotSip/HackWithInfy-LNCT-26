class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        temp = nums.copy()
        max_=float("-inf")
        max__=float("-inf")
        for i in temp:
            max_=max(max_,i)
        temp.remove(max_)
        for j in temp:
            max__=max(max__,j)

        return (max_-1)*(max__-1)

        