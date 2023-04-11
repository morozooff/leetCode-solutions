def longestCommonPrefix(strs):
    res = ""
    for a in zip(*strs):
        if len(set(a)) == 1:
            res += a[0]
        else:
            return res
    return res


strs = ["flower", "flow", "flight"]
print(longestCommonPrefix(strs))