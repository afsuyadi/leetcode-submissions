class Solution:
    def romanToInt(self, s: str) -> int:
        dictionary = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        idx = 0
        result = 0
        max_length = len(s)
        for letter in s:      
            # print(letter)         
            # print(result) 
            if idx+1 == max_length:
                current_value = dictionary[letter]
                result = result + current_value
                break
            current_value = dictionary[letter]
            next_value = dictionary[s[idx+1]]
            if current_value < next_value: # ex: "IV", which means 1 and 5
                result = result - current_value
            else:
                result = result + current_value
            idx += 1
        
        return result