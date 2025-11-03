knats = int(input("Введите количество кнатов: "))
galleons = knats // (17 * 29)
knats %= (17 * 29)
sickles = knats // 29
knats %= 29
result = []
if galleons > 0:
    result.append(f"{galleons} галлеонов")
if sickles > 0:
    result.append(f"{sickles} сиклей")
if knats > 0:
    result.append(f"{knats} кнатов")
print(" \n".join(result))



