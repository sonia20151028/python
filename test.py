# -*- coding:UTF-8 -*-
print('aaa')
print('’‘')
tmp = 'bbb'
print(tmp)
tmp=2222
print(tmp)
#message = 'apple' + tmp + 'dollar'
#print (message)


message = 'apple' + str(tmp) + 'dollar'
print (message)


message = 'apple' * 3
print (message)


message = 90.9/3
print ('90.9/3='+str(message))


message = 90.9//3
print ('90.9//3='+str(message))


message = 90.0//3
print ('90.0//3='+str(message))

message = 10.0//3
print ('10.0//3='+str(message))

message = 10//3
print ('10//3='+str(message))

message = 2**3
print (message)


message += message
print(message)

message += 1
print(message)

message = '\o\p\n'
print(message)


message = '\o\p\\n'
print(message)


#message = message++
#print (message)


#s=input('please input sth :')
#print ('test result:' + s * 3)

print(type("aaa"))



#test=input('please input sth :')
#print ('test result:' + str(int(test) * 3))

nu = 100
if nu>90:
    print('nu>90')
elif nu==100:
    print('100')
else:
    print('nu < 90')

if nu>80:
    print('aaa')
    pass
    print('bbb')



i = 1
while i <=5:
    print('aa'+str(i))
    i=i+2


print('I am', 'a girl',36,'years old','right?', ' ')

print('I am',1000)


print('The quick brown fox', 'jumps over', 'the lazy dog')


for i in range(10):
    print(i, end=' ')

print('\\\n\\')
print(r'\\\n\\')


print('''line1
... line2
... line3''')


print('''line1
line2
line3''')


print (4>2)

print(10/3,10//3)