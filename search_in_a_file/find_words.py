file_name = input('Enter file name: ')
file_handle = open(file_name)
unique_words = list()

for line in file_handle:
    word = line.split()
    for item in word:
        if item not in unique_words:
            unique_words.append(item)
            unique_words.sort()
print(unique_words)
