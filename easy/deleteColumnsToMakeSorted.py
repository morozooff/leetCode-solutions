def minDeletionSize(strs):

    counter = 0
    new_strs = []
    for i in range(len(strs[1])):
        str_elem = ""
        for string in strs:
            str_elem = str_elem + string[i]
        new_strs.append(str_elem)

    print(new_strs)
    for string in new_strs:
        for i in range(len(string) - 1):
            if string[i] > string[i + 1]:
                counter += 1
                break
            else:
                pass

    return counter

strs = ["cba","daf","ghi"]
print(minDeletionSize(strs))
