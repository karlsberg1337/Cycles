n = int(input())
e = 0
while n > 0:
    d = n % 10
    if d % 2 == 0:
        e += d
    n //= 10
print(e)
