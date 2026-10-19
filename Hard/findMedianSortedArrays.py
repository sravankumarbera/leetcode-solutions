
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        a = nums1 + nums2
        a.sort()
        n = len(a)

        if n % 2 != 0:
            return float(a[n // 2])
        else:
            return (a[n // 2 - 1] + a[n // 2]) / 2
