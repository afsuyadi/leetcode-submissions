class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sdict = {}
        # tdict = {}
        # ex. tdict = {
        #     "p": "t",
        #     "a": "i",
        #     "e": "l",
        #     "r": "e",
        # }
        idx = 0
        for char in s:
            res = sdict.get(char, 0)
            print("IDX: ", idx)
            if res != 0 and t[idx] != sdict[char]: # means that there is an existing value for that key, which is prohibited.
                print("CHAR, RES:", char, res)
                return False
            else:
                sdict[char] = t[idx]
            idx += 1
        
        sdict = {}
        idx = 0
        for char in t:
                    res = sdict.get(char, 0)
                    print("IDX: ", idx)
                    if res != 0 and s[idx] != sdict[char]: # means that there is an existing value for that key, which is prohibited.
                        print("CHAR, RES:", char, res)
                        return False
                    else:
                        sdict[char] = s[idx]
                    idx += 1
        print("SDICT:", sdict)
        return True
    