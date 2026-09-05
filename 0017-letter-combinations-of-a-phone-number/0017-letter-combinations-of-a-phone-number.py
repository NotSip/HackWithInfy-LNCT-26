class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        hash_map={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}

        res = []
        def backtrack(idx,string):
            if idx == len(digits):
                res.append(string)
                return

            curr = digits[idx]
            curr_str = hash_map[curr]

            for s in curr_str:
                backtrack(idx+1,string+s)

        backtrack(0,"")
        return res