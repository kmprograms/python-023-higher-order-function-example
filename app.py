from typing import Callable

# Napisz program, w którym zliczysz, ile liczb parzystych
# znajduje się w przykładowej liście liczb całkowitych.

def count_even_numbers(numbers: list[int]) -> int:
    return len([number for number in numbers if number % 2 == 0])

def count_numbers(numbers: list[int], condition_fn: Callable[[int], bool]) -> int:
    return len([number for number in numbers if condition_fn(number)])

if __name__ == '__main__':
    numbers = [21, 34, 22, 45, 11, 76]
    print(count_even_numbers(numbers))
    print(count_numbers(numbers, lambda n: n % 2 == 0))
    print(count_numbers(numbers, lambda n: n % 3 == 0))
    print(count_numbers(numbers, lambda n: n > 10))

