a = int(input())
if (a % 10 == a // 1000) and ((a%1000)//100 == (a % 100) // 10):
    print('Настоящее')
else:
    print('Кривое')
