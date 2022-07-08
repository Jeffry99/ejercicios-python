numbers1 = [1, 2, 4, -6, -8, 3, 1, 8, -10, -20, -40]
numbers2 = [5, 4, 2, -7, -1, 2, -9, 10, -64, 12, -1]

def change_negatives(list):
    for i in range(len(list)):
        if list[i] < 0:
            list[i] = 0


print(f'Before: {numbers1}')
change_negatives(numbers1)
print(f'After: {numbers1}')