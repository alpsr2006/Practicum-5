a = set()
p = input('Введите PIN-код: ')
if 1000 <= int(p) < 10000 and not(1900 <= int(p) <= 2050):
    a.add(p[0])
    a.add(p[1])
    a.add(p[2])
    a.add(p[3])
    if len(a) == 4:
            print('OK')
    else:
        print('ERROR')
else:
    print('ERROR')




