class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        subset = []
        def backtracking(idx,curr_sum):
            if curr_sum == target:
                result.append(subset.copy())
                return

            if curr_sum > target or idx == len(candidates):
                return

            subset.append(candidates[idx])
            backtracking(idx,curr_sum+candidates[idx])
            subset.pop()
            backtracking(idx+1,curr_sum)

        backtracking(0,0)

        return result

        