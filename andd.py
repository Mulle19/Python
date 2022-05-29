x = True
y = True
z =print( x and y) # z = True
x = True
y = False
z =print( x and y) # z = False
x = False
y = True
z = print(x and y) # z = False
x = False
y = False
z =print( x and y) # z = False
x = 1
y = 1
z =print( x and y) # z = y, so z = 1, see `and` and `or` are not guaranteed to be a boolean
x = 0
y = 1
z =print( x and y) # z = x, so z = 0 (see above)
x = 1
y = 0
z =print( x and y) # z = y, so z = 0 (see above)
x = 0
y = 0
z = print(x and y) # z = x, so z = 0 (see above)