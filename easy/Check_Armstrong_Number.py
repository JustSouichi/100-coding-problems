def is_armstrong(number):
    sum_of_digits = sum(int(digit)**len(str(number)) for digit in str(number))
    return sum_of_digits == number

