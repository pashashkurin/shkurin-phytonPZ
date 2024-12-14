'''
Даны четыре целых числа, одно из которых отлично от трех других, равных между
собой. Определить порядковый номер числа, отличного от остальных.
'''

numbers = []
for i in range(4):
    num = int(input(f"Введите число {i + 1}: "))
    numbers.append(num)

unique_index = -1

for i in range(4):

    if numbers[i] != numbers[(i + 1) % 4] and numbers[i] != numbers[(i + 2) % 4]:
        unique_index = i + 1  
        break

if unique_index != -1:
    print(f"Порядковый номер числа, отличного от остальных: {unique_index}")
else:
    print("Нет уникального числа.")
