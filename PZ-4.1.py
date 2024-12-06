N = int(input("Введите целое число N (>0): "))

result = sum(((-1) ** (i + 1)) * (i + 1) for i in range(N))

print(f"Значение выражения: {result}")
