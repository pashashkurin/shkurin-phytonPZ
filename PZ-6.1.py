'''
В30
Дан целочисленный список размера N. Увеличить все четные числа, содержащиеся
в списке, на исходное значение первого четного числа. Если четные числа в списке
отсутствуют, то оставить список без изменений.
'''


def increase_even_numbers(lst):
    
    first_even = next((x for x in lst if x % 2 == 0), None)

  
    if first_even is not None:
        lst = [x + first_even if x % 2 == 0 else x for x in lst]
    
    return lst

N = 10
lst = [1, 3, 5, 2, 4, 6, 7, 8, 9, 10]
result = increase_even_numbers(lst)
print(result)
