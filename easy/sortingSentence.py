import re
def sortSentence(s: str) -> str:
    corr = {}

    def default(sentence):
        result = re.sub(r'/d+', '', sentence)
        return result

    new_sentence = ''
    new_s = s.split(' ')
    for word in new_s:
        if word[len(word) - 1] in corr.keys():
            return default(s)
        else:
            corr[int(word[len(word) - 1])] = word[0:len(word) - 1]

    print(corr)
    for i in range(10):
        if i in corr.keys():
            new_sentence += corr[i] + ' '

    return new_sentence.strip()


s = "is2 sentence4 This1 a3"
print(sortSentence(s))