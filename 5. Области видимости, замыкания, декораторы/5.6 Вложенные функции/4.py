def double_odd_numbers(numbers):
    def double(num):
        return num * 2
    
    def is_odd(num):
        return num % 2 == 1

    return [double(num) for num in numbers if is_odd(num)]
