def isBadVersion(version):
    # Its false API that know bad/good version and evaluate input version
    # return True if input is bad version, False if input is good version
    # this API realized in Leetcodes tests, its doesn't work in my cod
    return True

def firstBadVersion(self, n: int) -> int:
    start = 1
    end = n
    while start <= end:
        print("-----")
        middle = (start + end) // 2
        print(middle)
        decision = isBadVersion(middle)
        print(decision)
        if not decision:
            start = middle + 1
            print(start)
        if decision:
            n = middle
            end = middle - 1
            print(end)
    return n