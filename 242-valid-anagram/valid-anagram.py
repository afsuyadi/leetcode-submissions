class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict = {}
        tdict = {}
        ss = s
        ts = t
        for s in ss:
            sdict[s] = sdict.get(s, 0) + 1
        
        for t in ts:
            tdict[t] = tdict.get(t, 0) + 1
            
        if sdict == tdict:
            return True
        print("sdict=", sdict)
        print("tdict=", tdict)
        return False