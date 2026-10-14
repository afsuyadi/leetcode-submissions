class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        n = len(s)
        answer = [0] * n

        # left-to-right: distance from most recent c seen so far
        prev = float('-inf')
        for i in range(n):
            if s[i] == c:
                prev = i
            answer[i] = i - prev

        # right-to-left: distance from next c seen so far
        prev = float('inf')
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                prev = i
            answer[i] = min(answer[i], prev - i)

        return answer