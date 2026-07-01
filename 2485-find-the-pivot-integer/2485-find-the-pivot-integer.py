import math

class Solution:
    def pivotInteger(self, n: int) -> int:
        pivot = math.sqrt(n * (n + 1) / 2)
        if pivot.is_integer():
            return int(pivot)
        else:
            return -1


