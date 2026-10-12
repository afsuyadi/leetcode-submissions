# two-pointers
class Solution:
    def validPalindrome(self, s: str) -> bool:
        leftidx = 0
        failcount = 0
        rightidx = len(s) - 1
        def is_pal(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
                
        while leftidx < rightidx:
            # rightidx = len(s) - leftidx - 1
            if s[leftidx] != s[rightidx]:
                res = is_pal(leftidx+1, rightidx) or is_pal(leftidx, rightidx - 1)
                if res == True:
                    return True
                else:
                    return False
            leftidx += 1
            rightidx -= 1
            # rightidx -= 1
            # failcount += 1
            # if failcount > 1:
            #     return False
        return True 
