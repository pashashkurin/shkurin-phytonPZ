def sum_natural_numbers(n):
    return sum(range(1, n + 1))

n = int(input("Введите N: "))
result = sum_natural_numbers(n)
print(f"Сумма первых {n} натуральных чисел: {result}")
