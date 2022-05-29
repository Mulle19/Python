# 8 = 0b1000
8 >> 2
# Out: 2
# 2 = 0b10
print(bin(8 >> 2))
# Out: 0b10
#Performing a right bit shift of 1 is equivalent to integer division by 2:
print(36 >> 1)
# Out: 18
print(15 >> 1)
# Out: 7
#Performing a right bit shift of n is equivalent to integer division by 2**n:
print(48 >> 4)
# Out: 3
print(59 >> 3)
# Out: 7