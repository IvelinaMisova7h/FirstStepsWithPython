import re
# file_name = input('Enter a file name: ')
file_handle = open('mbox-short.txt')

for line in file_handle:
    line = line.rstrip()
    x = re.findall('\\d', line)
    if len(x) > 0:
        print(x)
