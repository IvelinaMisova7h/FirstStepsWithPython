file_name = input('Enter a file name: ')
if len(file_name) < 1 : file_name = 'clown.txt'
file_handle = open(file_name)

for line in file_handle:
    line = line.rstrip()
    # print(line)
    words = line.split()
    # print(words)
    for word in words:
        print(word)
