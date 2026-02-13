class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        my_set = set()
        for i in range(0,len(nums)):
            if nums[i] in my_set:
                return True
            if nums[i] not in my_set:
                my_set.add(nums[i])
            if len(my_set)>k:
                my_set.remove(nums[i-k])

        return False
        