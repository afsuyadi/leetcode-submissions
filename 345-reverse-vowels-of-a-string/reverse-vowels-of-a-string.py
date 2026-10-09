class Solution:
    def reverseVowels(self, strs: str) -> str:
        leftidx = 0
        leng = len(strs)
        s = []
        for e in strs:
            s.append(e)
        print(s)
        vowels = ['a', 'A', 'i', 'I', 'u', 'U', 'e', 'E', 'o', 'O']
        rightidx = leng - 1
        while leftidx < rightidx:
            # print('rightidx', rightidx)
            if s[leftidx] in vowels and s[rightidx] in vowels:
                s[leftidx], s[rightidx] = s[rightidx], s[leftidx]
                leftidx += 1
                rightidx -= 1
            elif s[leftidx] in vowels and s[rightidx] not in vowels:
                rightidx -= 1
            elif s[leftidx] not in vowels and s[rightidx] in vowels:
                leftidx += 1
            else:
                leftidx += 1
                rightidx -= 1
        res = ''.join(e for e in s)
        return res