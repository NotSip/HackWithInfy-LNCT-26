class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])

        removal = 0
        prev_end = float("-inf")

        for start,end in intervals:
            if start >= prev_end:
                prev_end = end

            else:
                removal +=1

        return removal
        