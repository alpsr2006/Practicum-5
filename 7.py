N, K, M = map(int, input().split())
c= (M - K - 1) % N
c1 = (K - M - 1) % N
result = min(c, c1)
print(result)


