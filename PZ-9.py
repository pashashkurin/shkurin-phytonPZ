'''
В30
Сгенерировать словарь вида {0: 0, 1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216},
удалить из него первый и последний элементы. Отобразить исходный и
получившийся словарь. Использовать for, range.
'''


original_dict = {i: i**3 for i in range(7)}

keys = list(original_dict.keys()) 
if keys:  
    del original_dict[keys[0]]  
    del original_dict[keys[-1]] 

print("Исходный словарь:", {i: i**3 for i in range(7)})
print("Получившийся словарь:", original_dict)
