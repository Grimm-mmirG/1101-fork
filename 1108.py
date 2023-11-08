with open('one_hundred.txt', 'r') as file:
    numbers = file.read().split()
numbers = [int(num) for num in numbers if num.isdigit()]
missing_numbers = [num for num in range(1, 101) if num not in numbers]
print (f'{missing_numbers} are the values missing')
numbers.sort()
with open('one_hundred_sorted.txt', 'w') as file:
    for num in numbers:
        file.write(str(num) + '\n')
