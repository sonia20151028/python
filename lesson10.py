def print_info(func):
    def wrapper(*args,**kwargs):
        print('Start')
        result = func(*args,**kwargs)
        print('End')
        return result
    return wrapper


def print_more(func):
    def wrapper(*args,**kwargs):
        print('func:',func.__name__)
        print('args:',args)
        print('kwargs:',kwargs)
        result = func(*args,**kwargs)
        print('result:',result)
        return result
    return wrapper

@print_info
@print_more
def addNum(y,z):
    return y+z
print(addNum(13,24))
#
# f = (print_info(addNum))
# print(f(13,29))



li=['Mon','tus','ths','Wed','fri']
def change_words(words,func):
    for word in words:
        print(func(word))

print("#############################")
# def sample_func(word):
#     return word.capitalize()
# def sample_func(word):
#     return word.XXXX()
# def sample_func(word):
#     return word.ZZZZ()
# sample_func=lambda word:word.capitalize()

# change_words(li,sample_func)

change_words(li,lambda word:word.capitalize())
# change_words(li,lambda word:word.XXXX())
# change_words(li,lambda word:word.ZZZZ())


print("#############################")
greetingList = ['Good Morning','Good afternoon','Good evening']

for ind in greetingList:
    print(ind)


print("#############################")
def greeting():
    yield 'Good Morning'
    yield 'Good afternoon'
    yield 'Good evening'
for g in greeting():
    print(g)


print("#############################")
gre = greeting()
def counter(num=10):
    for _ in range(num):
        yield 'run'
cou = counter()
print(next(gre))
print(next(gre))
print(next(cou))
print(next(gre))

