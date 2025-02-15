'''
В30
Даны строки S и S0. Проверить, содержится ли строка S0 в строке S. Если содержится,
то вывести TRUE, если не содержится, то вывести FALSE.
'''

def check_substring(S, S0):
    
    if S0 in S:
        return True
    else:
        return False


S = "Hello, world!"
S0 = "world"
result = check_substring(S, S0)
print(result)  
