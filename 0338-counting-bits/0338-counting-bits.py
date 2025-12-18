class Solution:
    def countBits(self, n: int) -> List[int]:
        a = []
        for i in range(0,n+1):
            a.append(bin(i).count("1"))
        return a