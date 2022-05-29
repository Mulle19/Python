#1. Variables names must start with a letter or an underscore.
x = True # valid
_y = True # valid
9x = False # starts with numeral
#=> SyntaxError: invalid syntax 
$y = False # starts with symbol
=> SyntaxError: invalid syntax