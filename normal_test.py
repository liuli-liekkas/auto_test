import sys

i ='014f43ff8020017e'
str=''
for k in i:
    # print(k)
    j = bin(int(k, 16))
    # print(j)
    l = j[2:].rjust(4, '0')
    # print(l)
    str += l
print(str)
print(len(str))
print(str[8:21])
print(len(str[8:21]))
distance = int(str[8:21], 2) * 0.2 -500
print(distance)