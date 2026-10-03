class Solution:
    def firstUniqChar(self, s: str) -> int:
        # slowidx = 0
        # fastidx = slowidx + 1
        # notunique = []
        # if len(s) == 1:
        #     return 0
        
        # while slowidx < len(s):
        #     print('FASTIDX: ', fastidx)
        #     if s[slowidx] == s[fastidx] or s[slowidx] in notunique:
        #         slowidx += 1
        #         fastidx = slowidx + 1
        #         notunique.append(s[slowidx])
        #     else:
        #         fastidx += 1
        #         if fastidx == len(s):
        #             print('FASTIDX, SLOWIDX', fastidx, slowidx)
        #             return slowidx
        # return -1
        counter= {}
        for val in s:
            counter[val] = counter.get(val, 0) + 1
        
        for i, val in enumerate(s):
            if counter[val] == 1:
                return i
        
        return -1