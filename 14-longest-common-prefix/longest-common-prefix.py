from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        idx = -1
        count = 0
        pointer = 0
        # is_similar = 0
        for letter in strs[0]: # F, L, O, W, E, R
            is_similar = 0
            for str in strs: # F, L, O, W
                # F VS FLOW
                if pointer >= len(str): # quit loop if pointer exceeds str's length.
                    break
                # print(letter, str[pointer])
                if letter != str[pointer]: # quit loop if there is any unsimilar letter.
                    print("break", letter,str[pointer])
                    break
                else:
                    is_similar += 1
            if is_similar == len(strs): # check is number of similar letters equal to strs' length
                idx += 1 # assign the similat letter's index
            else:
                print("not the same", is_similar)
                break
            pointer += 1 # points at what index we are comparing.
        # print(idx)
        if idx == -1:
            return ""
        print(idx)
        return strs[0][:idx+1]