def isPalindrome(self, x):
    string = str(x)[::-1]
    if string == str(x):
        return True
    else:
        return False