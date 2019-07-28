encrypted = [89,111,117,114,32,115,112,101,99,115,32,105,115,32,103,111,111,100,33,33,33,33,33,33 ]
for e in encrypted:
    print(chr(e),sep='',end='')

warmtones = ['red','yellow','green','blue','pink']
print(warmtones[0])

palette = warmtones
palette1 = list(warmtones)
print(palette)
print(warmtones)
print(palette1)

del warmtones[-1]
print(warmtones)
print(palette)
print(palette1)

warmtones.extend(['brown'])

print(warmtones)
print(palette)
print(palette1)

del palette1[-2]
print(palette1)
print(warmtones)

palette1.extend(['mane'])
print(palette1)
print(warmtones)

palette1[0] = 'black'
print(palette1)
print(warmtones)
print(palette)