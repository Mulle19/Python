a = '123.456'
b = float(a)
d = int(b) # 123
#c = int(a) # ValueError: invalid literal for int() with base 10: '123.456'
print(b)
#print(c)
print(d)
a = 'hello'
list(a) # ['h', 'e', 'l', 'l', 'o']
set(a) # {'o', 'e', 'l', 'h'}
tuple(a) # ('h', 'e', 'l', 'l', 'o')
print(a)