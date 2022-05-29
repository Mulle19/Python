# Existence check
2 in {1,2,3} # True
4 in {1,2,3} # False
4 not in {1,2,3} # True
# Add and Remove
s = {1,2,3}
s.add(4) # s == {1,2,3,4}
s.discard(3) # s == {1,2,4}
s.discard(5) # s == {1,2,4}
s.remove(2) # s == {1,4}
s.remove(2) # KeyError!s