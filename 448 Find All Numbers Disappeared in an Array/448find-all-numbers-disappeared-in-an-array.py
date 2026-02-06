class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        hash_map={key:0 for key in range(1,n+1)}
        diss_element=[]
        for i in nums:
            if i not in hash_map:
                hash_map[i]=1
            else:
                hash_map[i]+=1

        for i,j in hash_map.items():
            if j == 0:
                diss_element.append(i)
        return diss_element

        

        