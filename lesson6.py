x=-10
if x<0:
    print('negative')
elif x==0:
    print('zero')
else:
    print('positive')


a=10
b=5
if a==10:
    print(' a is 10')
    if b>0:
        print('b > 0')
if not a==b:
    print('a not equal b')

c=10
d=10
print(c==d)
print(c!=d)
print(c>d)
print(c<d)
print(c>0 and d>0)
print(c>0 or d>0)


e=[1,2,3]
f=1
if f in e:
    print('f in e')

if 100 not in e:
    print('100 not in e')

is_ok = True
if is_ok:
    print('is ok  is true')
elif not is_ok:
    print('is ok is not true')

is_test=0
if is_test:
    print('is true')
else:
    print('is false')

if_test =1
if if_test:
    print('true')
else:
    print('false')

if_test1 =100000
if if_test1:
    print('100000 is true')
else:
    print('100000 is false')

if_test2 ='aaaaaaaa'
if if_test2:
    print('aaaaaaaa is true')
else:
    print('aaaaaaaa is false')

if_test3 =''
if if_test3:
    print('empty is true')
else:
    print('empty is false')

if_test4 =[]
if if_test3:
    print('list is true')
else:
    print('list is false')

#about false:Flase,0,0.0,'',[],(),{},set()


is_empty=None
if is_empty is None:
    print('is_empty is None')
elif is_empty is not None:
    print('is_empty is Not None')


print(1==True)
print(1 is True)