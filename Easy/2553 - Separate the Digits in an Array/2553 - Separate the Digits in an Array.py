class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        new = []

        for i in nums:
            for j in str(i):
                new.append(int(j))

        return new