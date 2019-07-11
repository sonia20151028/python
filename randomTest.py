import random
import time

print(random.randint(1,100))

#print(random.gammavariate(4,3))


v=0
for k in range(10):
    i = k+1
    print(str(v) + "+" + str(i) +"="+str(v+i))
    v = v+i

print("aa"+str(v))


for j in range(10):
    f=j+1
    print(str(f))