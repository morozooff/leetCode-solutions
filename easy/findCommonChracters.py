def commonChars(words):
    common = list(words[0])
    i = 1
    while i != len(words):
        result = []
        symb_list = list(words[i])
        for symb in symb_list:
            if symb in common:
                result.append(str(symb))
                common.remove(symb)
        i += 1
        common = result

    print(result)

words = ["bella","label","roller"]
commonChars(words)