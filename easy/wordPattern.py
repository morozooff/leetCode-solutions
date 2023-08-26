
def wordPattern(pattern, s):
    pattern_sequence = {}
    lstr = s.split()
    if len(pattern) != len(lstr):
        return False
    for i in range(len(pattern)):
        if pattern[i] not in pattern_sequence.keys() and lstr[i] not in pattern_sequence.values():
            pattern_sequence[pattern[i]] = lstr[i]
            print(pattern_sequence)
        else:
            if lstr[i] == pattern_sequence.get(pattern[i]):
                continue
            else:
                return False

    return True