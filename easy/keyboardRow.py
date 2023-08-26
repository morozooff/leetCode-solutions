def findWords(words):
    keyboard = {
        'first': ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
        'second': ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
        'third': ['z', 'x', 'c', 'v', 'b', 'n', 'm']
    }
    result_words = []

    def check(word):
        word = word.lower()
        result = [0, 0, 0]
        for symb in word:
            if symb in keyboard['first']:
                result[0] += 1
            elif symb in keyboard['second']:
                result[1] += 1
            elif symb in keyboard['third']:
                result[2] += 1
        return len(word) in result

    for word in words:
        if check(word):
            result_words.append(word)

    return result_words