import pymongo
from pymongo import MongoClient


def dickeys(dictionary):
    dictkeys = list(dictionary.keys())
    dictionlist = []
    for i in dictkeys:
        if i != "u_id":
            dictkeysN = list(dictionary[i].keys())
            dictionlist.append(dictkeysN)

    return dictionlist


def comparator(sentence, dictionary):
    error = ''
    dictkeys = list(dictionary.keys())
    datacomp = []
    sentencelisted = sentence.split()
    dictionkeys = dickeys(dictionary)
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
    client = MongoClient('mongodb://mt:general@ds123193.mlab.com:23193/mt')
    diction = client.mt.diction.find_one({}, {'_id': False})
    sentence = 'I hate that boy'
    sentence = sentence.lower()
    data, error = comparator(sentence, diction)
    if not len(data):
        print(error)
    else:
        print(translator(data))
