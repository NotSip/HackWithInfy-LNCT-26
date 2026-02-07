class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        s=sorted(nums)
        dict_1={}
        for i , v in enumerate(s):
            if v not in dict_1:
                dict_1[v]=i
        
        returning=[]
        for i in nums:
            returning.append(dict_1[i])

        return returning
        