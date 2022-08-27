file_handle = open('mbox-short.txt')


for line_x in file_handle:
    line_y = line_x.rstrip()
    print(line_y.upper())

