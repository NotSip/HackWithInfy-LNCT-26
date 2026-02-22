class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map={}
        n=len(nums)
        for i in nums:
            if i not in hash_map:
                hash_map[i]=1
            else:
                hash_map[i]+=1
        for i,v in hash_map.items():
            if v > (n/2):
                return i
        