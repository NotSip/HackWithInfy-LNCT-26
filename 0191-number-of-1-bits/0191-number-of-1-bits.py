class Solution:
    def hammingWeight(self, n: int) -> int:
        num = n
        count = 0
        while num:
            count+= num%2
            num//=2

        return count
        