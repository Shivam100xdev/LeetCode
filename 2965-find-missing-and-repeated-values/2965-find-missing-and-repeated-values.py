class Solution:
    def findMissingAndRepeatedValues(self, grid):
        n = len(grid)
        count = [0] * (n * n + 1)
        for row in grid:
            for num in row:
                count[num] += 1
        ans = [0, 0]
        for i in range(1, n * n + 1):
            if count[i] == 2:
                ans[0] = i
            elif count[i] == 0:
                ans[1] = i
        return ans
