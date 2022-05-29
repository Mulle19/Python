a, b = 1, 2
# Using the "+" operator:
a + b 
# Using the "in-place" "+=" operator to add and assign:
a += b # a = 3 (equivalent to a = a + b)
import operator # contains 2 argument arithmetic functions for the examples
operator.add(a, b) # = 5 since a is set to 3 right before this line
# The "+=" operator is equivalent to:
a = operator.iadd(a, b) # a = 5 since a is set to 3 right before this line
"first string " + "second string" # = 'first string second string'
[1, 2, 3] + [4, 5, 6] # = [1, 2, 3, 4, 5, 6]