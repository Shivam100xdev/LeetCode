class Solution(object):
    def countBinarySubstrings(self, s):
        left = 0
        ans = 0

        while left < len(s):
            mid = left

            while mid < len(s) and s[mid] == s[left]:
                mid += 1

            right = mid

            while right < len(s) and s[right] == s[mid]:
                right += 1

            ans += min(mid - left, right - mid)
            left = mid

        return ans