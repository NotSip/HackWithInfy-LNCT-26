class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        substring =""
        def backtracking(substring,open_count,close_count):
            if open_count == close_count == n:
                result.append(substring)
                return

            if open_count<n:
                backtracking(substring+"(",open_count+1,close_count)
            if close_count<open_count:
                backtracking(substring+")",open_count,close_count+1)
        
        

        backtracking(substring,0,0)

        return result