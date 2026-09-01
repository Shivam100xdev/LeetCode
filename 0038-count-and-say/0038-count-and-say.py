class Solution:
    def countAndSay(self, n):
        s = "1"
        for _ in range(n - 1):
            res, count, prev = "", 1, s[0]
            for c in s[1:]:
                if c == prev:
                    count += 1
                else:
                    res += str(count) + prev
                    prev, count = c, 1
            res += str(count) + prev
            s = res
        return s
