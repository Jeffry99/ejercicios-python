import random
import sys

numbers = [0]*20
differences = [0]*20

for i in range(len(numbers)):
    numbers[i] = random.randint(-100, 100)

for i in range(len(numbers)):
        differences[i] = numbers[0] - numbers[i]

for i in range(len(differences)):
    if(differences[i] < 0):
        differences[i] *= -1

for i in range(len(differences)):
    if(differences[i] == 0):
        differences[i] = sys.maxsize

dif = min(differences)
closest = numbers[differences.index(dif)]

print(f'Numbers: {numbers}')
print(f'Closest number: {closest}')
