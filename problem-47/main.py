import itertools

def some_functionality(number1, number2, number3, number4):
    pass

def four_consecutive_number_generator(start=0):
    local_number = start
    while True:
        yield [local_number, local_number + 1,
               local_number + 2, local_number + 3]
        local_number += 1

for first_number, second_number, third_number, fourth_number in four_consecutive_number_generator():
    print(first_number, second_number, third_number, fourth_number)
   
