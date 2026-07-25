class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        window = []
        l = 0
        maximum = 0
        count = 0

        for r in range(len(nums)):
            
            if nums[r] == 1:
                window.append(nums[r])
            else:
                window.append(nums[r])
                count +=1

            while count>k:
                x = window.pop(0)
                l+=1

                if x == 0:
                    count -= 1
            maximum = max(maximum,len(window))


        return maximum
        