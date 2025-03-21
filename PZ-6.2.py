'''
Дан список A размера N. Сформировать новый список B того же размера по
следующему правилу: элемент BK равен сумме элементов списка A с номерами от 1
до K.
'''


def create_list_b(A):
    B = []
    current_sum = 0
    
    for i in range(len(A)):
        current_sum += A[i]  
        B.append(current_sum)  
    
    return B

N = 5
A = [1, 2, 3, 4, 5]
B = create_list_b(A)
print(B)
