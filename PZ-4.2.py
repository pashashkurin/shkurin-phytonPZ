N = int(input("Введите целое число N (>0): "))

has_two = False

while N > 0:
    if N % 10 == 2: 
        has_two = True
        break  
    N //= 10  
print(has_two)
