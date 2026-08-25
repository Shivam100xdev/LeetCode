class Solution:
    def mySqrt(self, x):
        if x == 0 or x == 1:
            return x
        left, right = 1, x
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            if square == x:
                return mid
            if square < x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans
