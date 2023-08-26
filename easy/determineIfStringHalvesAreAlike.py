import re

def halvesAreAlike(s: str) -> bool:
    def vowelsInString(string):
        vowels = re.findall(r'[EUIOAaeiou]', string, flags = re.ASCII)
        num_of_vowels = len(vowels)
        return num_of_vowels

    def halve(string):
        halfs = []
        halfs.append(string[0:len(string)//2])
        halfs.append(string[len(string)//2:len(string)])
        return halfs

    halfs = halve(s)
    vowels_in_first_half = vowelsInString(halfs[0])
    vowels_in_second_half = vowelsInString(halfs[1])
    return vowels_in_first_half == vowels_in_second_half
