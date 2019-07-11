a={1,2,3,4,5,6,7,8,2,3,4}
print(a)
print(type(a))

b={1,3,5,0}
print('a=',a)
print('b=',b)
print('a-b=',a-b)
print('b-a=',b-a)
print('a&b=',a&b)
print('a|b=',a|b)
print('a^b=',a^b)
#error
#print(a+b)

s={1,2,3,4,5}
print(s)
s.add(6)
print(s)
s.add(6)
print(s)
s.remove(5)
print(s)
s.clear()
print(s)
#print(s[0])

myFriend={'A','B','D','E'}
aFriend={'D','K','J','G'}
print(myFriend&aFriend)

fruits=['apple','banana','apple','banana']
kind=set(fruits)
print(kind)


"""
This is a commont about multi rows
"""

astr="aaaaaaaaaaaaa"+"bbbbbbbbbbbbbbb"
astr="aaaaaaaaaaaaa"\
     +"bbbbbbbbbbbbbbb"
print(astr)

astr=("aaaaaaaaaaaaa"
     +"bbbbbbbbbbbbbbb")
print(astr)