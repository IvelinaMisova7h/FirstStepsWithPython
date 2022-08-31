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
        # Idiom: retrieve/create/update counter
        di[word] = di.get(word, 0) + 1

# print(di)

tmp = list()
for k,v in di.items():
    # print(k,v)
    new_tuple = (v,k)
    tmp.append(new_tuple)

# print('Flipped: ', tmp)

tmp = sorted(tmp, reverse=True)
# print('Sorted: ', tmp[:5])

for v,k in tmp[:5]:
    print(k,v)
