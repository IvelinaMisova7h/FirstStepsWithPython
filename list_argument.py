def chop(t):
    r = t[0::4]
    return r


letters = ['a', 'h', 'd', 'u', 'm']
rest = chop(letters)
print(rest)


def middle(d):
    s = d[1:4]
    return s


numbers = ['2', '3', '4', '9', '7']
p = middle(numbers)
print(p)
