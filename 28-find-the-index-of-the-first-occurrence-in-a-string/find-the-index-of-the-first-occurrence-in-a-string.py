#two-pointers

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        hayidx = 0
        needidx = 0
        start = 0
        while hayidx < len(haystack) and needidx < len(needle):
            if haystack[hayidx] == needle[needidx]:
                hayidx += 1
                needidx += 1
            else:
                start += 1
                hayidx = start
                needidx = 0
        return start if needidx == len(needle) else -1