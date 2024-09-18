strs = ["flower", "flow", "flight"]

res = ""

for i in range(len(strs[0])):
    # print(f"Цикл, на котором происходит перебор символа: {i}")
    # print(f"Длина первого слова: {list(range(len(strs[0])))}")
    for s in strs:
        # print(f"Длина каждого слова: {len(s)}")
        if i == len(s) or s[i] != strs[0][i]:
            print(f"Ответ: {res}")
            exit()
    res += strs[0][i]
