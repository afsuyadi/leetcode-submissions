# two-pointer
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        result = []
        for word in words:
            reversedword = reversed(word)
            res = ''.join(word for word in reversedword)
            result.append(res)
        # print(result)
        return ' '.join(word for word in result)