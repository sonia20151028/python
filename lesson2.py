#error:abc is not a variable
#print(abc)
print('abc')

s='It is time to go lunch,is'
print(s.find('is'))
print(s.rfind('is'))
print(s.count('is'))
#It Is Time To Go Lunch,Is
print(s.title())
print(s.replace('is','are'))

print('a is {}'.format('test'))
print('a is {} {} {}'.format('test','tset','poiu'))
print('a is {0} {1} {2}'.format('test','tset','poiu'))
print('a is {2} {0} {1}'.format('test','tset','poiu'))


print('my name is {0} {1} ,you can call me {1}'.format('wang','xiaomei'))
print('my name is {familyName} {name} ,you can call me {name}'.format(familyName='wang',name='xiaomei'))


print(str(2344.33),type(str(2344.33)))

a = 'z'
print(f'a is {a}')


x, y, z = 1, 2, 3
print(f'a is {x}, {y}, {z}')
print(f'a is {z}, {y}, {x}')

name = 'Jun'
family = 'Sakai'
print(f'My name is {name} {family}. Watashi ha {family} {name}')


l=[12,3,34,45,56]
print(l)
print(l[0]+l[1])
print(l[-1])
print(l[0:3])
print(l[:3])
print(l[3:])
print(l[:])
print(len(l))
print(type(l))

print(list('abcdefg'))

n=[1,2,3,4,5,6,7,8,9,10]
print(n[::1])
print(n[::2])
print(n[::3])
print(n[::-1])

aa=[1,2,3]
bb=['a','b','c','d','e']
zz=[aa,bb]
print(zz)
print(zz[1])
print(zz[1][2])

bb[1]='KKK'
print(bb)
print(bb[2:5])
bb[2:4]=['zz','ff']
print(bb)
bb[1:3]=[]
print(bb)
bb[:]=[]
print(bb)

n=[1,2,3,4,5,6,7,8,9,10]
n.append(99)
print(n)
n.insert(1,77)
print(n)
print("###### pop(): remove a object from list,and show the object concent ##########")
print(n.pop())
print(n.pop(0))
print(n)
n.remove(6)
print(n)
print("###### remove(): remove the object from list ##########")
del n[4]
print(n)
del n

a=[1,2,3,4,5]
b=[6,7,8,9,10]
a+=b
print(a)
print("###### a: a+=b two list union ##########")

c=[1,2,3,4,5]
d=[6,7,8,9,10]
c.extend(d)
print(c)

r=[0,1,2,3,1,5,2,7]
print(r.index(2))
print(r.index(2,3))
print(r.count(2))

if 5 in r:
    print('have if 5 in r')

r.sort()
print(r)
r.sort(reverse=True)
print(r)
r.reverse()
print(r)
print("reverse r")

str='My name is test'
strSplit = str.split(' ')
print(strSplit)

strJoin=' $$ '.join(strSplit)
print(strJoin)

i=[1,2,3,4,5]
j=i
j[0]=100
print('i= ',i)
print('j= ',j)

ii=[1,2,3,4,5]
jj=ii.copy()
jj[0]=100
print('ii= ',ii)
print('jj= ',jj)

iii=[1,2,3,4,5]
jjj=iii[:]
jjj[0]=100
print('iii= ',iii)
print('jjj= ',jjj)