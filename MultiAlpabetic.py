alpha = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
def decrypt(key, text):
    result = []
    space = 0
    for index, ch in enumerate(text):
        if ch != ' ':
            cj = alpha.index(ch) #индекс буквы текста в алфавите
            kj = alpha.index(key[(index - space) % len(key)]) #индекст буквы ключа в алфавите
            mj = (cj - kj) % len(alpha) #получаем индекст буквы из исходного текста
            result.append(alpha[mj])
            print(alpha[mj])
        else:
            space += 1
            result.append(' ')
    return ''.join(result)
print(decrypt("прибой", "брт иощпяцсачсрутн шяю шбххэъшпэчтюмйрбвоща эчтюмф еыэ фивй"))

#так зарапортавался
"""
а б в г д е ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я
п р с т у ф х ц ч ш щ ъ ы ь э ю я а б в г д е ж з и й к л м н о
р с т у ф х ц ч ш щ ъ ы ь э ю я а б в г д е ж з и й к л м н о п
и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я а б в г д е ж з 
б в г д е ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я а
о п р с т у ф х ц ч ш щ ъ ы ь э ю я а б в г д е ж з и й к л м н
й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я а б в г д е ж з и
"""