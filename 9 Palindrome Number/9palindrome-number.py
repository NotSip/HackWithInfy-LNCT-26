class Solution:
    def isPalindrome(self, x: int) -> bool:
        orignal = x
        if x < 0 :
            return False
        if x == 0 :
            return True
        if x > 0 :
            result = 0
            while x > 0 :
                last_digit = x % 10
                result = (result*10) + last_digit
                x = x//10
            if result >(2**31 -1) or result < (-(2**31)):
                return False
            return result == orignal
            

        