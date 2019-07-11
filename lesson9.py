def menu(**abc):
    for (k,v) in abc.items():
        print(k,v)

#menu(entree='beef',drink='coffee')

d={
    'entree':'beef',
    'drink':'beer',
    'dessert':'ice'
}
menu(**d)

def testFunc(pram1,pram2):
    """
    The function is for test
    """
    print(pram1)
    print(pram2)
    return True

print(testFunc.__doc__)
print("ffffffffffffffffffffffffffff")
help(testFunc)

#just use in this function,you can write a function in a function
def outer(a,b):
    def plus(c,d):
        return c-d
    r=plus(a,b)
    return r

print(outer(10,2))

def out1(a,b):
    def inner():
        return a + b
    return inner()

print(out1(2,5))

def out2(pi):
    def inner2(radius):
        return pi*radius*radius
    return inner2

cal1=out2(3.14)
cal2=out2(3.1415926)
print(cal1(10))
print(cal2(10))


