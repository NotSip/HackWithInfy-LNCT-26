class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prod = 1
        k = 0
        hash_map = {}
        res = []
        more_zero = False

        for j in nums:
            hash_map[j] = hash_map.get(j,0)+1

        if len(hash_map) == 1 and nums[0] == 0:
            for z in range(n):
                res.append(0)

            return res

        for i,v in hash_map.items():
            if i == 0 and v > 1:
                more_zero = True

        if more_zero == True:
            for k in range(n):
                res.append(0)
            return res
                

        else:

            if k in hash_map:
                for i in nums:
                    if i!=0:
                        prod*=i
                for j in nums:
                    if j!=0:
                        res.append(0)
                    else:
                        res.append(prod)
            else:
                for i in nums:
                    prod *=i
                for j in nums:
                    res.append(prod//j)


        return res
            


        