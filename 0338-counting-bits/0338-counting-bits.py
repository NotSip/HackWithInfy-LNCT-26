class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for i in range(n+1):
            count = 0
            while i:
                count+= i%2
                i//=2

            output.append(count)
        return output