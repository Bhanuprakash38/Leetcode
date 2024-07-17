class Solution:
    lut = {
        2: "abc",
        3: "def",
        4: "ghi",
        5: "jkl",
        6: "mno",
        7: "pqrs",
        8: "tuv",
        9: "wxyz"
    }

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        sequences = [[''] for _ in range(len(digits))]

        for index, char in enumerate(digits):
            try:
                num = int(char)
                if num < 2 or num > 9:
                    return []

                if index == 0:
                    sequences[index] = [char for char in self.lut[num]]
                else:
                    # list(chain.from_iterable()) flattens a list of list into a list
                    sequences[index] = list(chain.from_iterable(self.append_num(string, num) for string in sequences[index - 1]))
            except ValueError:
                return []

        return sequences[-1]

    def append_num(self, seq: str, num: int) -> List[str]:
        return [seq + char for char in self.lut[num]]
        