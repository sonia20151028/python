seat = []
min = 0
max=5
print(min<=len(seat)<max)
seat.append('z')
print(len(seat))
seat.append('a')
seat.append('a')
seat.append('a')
seat.append('b')
print(min<=len(seat)<max)
print(len(seat))
print(seat.pop(0))
print(min<=len(seat)<max)
print(seat[:])

#cant change the value of a tuple
t=(1,2,3,4,5,6,4,3)
print(t)
#t[0] = 100
print(t)

print(t[0])
print(t[:])
print(t[-1])
print(t[2:4])
print(t.index(3))
print(t.index(3,3))
print(t.count(3))
#help(list)
#help(tuple)
t=([1,2,3],[4,5,6])
print(t)
print(t[0],[2])
print(t[0][2])
print(type(t))
t[0][2]=100
print(t)
t=1,3,4
print(t)

#comma is mean a tuple
t=1,
print(type(t))
print(t)
t=()
print(type(t))
print(t)

t=1
print(type(t))
t=(1)
print(type(t))

t=('test')
print(type(t))
t=('test',)
print(type(t))

t=1,
#error tuple+int
#print(t+100)

print("############")
newTuple = (1,2,3)+(4,5,6)
print(newTuple)
newTuple=(1,2)+(2,3,4)
print(newTuple)

aTuple =(10,20)
x,y=aTuple
print(x,y)

x,y,z=(12,20,30)
print(x,y,z)
print(x,y)
x,y,z=12,20,30
print(x,y,z)

print("###################")
a=100
b=200
print(a,b)
a,b=b,a
print(a,b)

chose=('A','B','C')
answer=[]
answer.append('A')
answer.append('C')
print(chose)
print(answer)