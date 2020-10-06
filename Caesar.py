s = "нцуфсжлрнжецп"
n = 3
alpha = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
print(len(alpha))
res = ''
for c in s:
    res += alpha[(alpha.index(c) - n) % len(alpha)]
print('Result: "' + res + '"')