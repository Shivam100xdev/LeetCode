class Solution(object):
    def maximalSquare(self, matrix):
        if not matrix:
            return 0

        cols = len(matrix[0])
        dp = [0] * (cols + 1)
        largest = 0

        for row in matrix:
            diagonal = 1

            for j in range(1, cols + 1):
                top = dp[j]

                if row[j - 1] == '1':
                    dp[j] = min(dp[j], dp[j - 1], diagonal) + 1
                    largest = max(largest, dp[j])
                else:
                    dp[j] = 0

                diagonal = top

        return largest * largest
