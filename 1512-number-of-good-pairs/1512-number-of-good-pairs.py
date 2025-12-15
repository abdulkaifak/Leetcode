class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return int(sum(((n-1)*n/2) for n in Counter(nums).values()))