def max_concatenated_number(str_list):
    # Сортируем строки в порядке обратном лексикографическому
    sorted_list = sorted(str_list, key=lambda x: x * 3, reverse=True)
    # Объединяем строки в одну строку
    concatenated_number = ''.join(sorted_list)
    return concatenated_number

# Пример использования
input_list = ['41', '4', '005', '89']
result = max_concatenated_number(input_list)
print(result)
