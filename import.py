
def add_numbers(a, b):
    sum = a + b
    return sum


def is_even(number):
    
    return number % 2 == 0


def calculate_discount(price, discount_percentage):
    Nprice = (price) * (discount_percentage / 100)
    mprice = price - Nprice
    return mprice