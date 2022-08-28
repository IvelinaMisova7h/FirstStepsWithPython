file_name = input('Enter a file name: ')
file_handle = open(file_name)

counts = dict()

for line in file_handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

print(counts)
