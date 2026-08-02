class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        rem_count = {0:1}
        total_sum = 0
        count = 0

        for num in nums:
            total_sum+=num
            rem = total_sum%k

            if rem in rem_count:
                count+=rem_count[rem]

            rem_count[rem] = rem_count.get(rem,0)+1

        return count