import random

numbers = [0]*10
for i in range(len(numbers)):
    numbers[i] = random.randint(-10, 10)

def sumaEnt(list):
    suma = 0
    for num in list:
        suma += num

    return suma

print(f'List: {numbers}')
print(f'Result: {sumaEnt(numbers)}')