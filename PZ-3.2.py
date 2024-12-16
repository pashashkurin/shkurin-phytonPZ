'''
Даны четыре целых числа, одно из которых отлично от трех других, равных между
собой. Определить порядковый номер числа, отличного от остальных.
'''

def find_unique_number_index(numbers):

    if len(numbers) != 4:
        raise ValueError("Должно быть ровно 4 числа")

    count = {}
    for number in numbers:
        count[number] = count.get(number, 0) + 1

    unique_number = None
    for number, cnt in count.items():
        if cnt == 1:
            unique_number = number
            break

    if unique_number is not None:
        return numbers.index(unique_number) + 1  
    else:
        return None  

numbers = [2, 2, 3, 2]
index = find_unique_number_index(numbers)
print(f"Порядковый номер отличающегося числа: {index}")
