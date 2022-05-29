a = '123'
print(type(a))
#GoalKicker.com – Python® Notes for Professionals 14
# Out: <class 'str'>
b = 123
print(type(b))
# Out: <class 'int'>

i = 7
if isinstance(i, int):
 i += 1
elif isinstance(i, str):
 i = int(i)
 i += 1
