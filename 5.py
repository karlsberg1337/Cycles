N = int(input())
a, b = 0, 1
for _ in range(N):
    print(a, end=' ')
    ne = a + b
    a = b
    b = ne
