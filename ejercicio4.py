import random

numbers = [0]*20
for i in range(len(numbers)):
    numbers[i] = random.randint(1, 10)

print(f' Normal: {numbers}')
numbers.reverse()
print(f' Inverted: {numbers}')