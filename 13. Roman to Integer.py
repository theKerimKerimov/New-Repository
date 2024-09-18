# Создаем словарь с символами в качестве ключей и числами в качестве значений
symbols = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

# Получаем значение по ключу
value = symbols["V"]
print(f"Значение для 'V': {value}")  # Вывод: Значение для 'V': 5


"""
IV - 4
IX - 9
XL - 40
XC - 90
CD - 400
CM - 900
"""

s = "LIV"
res = 0

for i in range(len(s)):
    if i + 1 < len(s) and symbols[s[i]] < symbols[s[i + 1]]:
        res -= symbols[s[i]]
    else:
        res += symbols[s[i]]

# print(len(s))
print(res)
