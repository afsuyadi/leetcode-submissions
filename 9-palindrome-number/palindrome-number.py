class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            x_string = '-' + str(x)
        else:
            x_string = str(x)
        length = len(x_string)
        end_idx = length-1
        for letter in x_string[:length//2]:
            print(letter, x_string[length-1])
            
            if letter == x_string[end_idx]:
                # print(letter, x_string[length-1])
                end_idx -= 1
                continue
            else: 
                return False
        return True  