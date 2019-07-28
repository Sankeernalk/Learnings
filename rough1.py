str_test = 'AB2C3'
k = 5
str_out = ''
for i in str_test:
    if len(str_out) == k+1:
        exit()
    else:
        if i.isdigit():
            str_out = str_out*int(i)
        else:
            str_out+=i
print(str_out)
print(str_out[k])

