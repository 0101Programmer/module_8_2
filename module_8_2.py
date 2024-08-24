def personal_sum(*numbers):
    incorrect_data = 0
    result = 0
    for num in numbers:
        try:
            result += num
        except TypeError:
            incorrect_data += 1
    return result, incorrect_data


def calculate_average(numbers):
    numbers_len = []
    try:
        for i in numbers:
            if isinstance(i, int):
                numbers_len.append(i)
    except TypeError:
        pass
    try:
        return personal_sum(*numbers)[0] / len(numbers_len)
    except ZeroDivisionError:
        return f'Деление на ноль! На ноль делить нельзя.'
    except TypeError:
        return 'Incorrect data type in <numbers>'


print(f'Результат 1: {calculate_average((5, 15, 10))}')
print(f'Результат 2: {calculate_average(())}')
print(f'Результат 3: {calculate_average(['1', '7', '2'])}')
print(f'Результат 4: {calculate_average(248)}')
print(f'Результат 5: {calculate_average(['buddy', 2, 4, 'melon', 6, 'farmer'])}')





