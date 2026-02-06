class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        output=[]
        """hash_map={}
        for i in nums:
            if i not in hash_map:
                hash_map[i]=1
            else:
                hash_map[i]+=1"""
        for i in range(0,n):
            remainder = target-nums[i]
            for j in range(i+1,n):
                if nums[j] > remainder and remainder > 0:
                    break
                if nums[i]+nums[j]==target:
                    output.append(i)
                    output.append(j)
                    return output

                
                


        
        