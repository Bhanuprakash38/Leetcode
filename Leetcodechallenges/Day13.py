class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string_digit = ""
        for digit in digits:
            string_digit = string_digit + str(digit)
        digit_int = int(string_digit) + 1
        string_digit = str(digit_int)
        result = []
        for s in string_digit:
            result.append(int(s))
        return result