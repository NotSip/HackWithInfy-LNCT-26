class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        seen = {}
        count = 0

        for i in range(len(nums)):
            total += nums[i]

            if total == k:
                count+=1

            if (total-k) in seen:
                count += seen[total-k]

            seen[total] = seen.get(total,0)+1

        return count 




        