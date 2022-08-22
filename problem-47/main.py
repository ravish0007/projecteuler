import itertools

def some_functionality(number1, number2, number3, number4):
    pass

for number in itertools.count():
    if some_functionality(number):
        print(number)
        break
