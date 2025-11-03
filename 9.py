b1,b2,b3 = map(int, input('Введите высоты трёх башен: ').split())
bmax = max(b1, b2, b3)
bmin = min(b1, b2, b3)
bsr = (b1 + b2 + b3) - bmax - bmin
print(bmax, bsr, bmin)


