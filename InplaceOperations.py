#Python follows PEMDAS rule. PEMDAS stands for Parentheses, Exponents, Multiplication and Division, and Addition
#and Subtraction.
a, b, c, d = 2, 3, 5, 7
a ** (b + c) # parentheses
256
a * b ** c # exponent: same as `a * (b ** c)`
7776
a + b * c / d # multiplication / division: same as `a + (b * c / d)`
4.142857142857142
#Extras: mathematical rules hold, but not always:
300 / 300 * 200
200.0
300 * 200 / 300
200.0
1e300 / 1e300 * 1e200
1e+200
1e300 * 1e200 / 1e300