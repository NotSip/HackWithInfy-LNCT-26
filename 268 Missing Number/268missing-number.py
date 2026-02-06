class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        my_hashmap={key:0 for key in range(n+1)}
        for i in nums:
            if i not in my_hashmap:
                my_hashmap[i]=1
            else:
                my_hashmap[i]+=1

        for i,j in my_hashmap.items():
            if j == 0:
                return i 

        