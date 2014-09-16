from string import maketrans

a=maketrans(' ', ' ')[97:123]
b=list(a)
b.extend(['a','b'])
b.pop(0)
b.pop(0)
b=''.join(b)
table=maketrans(a, b)
print"map".translate(table)