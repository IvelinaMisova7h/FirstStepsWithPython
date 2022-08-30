file_name = input('Enter a file name: ')
if len(file_name) < 1:
    file_name = 'clown.txt'
file_handle = open(file_name)

di = dict()

for line in file_handle:
    line = line.rstrip()
    # print(line)
    words = line.split()
    # print(words)
    for word in words:
        #
        # # Second solution
        #
        #         # print('**', word, di.get(word, -99))
        #         old_count = di.get(word, 0)    # If the key is not there the count is zero
        #         print(word, 'old', old_count)
        #         new_count = old_count + 1
        #         di[word] = new_count
        #         print(word, 'new', new_count)
        #
        #         # The second solution in two lines. Idiom: retrieve/create/update counter
        di[word] = di.get(word, 0) + 1
#         print(word, 'new', di[word])
#
# # First solution
#         # print(word)
#         # if word in di:
#         #     di[word] += 1
#         #     print('Existing')
#         # else:
#         #     di[word] = 1
#         #     print('**NEW**')
#         # print(di[word])
#
#
# #print(di)
#

# Here we find the most common word.
largest = -1
the_word = None
for k, v in di.items():
    print(k, v)
    if v > largest:
        largest = v
        the_word = k  # Capture/remember the key that was largest.
print('Done', the_word, largest)
