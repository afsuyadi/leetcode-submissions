class Solution:
    def isValid(self, s: str) -> bool:
        couple = {
            "(": ")", "[": "]", "{": "}", ")": "(", "]": "[", "}": "{"
        }
        openers = ["(", "{", "["]
        stack = []
        # for bracket in s:
        #     if not stack and bracket in openers:
        #         stack.append(bracket)
        #     elif not stack and bracket not in openers: # ex: "}"
        #         return False
        #     else:                
        #         if bracket == couple[stack[-1]]:
        #             print('stack:', stack)
        #             print('bracket"s couple:', couple[bracket])
        #             stack.pop(-1)
        #         else: 
        #             # stack.append(bracket)
        #             return False
        for current_bracket in s:
            if current_bracket in openers: # it's an OPENING parentheses
                if stack: # There is something in Stack
                    if current_bracket == couple[stack[-1]]:
                        stack.pop(-1)
                    else:
                        stack.append(current_bracket)
                else: # Stack is EMPTY
                    stack.append(current_bracket)
                    
            else: # it's a CLOSING parentheses
                if not stack: # stack is empty
                    return False
                else: # there is something in Stack
                    if current_bracket == couple[stack[-1]]:
                        stack.pop(-1)
                    else:
                        return False
        if not stack:
            return True
        print(stack)
        return False