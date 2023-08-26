class Solution:
    def maxPower(self, s: str) -> int:
        substrings_with_repeated_symbols = []
        current_symbol = ''
        substrings_with_repeated_symbols.append([current_symbol])
        i = 0

        for symbol in s:
            if symbol == current_symbol:
                substrings_with_repeated_symbols[i].append(symbol)
            else:
                i += 1
                current_symbol = symbol
                substrings_with_repeated_symbols.append([current_symbol])

        substrings_lenght = [len(substring) for substring in substrings_with_repeated_symbols]

        return max(substrings_lenght)