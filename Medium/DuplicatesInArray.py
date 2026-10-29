class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        d = {}
        a = []
        for i in nums:
            if i in d:
                d[i] = d[i]+1
            else:
                d[i] = 1
        for i in d:
            if d[i] != 1:
                a.append(i)
        return a
