class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = ""
        palindrome=False
        for i in s:
            if i.isalnum():
                a += i
        a=a.lower()
        k = a[-1::-1]
        if a == k:
            palindrome = True
        return palindrome


        
        

        