class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hash_map={}
        res=[]

        for i in nums:
            if i not in hash_map:
                hash_map[i]=1
            else:
                hash_map[i]+=1

        for j,v in hash_map.items():
            if v >= 2:
                res.append(j)

        return res