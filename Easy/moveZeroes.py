class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        c = nums.count(0)

        nums[:] = [i for i in nums if i != 0] + [0] * c
