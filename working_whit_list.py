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
max_number = max(num_list)
min_number = min(num_list)
print('Max number is: ', max_number)
print('Min number is: ', min_number)
print('Average: ', average)
