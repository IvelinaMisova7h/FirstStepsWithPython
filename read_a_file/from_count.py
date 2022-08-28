file_name = input('Enter a file name: ')
file_handle = open(file_name)

for line in file_handle:
    t = line.rstrip()
    word = line.split()
    if len(word) < 1 or word[0] != 'From':  # Guardian in a compound statement.
        continue
    print(word[1])
