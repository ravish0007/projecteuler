    

def four_consecutive_number_generator(start=0):
    local_number = start
    while True:
        yield [local_number, local_number + 1,
               local_number + 2, local_number + 3]


def get_factors(number):
    return []


def has_distinct_prime_factors(numbers):
    for each_number in numbers:
        factors = get_factors(each_number)

for numbers in four_consecutive_number_generator():
    if has_distinct_prime_factors(numbers):
        print(numbers)
        break
