class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # split s
        words = s.split()
        
        # map s; order matters
        mapped = {}
        if len(pattern) != len(words):
            return False
        for i, word in enumerate(words):
            
            pat = pattern[i]
            val = mapped.get(pat, None)
            if val == None and word not in mapped.values(): # means that val is still empty
                mapped[pat] = word
            elif val == word: # means that there is value, CHECK IT!
                continue
            elif val != word:
                return False
        print(mapped)
        return True