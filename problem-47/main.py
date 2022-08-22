import math  

def four_consecutive_number_generator(start=0):
    local_number = start
    while True:
        yield [local_number, local_number + 1,
               local_number + 2, local_number + 3]
        local_number += 1

# Hello problem-3, doesn't work for 0, 1 
def get_prime_factors(number):
    prime_factors = []

    while number % 2 == 0:
        number = number / 2
        prime_factors.append(2)
         
    for index in range(3, int(math.sqrt(number)) + 1, 2):
        while number % index == 0:
            prime_factors.append(index)
            number = number / index

    if number > 2:
        prime_factors.append(number)

    return prime_factors

def has_distinct_prime_factors(numbers, length):
    for each_number in numbers:
        factors = get_prime_factors(each_number)
        if len(set(factors)) != length:  # distinct, final piece
            return False
    return True


for numbers in four_consecutive_number_generator(start=1):
    print('processing: ', *numbers, flush=True)
    if has_distinct_prime_factors(numbers, length=4):
        print(numbers)
        break
