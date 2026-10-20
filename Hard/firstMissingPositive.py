class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        s = set(nums)

        for i in range(1, n + 2):
            if i not in s:
                return i
