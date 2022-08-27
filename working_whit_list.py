# total = 0
# count = 0

# while True:
    # n = input('Enter a number: ')
    # if n == 'done':
        # break
    # value = float(n)
    # total += value
    # count += 1

# average = total / count
# print('Average: ', average)

# Another solution with creating an empty list.

num_list = list()

while True:
    n = input('Enter a number: ')
    if n == 'done':
        break
    value = float(n)
    num_list.append(value)

average = sum(num_list) / len(num_list)
print('Average: ', average)
