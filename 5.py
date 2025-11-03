ves = float(input('введите Ваш вес (кг.): '))
h = float(input('введите Ваш рост (м.): '))
if ves < 0 or ves > 500 or h < 0 or h > 3:
    print('oшибочные входные данные')
else:
    IMT = ves / h ** 2
    IMT = round(IMT,2)
    if IMT < 16: print('выраженный дефицит массы тела')
    elif 16 <= IMT < 18.49: print('недостаточная масса тела')
    elif 18.5 <= IMT < 24.99: print('норма')
    elif 25 <= IMT < 29.99: print('избыточная масса тела')
    elif 30 <= IMT < 34.99: print('ожирение первой степени')
    elif 35 <= IMT < 39.99: print('ожирение второй степени')
    else: print('ожирение третьей степени')