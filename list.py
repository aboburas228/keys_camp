def get_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]


def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num


def find_min(numbers):
    min_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num


def custom_sort(numbers):
    sorted_numbers = numbers.copy()
    for i in range(len(sorted_numbers)):
        for j in range(i + 1, len(sorted_numbers)):
            if sorted_numbers[i] > sorted_numbers[j]:
                sorted_numbers[i], sorted_numbers[j] = sorted_numbers[j], sorted_numbers[i]
    return sorted_numbers

input_str = input("Введите список чисел: ")
numbers = [int(num.strip()) for num in input_str.split(',')]
even_numbers = get_even_numbers(numbers)
max_num = find_max(numbers)
min_num = find_min(numbers)
sorted_numbers = custom_sort(numbers)

print(f"Четные числа: {even_numbers}")
print(f"Максимальное число: {max_num}")
print(f"Минимальное число: {min_num}")
print(f"Отсортированный список: {sorted_numbers}")
