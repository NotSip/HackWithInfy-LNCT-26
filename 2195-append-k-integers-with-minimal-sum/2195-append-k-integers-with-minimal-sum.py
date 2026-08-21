class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:

        unique_nums = sorted(set(nums))

        for i in unique_nums:
            if i <= k:
                k+=1
            else:
                break

        total_sum =int(k*(k+1)/2)

        for i in unique_nums:
            if i <=k:
                total_sum-=i

            else:
                break

        return total_sum
        
            
        