total = 0
count = 0

while True:
    n = input('Enter a number: ')
    if n == 'done':
        break
    value = float(n)
    total += value
    count += 1

average = total / count
print('Average: ', average)
