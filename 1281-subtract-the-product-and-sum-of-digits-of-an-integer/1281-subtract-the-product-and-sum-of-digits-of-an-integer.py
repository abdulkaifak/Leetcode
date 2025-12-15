class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum = 0
        prod = 1

        for ch in str(n):
            d = int(ch)
            sum += d
            prod*= d

        return prod - sum