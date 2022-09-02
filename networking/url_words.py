import urllib.request

counts = dict()
file_handle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in file_handle:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)
