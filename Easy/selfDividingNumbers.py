class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        l = []
        for i in range(left, right + 1):
            is_div = 1
            for j in str(i):
                digit = int(j)
                if digit == 0 or i % digit != 0:
                    is_div = 0
                    break
            if is_div == 1:
                l.append(i)
        return l
