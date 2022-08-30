file_name = input('Enter a file name: ')
if len(file_name) < 1: file_name = 'clown.txt'
file_handle = open(file_name)

di = dict()

for line in file_handle:
    line = line.rstrip()
    # print(line)
    words = line.split()
    # print(words)
    for word in words:

# second solution

        # print('**', word, di.get(word, -99))
        old_count = di.get(word, 0)
        print(word, 'old', old_count)
        new_count = old_count + 1
        di[word] = new_count
        print(word, 'new', new_count)

# first solution
        # print(word)
        # if word in di:
        #     di[word] += 1
        #     print('Existing')
        # else:
        #     di[word] = 1
        #     print('**NEW**')
        # print(di[word])


print(di)
