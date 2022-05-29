x = True
y = True
z = print(x or y) # z = True
x = True
y = False
z = print(x or y) # z = True
x = False
y = True
z = print(x or y) # z = True

x = False
y = False
z = print(x or y) # z = False
x = 1
y = 1
z = print(x or y) # z = x, so z = 1, see `and` and `or` are not guaranteed to be a boolean
x = 1
y = 0
z = print(x or y) # z = x, so z = 1 (see above)
x = 0
y = 1
z = print(x or y) # z = y, so z = 1 (see above)
x = 0
y = 0
z =print( x or y) # z = y, so z = 0 (see above)