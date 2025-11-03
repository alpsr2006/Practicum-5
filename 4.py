n = int(input("Введите число от 1 до 100: "))
if n < 1 or n > 100:
    print("Число должно быть от 1 до 100")
else:
    l = n % 10
    l2 = n % 100
    if l2 >= 11 and l2 <= 14:
        print(f"{n} попугаев")
    else:
        if l == 1:
            print(f"{n} попугай")
        elif l >= 2 and l <= 4:
            print(f"{n} попугая")
        else:
            print(f"{n} попугаев")

