class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sidx = len(s) - 1
        tidx = len(t) - 1
        skips = 0
        skipt = 0

        while sidx >= 0 or tidx >= 0:
            # advance sidx until it lands on a surviving character (or runs out)
            while sidx >= 0:
                if s[sidx] == '#':
                    skips += 1
                    sidx -= 1
                elif skips > 0:
                    skips -= 1
                    sidx -= 1
                else:
                    break

            # advance tidx until it lands on a surviving character (or runs out)
            while tidx >= 0:
                if t[tidx] == '#':
                    skipt += 1
                    tidx -= 1
                elif skipt > 0:
                    skipt -= 1
                    tidx -= 1
                else:
                    break

            if sidx >= 0 and tidx >= 0:
                if s[sidx] != t[tidx]:
                    return False
            elif sidx >= 0 or tidx >= 0:
                # one string still has a surviving character, the other doesn't
                return False

            sidx -= 1
            tidx -= 1

        return True
        