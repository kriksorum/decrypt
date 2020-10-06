def decrypt(key, text):
    keyLen = len(key)
    result = []
    while text != "":
        tmpStr = text[0:keyLen]
        arrStr = []
        arrKey = []

        for i in range(len(tmpStr)):
            arrStr.append(tmpStr[i])
        for i in range(len(key)):
            arrKey.append(key[i])

        arrKeyIndex = []
        sortKey = sorted(key)

        for i in range(len(key)):
            for j in range(len(key)):
                if key[i] == sortKey[j]:
                    arrKeyIndex.append(j)
        for i in range(len(arrKeyIndex)):
            #print(arrStr[arrKeyIndex[i]])
            result.append(arrStr[arrKeyIndex[i]])
        text = text[keyLen:]

    return ''.join(result)
print(decrypt("прибой", "ваакстфени_рисоранин_ява"))

"""
п р и б о й
5 6 2 1 4 3   


1 2 3 4 5 6 1 2 3 4 5 6 1 2 3 4 5 6 1 2 3 4 5 6 1 2 3 4 5 6
п р и б о й п р и б о й п р и б о й п р и б о й п р и б о й

1 2 3 4 5 6 | 1 2 3 4 5 6 | 1 2 3 4 5 6 | 1 2 3 4 5 6 
в а а к с т | ф е н и _ р | и с о р а н | и н _ я в а 
5 6 2 1 4 3 | 5 6 2 1 4 3 | 5 6 2 1 4 3 | 5 6 2 1 4 3 
с т а в к а | _ р е ф и н | а н с и р о | в а н и я _


"""