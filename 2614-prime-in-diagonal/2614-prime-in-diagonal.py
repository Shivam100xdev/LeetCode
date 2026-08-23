class Solution:
    def diagonalPrime(self, nums):
        def isPrime(x):
            if x < 2:
                return False
            if x % 2 == 0:
                return x == 2
            i = 3
            while i * i <= x:
                if x % i == 0:
                    return False
                i += 2
            return True

        n = len(nums)
        ans = 0
        for i in range(n):
            if isPrime(nums[i][i]):
                ans = max(ans, nums[i][i])
            if isPrime(nums[i][n - i - 1]):
                ans = max(ans, nums[i][n - i - 1])
        return ans
