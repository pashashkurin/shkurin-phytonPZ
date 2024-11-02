dict_week = {
    "Воскресенье": 0,
    "Понедельник": 1,
    "Вторник": 2,
    "Среда": 3,
    "Четверг": 4,
    "Пятница": 5,
    "Суббота": 6
}

dict_week_test = {
    0: "Среда",
    1: "Четверг",
    2: "Пятница",
    3: "Суббота",
    4: "Воскресенье",
    5: "Понедельник",
    6: "Вторник",
}

def func_test(number, dict_week_test):
    a = number % 7
    return dict_week[dict_week_test[a]]
print(func_test(365, dict_week_test))

