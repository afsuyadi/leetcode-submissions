# two-pointer
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sidx = 0
        tidx = 0
        counts = 0
        while sidx < len(s) and tidx < len(t):
            # print('sidx, tidx=', sidx, tidx)
            if s[sidx] == t[tidx]:
                counts += 1
                sidx += 1
                tidx += 1
            else:
                tidx += 1
        return True if counts == len(s) else False
                