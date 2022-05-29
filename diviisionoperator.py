a, b, c, d, e = 3, 2, 2.0, -3, 10
a / b # = 1
a / c # = 1.5
d / b # = -2
b / a # = 0
d / e # = -1
import operator # the operator module provides 2-argument arithmetic functions
operator.div(a, b) # = 1
operator.__div__(a, b) # = 1
from __future__ import division # applies Python 3 style division to the entire module
a / b # = 1.5
a // b # = 1
a / (b * 1.0) # = 1.5
1.0 * a / b # = 1.5
a / b * 1.0 # = 1.0 (careful with order of operations)
from operator import truediv
truediv(a, b) # = 1.5
float(a) / b # = 1.5
a / float(b) # = 1.5
a / b # = 1.5
e / b # = 5.0
a // b # = 1
a // c # = 1.0
import operator # the operator module provides 2-argument arithmetic functions
operator.truediv(a, b) # = 1.5
operator.floordiv(a, b) # = 1
operator.floordiv(a, c) # = 1.0
