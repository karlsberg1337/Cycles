n = int(input())
d = 0
di = 1
while n > 0:
    dig = n % 10
    d += dig
    di *= dig
    n //= 10
print("Сумма:", d)
print("Произведение:", di)
