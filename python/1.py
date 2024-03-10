def convert_special_to_good(input_string):
    def convert_number(number_str):
        parts = number_str.split('\\')
        if len(parts) != 2:
            return number_str  # Не является особенным номером
        first_part = parts[0].zfill(4)
        second_part = parts[1].zfill(5)
        return f"{first_part}\\{second_part}"

    output_numbers = []
    parts = input_string.split()
    for part in parts:
        if '\\' in part:
            output_numbers.append(convert_number(part))
    return '\n'.join(output_numbers)

# Пример использования
input_str = "Адрес 5467\\456. Номер 405\\549"
output_str = convert_special_to_good(input_str)
print(output_str)
