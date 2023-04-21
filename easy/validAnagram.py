def isAnagram(s, t) :
    first_word = {}
    for symb in s:
        if symb not in first_word:
            first_word[symb] = 1
        else:
            first_word[symb] += 1

    second_word = first_word.copy()
    for key in second_word:
        second_word[key] = 0

    for symb in t:
        if symb not in second_word:
            second_word[symb] = 1
        else:
            second_word[symb] += 1
    return first_word == second_word