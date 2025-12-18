class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a = b = 0
        for n in nums:
            a, b = max(a, n), max(b, min(a, n))
        return (a - 1) * (b - 1)