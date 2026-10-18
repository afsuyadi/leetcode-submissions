class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        slist = []
        for i in s:
            slist.append(i)
        
        left = 0
        right = len(slist) - 1
        while left < right:
            if not slist[left].isalpha():
                left += 1
            elif not slist[right].isalpha():
                right -= 1
            else:
                slist[left], slist[right] = slist[right], slist[left]
                left += 1
                right -= 1
        
        return ''.join(slist)