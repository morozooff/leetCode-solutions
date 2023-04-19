

def convertToTitle(columnNumber):
    #create empty string
    title = ""
    #while n>0
    while columnNumber > 0:
        #minus one because symbs starts with 0
        columnNumber -= 1
        #find remain of divide
        c = columnNumber%26
        #find position in ascii
        ac = c + 65
        #take symb from ascii by posiyion
        elem = chr(ac)
        #add to title
        title = elem + title
        #new column num = whole part of divide
        columnNumber //= 26
    return title



print(convertToTitle(48053565))
print(convertToTitle(28))
print(convertToTitle(701))
print(convertToTitle(18253))
print(convertToTitle(52))
print(convertToTitle(879501))
