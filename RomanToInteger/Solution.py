class Solution:

    mapping = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    def romanToInt(self, s: str) -> int:
        numerals = []
        str_reversed = [char for char in s]
        while len(str_reversed) != 0:
            char = str_reversed.pop()
            offset = 0
            if (len(str_reversed) > 0):
                if ((char == "V" or char == "X") and str_reversed[-1] == "I"):
                    str_reversed.pop()
                    offset = -1
                elif ((char == "L" or char == "C") and str_reversed[-1] == "X"):
                    str_reversed.pop()
                    offset = -10
                elif ((char == "D" or char == "M") and str_reversed[-1] == "C"):
                    str_reversed.pop()
                    offset = -100
                else:
                    pass
            numerals.append(self.mapping.get(char, 0) + offset)
        return sum(numerals)
