class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        while low < high:
            mid = low + (high-low)//2
            total_hour = 0
            for i in piles:
                total_hour += (i+mid-1)//mid
            if total_hour <= h:
                high = mid
            else:
                low = mid+1

        return low


        