#while and for
count=0
while count<5:
    print(count)
    count += 1

count1=0
while True:
    if count1>5:
        break
    if count1 ==2:
        count1+=1
        continue
    print('this is count1',count1)
    count1+=1
#if has a break,it cant output
else:
    print('count1 is done')

count2 = 0
while count2>5:
    break
    count2+=1
else:
    print('count2 is done')

# input just like scanner or system.in in java
while True:
    word=input('input a word: ')
    if(word =='ok'):
        break
    print('next')

some_list=[1,2,3,4,5]
for i in some_list:
    print(i)

some_list1=['abc','def','ffg']
for j in some_list1:
    print(j)

for x in 'abcedf':
    print(x)

for str in ['abc','def','ffg']:
    print(str)
else:
    print('is done')

for i in range(10):
    print(i)

for i in range(3,7):
    print(i)

for i in range(1,10,2):
    print(i)

for _ in range(3):
    print('test')

#enumerate
for i,fruit in enumerate(['banana','tomato','pear']):
    print(i,fruit)
