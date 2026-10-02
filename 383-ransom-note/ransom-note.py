class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # ====
        # if ransomNote can be constructed from magazine?
        ransomdict = {}
        for ran in ransomNote:
            ransomdict[ran] = ransomdict.get(ran, 0) + 1
        magazinedict = {}
        for mag in magazine:
            magazinedict[mag] = magazinedict.get(mag, 0) + 1
        
        for key, count in ransomdict.items():
            if key not in magazine:
                return False
            if key in magazine and count > magazinedict[key]:
                return False
        return True
            