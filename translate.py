# sendict = {'NP':['N','D'],'VP':['V','V.NP']}
def dickeys(dictionary):
    dictkeys = list(dictionary.keys())
    for i in dictkeys:
        if i == 'N':
            dictkeysN = list(dictionary[i].keys())
        elif i == 'V':
            dictkeysV = list(dictionary[i].keys())
        elif i == 'NP':
            dictkeysNP = list(dictionary[i].keys())
        elif i == 'VP':
            dictkeysVP = list(dictionary[i].keys())
        elif i == 'D':
            dictkeysD = list(dictionary[i].keys())
        elif i == 'A':
            dictkeysA = list(dictionary[i].keys())
    return dictkeysN, dictkeysV, dictkeysNP, dictkeysVP, dictkeysD, dictkeysA


def comparator(sentence, dictionary):
    dictkeys = list(dictionary.keys())
    datacomp = []
    sentencelisted = sentence.split()
    dictkeysN, dictkeysV, dictkeysNP, dictkeysVP, dictkeysD, dictkeysA = dickeys(dictionary)
    dictionkeys = [dictkeysN, dictkeysV, dictkeysNP, dictkeysVP, dictkeysD, dictkeysA]
    diclen = len(dictionkeys)

    for i in sentencelisted:
        for k in range(diclen):
            if i in dictionkeys[k]:
                for x in range(diclen):
                    if i in dictionary[dictkeys[x]]:
                        val1 = dictionary[dictkeys[x]][i]
                        val = [val1, dictkeys[x]]
                        datacomp.append(val)
                    else:
                        error = 'Word Not in Dictionary'
            else:
                error = 'Part of Speech or Word Not in Dictionary'
    return datacomp, error


def translator(data):
    result = ''
    for i in range(len(data)):
        if i < len(data) - 1:
            if 'D' in data[i] and 'N' in data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
            elif 'A' in data[i] and 'N' in data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
            elif 'D' in data[i] and (len(data) > (i + 2) and 'A' in data[i + 1]) and (
                    len(data) > (i + 2) and 'N' in data[i + 2]):
                data[i], data[i + 1], data[i + 2] = data[i + 2], data[i + 1], data[i]
            else:
                pass
    for i in data:
        result += i[0] + ' '
    return result


if __name__ == "__main__":
    sentence = 'the girl is here'
    sentence = sentence.lower()
    diction = {'NP': {1: 'N', 2: 'D'},
               'VP': {1: 'V', 2: 'V.NP'},
               'V': {'play': 'sere', 'cut': 'ge', 'grow': 'gbi', 'is': 'n', 'bought': 'ra'},
               'N': {'boy': 'omokunrin', 'tree': 'igi', 'fruit': 'eso', 'cloth': 'aso', 'girl': 'omobinrin'},
               'D': {'the': 'naa', 'a': 'kan', 'an': 'kan'},
               'A': {'white': 'funfun', 'black': 'dudu'}
               }
    data, error = comparator(sentence, diction)
    if not len(data):
        print(error)
    else:
        print(translator(data))
