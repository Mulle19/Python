a, b, c = 1, 2, 3
print(a, b, c)
# Output: 1 2 3
a, b, c = 1, 2
=> Traceback (most recent call last):
=> File "name.py", line N, in <module>
=> a, b, c = 1, 2
=> ValueError: need more than 2 values to unpack
a, b = 1, 2, 3
=> Traceback (most recent call last):
=> File "name.py", line N, in <module>
=> a, b = 1, 2, 3
=> ValueError: too many values to unpack