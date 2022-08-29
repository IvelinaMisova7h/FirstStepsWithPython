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


# Another solution

# file_name = input('Enter the file name: ')
# try:
#     file_handle = open(file_name)
# except:
#     print('File cannot be opened:', file_name)
#     exit()
#
# counts = dict()
# for line in file_handle:
#     words = line.split()
#     for word in words:
#         if word not in counts:
#             counts[word] = 1
#         else:
#             counts[word] += 1
#
# print(counts)
