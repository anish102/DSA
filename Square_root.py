'''Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.'''


class Solution:
    def mySqrt(self, x: int):
        if x == 0:
            return 0
        left, right = 1, x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
        return right
