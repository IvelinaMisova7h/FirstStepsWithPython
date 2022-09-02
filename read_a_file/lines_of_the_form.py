import re
# file_name = input('Enter a file name: ')
file_handle = open('mbox-short.txt')

lst = list()
for line in file_handle:
    line = line.rstrip()
    num = re.findall('^New Revision: ([0-9.]+)', line)
    if len(num) > 0:
        for number in num:
            number = float(number)
        lst.append(number)
avg = sum(lst) / len(lst)
print(avg)
