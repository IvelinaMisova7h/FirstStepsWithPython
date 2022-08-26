x = 'X-DSPAM-Confidence: 0.8475'

i_pos = x.find(':')
print(i_pos)
piece = x[i_pos + 2:]
print(piece)
print(piece+42.0)  # Will fail
value = float(piece)
print(value)
print(value+42.0)
