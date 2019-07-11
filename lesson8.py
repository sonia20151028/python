#zip
days=['mon','tus','wes']
fruits = ['apple','banana','orange']
drinks=['water','juice','coffee']
for day,fruit,drink in zip(days,fruits,drinks):
    print(day,fruit,drink)

#about map for
d={'x':100,'y':200}
print(d.items())
for k,v in d.items():
    print(k,' ',v)

#about function
def saySth():
    print('abcdefg')

saySth()
#function
print(type(saySth))
#NoneType
#print(type(saySth()))

def saySth1():
    s='ffffff'
    return s
result =saySth1()
print('result',result)

def whatIsThis(color):
    print(color)
whatIsThis('green')

def addNum(a:int,b:int)->int:
    return a+b
r=addNum(10,20)
print(r)
r=addNum('a','b')
print(r)

def menu(entree='beef',drink='beer',dessert='ice'):
    print(entree,drink,dessert)
menu()
menu(entree='lamb')


def testFunc(x,l=[]):
    l.append(x)
    return l
x=[1,2,3]
ret = testFunc(100,x)
print(ret)

test1=testFunc(100)
print(test1)
test1=testFunc(100)
print(test1)

# function initalization
def testFunc(x,l=None):
    if l is None:
        l=[]
    l.append(x)
    return l
x=[1,2,3]
ret = testFunc(100,x)
print(ret)
x=[1,2,3]
ret = testFunc(100,x)
print(ret)

test1=testFunc(100)
print(test1)
test1=testFunc(100)
print(test1)

def wantSay(*args):
    for arg in args:
        print(arg)
wantSay('I','am','a','genius')

def wantSay1(word,*args):
    print('word= ',word)
    for arg in args:
        print(arg)
#not used frequently
taple=('I','am','a','genius')
wantSay1('Hi',*taple)
#should remember this kind of writing
wantSay1('I','am','a','genius')
