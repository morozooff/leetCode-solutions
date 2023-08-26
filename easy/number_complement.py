def findComplement(num):
    pretranc = format(num, 'b')
    postranc = ''
    for i in pretranc:
        if i == '0':
            postranc += '1'
        elif i == '1':
            postranc += '0'
    return int(postranc, 2)