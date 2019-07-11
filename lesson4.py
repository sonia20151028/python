d={'x':10,'y':50}
print(d)
print(type(d))
print(d['x'],d['y'])
d['x']=100
print(d)
d['x']='xxxxxx'
print(d)
d['z']='zzzzzz'
print(d)
d[1]=10000
print(d)
print(d.keys())

a=dict(a=10,b=20)
print(a)
a=dict([('f',10),('k',20)])
print(a)
#help(a)


c={'x':10,'y':50}
print(c.keys())
print(c.values())
print('c= ',c)
c1={'x':1000,'z':900}
print(c1)
c.update(c1)
print(c)
print('c1= ',c1)

print(c.get('x'))
print(c['x'])
print(c.get('xx'))
type(c.get('xx'))
c.pop('x')
del c['y']
print('removed c=',c)
del c
#exception null,but hasn't show next
#print(c)

e={'x':10,'y':20}
print('not cleared d=',e)
e.clear()
print('cleared d=',e)

e={'x':10,'y':20}
print('x' in e)

f={'x':10,'y':20}
g=f
g['x']=1000
print(f)
print(g)

h={'x':10,'y':20}
i=h.copy()
i['x']=100
print(h)
print(i)

fruits = {
    'apple':100,
    'orange':200,
    'tomato':300
}
print(fruits['orange'])

l=[
    ['apple',100],
    ['orange',200],
    ['tomato',300]
]
print(l[0][1])