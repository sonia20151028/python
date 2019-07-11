import math
a='testaaa'
b=a
c=b

print(c)

print(1, type(1))

print('test', type('aa'))

test=True
print(test, type(False))

abc = int('980')
print(abc, type(abc))

#¥n is not right,\n is ok \=option+¥
print('abc¥r¥naaaa', '123', sep=',', end='¥n')
print('abc¥r¥naaaa', '123', sep=',', end='\n')
print('ttt', '123', sep='...')


print(8/7, type(8/7))

print(.99)

#only return part of integer
print(10//3)
print(10/3)
print(10%3)

#5*3
print(5*3)
#5*5*5
print(5**3)

#3.145
print(round(3.1425926,3))

print(math.isinf(099.3333))

print("test123")
print(456)

#print(help(math))
#if there is a '' in "",ok
print("I can't answer")
#error
#print('I can't answer)
#cant use ¥ mark
#print('I can¥'t answer')
print('I can\'t answer')
print('say "I can\'t answer"')
print("say \"I can't answer\"")

print('hello!\nHow a u')
#r=raw
print(r'c:\a\b')
print("#################")
#change line auto
print("""
line1"
"line2
line3
""")
print("#################")


print("#################")
#change line auto
print("""line1"
"line2
line3""")
print("#################")


print("#################")
#\from next line change,easy to read
print("""\
line1
"line2
line3\
""")
print("#################")


print('abc ' * 3 + 'zzz')

#the same result
print('a'+'b')
print('a''b')

#long string ,easy to read
s=('aaaaaaaaaaaaaaaaaaaaaaaaa'
  'bbbbbbbbbbbbbbbbbbbb')
#the same
s='aaaaaaaaaaaaaaaaaaaaaaaaa'\
'bbbbbbbbbbbbbbbbbbbb'
print(s)

word='test'
print(word[1])
print(word[-1])
print("###########################")
#the same
print(word[0:2])
print(word[:2])

#the same
print(word[2:4])
print(word[2:])

#error
#word[0]='a'
word='a'+word[1:]
print("###########################")
#word[:]=word
print(word[:])
print(len(word))