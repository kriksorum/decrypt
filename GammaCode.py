alphabeth = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя 0123456789"
def decrypt(code, gamma):
    codeLen = len(code)
    gammaLen = len(gamma)

    #Формируем ключевое слово(растягиваем гамму на длину текста)
    keyText = []
    for i in range(codeLen // gammaLen):
        for symb in gamma:
            keyText.append(symb)
    for i in range(codeLen % gammaLen):
        keyText.append(gamma[i])

    codeArr = []
    for i in range(len(code)):
        codeArr.append(code[i])
    print(codeArr)

    print(keyText)

    #Расшифровка
    text = []
    for i in range(codeLen):
        text.append(alphabeth[(alphabeth.index(code[i]) - alphabeth.index(keyText[i]) + len(alphabeth) - 1) % len(alphabeth)])

    return text

print(decrypt("т 05юцсызкёв5я2н", "восток"))









