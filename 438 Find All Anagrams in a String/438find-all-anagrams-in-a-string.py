class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ns = len(s)
        np = len(p)
        if np > ns:
            return []
        p_count = [0]*26
        s_count = [0]*26
        res = []

        for i in range(np):
            p_count[ord(p[i])-ord('a')]+=1
            s_count[ord(s[i])-ord('a')]+=1

        for i in range(np,ns):
            if s_count == p_count:
                res.append(i-np)
            s_count[ord(s[i]) - ord('a')] += 1
            s_count[ord(s[i - np]) - ord('a')] -= 1
        if s_count == p_count:
            res.append(ns-np)      
                    
        return res


        