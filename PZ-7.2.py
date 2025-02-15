'''
Дана строка, состоящая из русских слов, набранных заглавными буквами и
разделенных пробелами (одним или несколькими). Найти количество слов, которые
начинаются и заканчиваются одной и той же буквой.
'''

def count_same_start_end_words(s):
    
    words = s.split()
    
  count = 0
    
    for word in words:
        
        if word and word[0] == word[-1]:
            count += 1
    
    return count

s = "МАМА РАД АННА ШАЛАШ ПРИВЕТ"
result = count_same_start_end_words(s)
print(result)  
