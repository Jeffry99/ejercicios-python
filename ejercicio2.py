import random

numbers = [0]*20
for i in range(20):
    numbers[i] = random.randint(-100, 100)

def splitnumbers(list):
    even = []
    odd = []
    for num in list:
        if num%2 == 0:
            even.append(num)
        else:
            odd.append(num)

    print(f'All numbers: {numbers}')
    print(f'Odd numbers {odd}')
    print(f'Even numbers: {even}')

splitnumbers(numbers)
