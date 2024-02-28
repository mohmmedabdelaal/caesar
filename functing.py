# height = int(input('Please enter the height of the can'))
# width = int(input('Please enter the width of the can'))
# coverage = 38


# def get_can_coverage(height, width, coverage):
#     can = (height * width) / coverage
#     return round(can)


# can_coverage = get_can_coverage(height, width, coverage)
# print(can_coverage)

# prime number
prime = int(input('Enter a prime number'))


def is_prime_number(number):
    if number < 2:
        return False  # Numbers less than 2 are not prime

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False  # Number is divisible by a factor other than 1 and itself

    return 'number is prime'  # Number is prime


print(is_prime_number(4))
