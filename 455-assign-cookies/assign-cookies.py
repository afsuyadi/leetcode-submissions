class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        childidx = 0
        cookieidx = 0
        count = 0
        while childidx < len(g) and cookieidx < len(s):
            if s[cookieidx] >= g[childidx]:
                count += 1
                childidx += 1
            cookieidx += 1
        return count
