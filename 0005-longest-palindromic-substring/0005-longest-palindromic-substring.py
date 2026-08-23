class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        max_length = 0

        def expand(l,r):
            while l>=0 and r<len(s) and s[l] == s[r]:
                l-=1
                r+=1

            return r-l-1

        for i in range(len(s)):
            odd = expand(i,i)
            even = expand(i,i+1)

            curr_max = max(odd,even)
            if curr_max > max_length:
                max_length=curr_max
                start = i-(curr_max-1)//2

        return s[start:start+max_length]