class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        distinct = []
        strs = s
        leftidx = 0
        rightidx = leftidx
        max_len = 0
        for rightidx in range(len(strs)):
            while strs[rightidx] in distinct:
                distinct.pop(0)
                leftidx += 1
            if strs[rightidx] not in distinct:
                distinct.append(strs[rightidx])
                max_len = max(max_len, rightidx-leftidx+1)
                
            
        print('distinct=', distinct)
        # print('rightidx - leftidx', rightidx, leftidx)
        # return len(distinct)
        return max_len