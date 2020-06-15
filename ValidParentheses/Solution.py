class Solution:

    pairs = {
        "(" : ")" ,
        "[" : "]" ,
        "{" : "}" 
    }

    def isValid(self, s: str) -> bool:
        remaining_stack = list(s)
        processed_stack = []
        while len(remaining_stack) > 0:
            current_char = remaining_stack.pop()
            if len(processed_stack) > 0 and self.pairs.get(current_char) == processed_stack[-1]:
                processed_stack.pop()
            else:
                processed_stack.append(current_char)
        if len(processed_stack) == 0:
            return True
        else:
            return False