class Solution(object):
    def numberOfBoomerangs(self, points):
        ans = 0

        for x1, y1 in points:
            dist = {}

            for x2, y2 in points:
                d = (x1 - x2) ** 2 + (y1 - y2) ** 2
                dist[d] = dist.get(d, 0) + 1

            for count in dist.values():
                ans += count * (count - 1)

        return ans