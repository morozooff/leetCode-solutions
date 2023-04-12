def isPalindrome( s: str) -> bool:
    low = s.lower()
    new = [i for i in low if i.isalnum()]
    print(new)
    return new == new[::-1]