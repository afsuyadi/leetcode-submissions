class Solution:
    def isPalindrome(self, s: str) -> bool:
        leng = len(s)
        idx = 0
        if leng == 1:
            return True
        strs = ''.join(c for c in s.lower() if c.isalnum())
        # print(strs)
        while idx < len(strs)/2:
            
            backidx = len(strs) - idx - 1
            # print('strs[idx] VS strs[backidx]=', strs[idx], strs[backidx])
            if strs[idx] != strs[backidx]:
                return False
            idx += 1
        return True
            
