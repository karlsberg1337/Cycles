b = int(input()) # базовое число 
e = int(input()) # показатель степени 
r = 1 # хранит результат возведения в степень 
for _ in range(e): # for для повторения 
    r *= b # итерации он умножает текущее значение на r и bобновляет значение r
print(r) # печатает значение r
