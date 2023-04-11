def strStr(haystack, needle):
    if needle not in haystack:
        return -1
    else:
        return haystack.find(needle)


haystack = "sadbutsad"
needle = "sad"
print(strStr(haystack, needle))