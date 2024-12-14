'''
Вариант 30
Дни недели пронумерованы следующим образом: 0 - воскресенье, 1
﻿﻿понедельник, 2 — вторник, . . ., 6 — суббота. Дано целое число К, лежащее в диапазоне 1-365. 
Определить номер дня недели для К-го дня года, если известно, что в этом году 1 января было четвергом.
'''

def day_of_week(K):
    start_day = 4

    day_number = (start_day + (K - 1)) % 7

    return day_number

K = int(input("Введите номер дня года (1-365): "))
if 1 <= K <= 365:
    print(f"Номер дня недели для {K}-го дня года: {day_of_week(K)}")
else:
    print("Ошибка: K должно быть в диапазоне от 1 до 365.")
